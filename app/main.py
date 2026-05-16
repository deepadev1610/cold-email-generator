import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
import pandas as pd


def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(page_title="Cold Email Generator", layout="wide")
    st.title("🚀 Cold Email Generator")

    # Initialize session state
    if "generating" not in st.session_state:
        st.session_state.generating = False
    if "generated_emails" not in st.session_state:
        st.session_state.generated_emails = []
    if "portfolio_loaded" not in st.session_state:
        st.session_state.portfolio_loaded = False

    # ============ SIDEBAR - USER & COMPANY CONFIGURATION ============
    with st.sidebar:
        st.header("⚙️ Configuration")

        st.subheader("👤 Your Details")
        employee_name = st.text_input("Your Name", placeholder="e.g., John Doe")
        designation = st.text_input(
            "Your Designation", placeholder="e.g., Business Development Executive"
        )

        st.subheader("🏢 Company Details")
        company_name = st.text_input(
            "Company Name", placeholder="e.g., TechCorp Solutions"
        )
        company_description = st.text_area(
            "Company Description/About",
            placeholder="Describe your company, its services, expertise, and unique value proposition...",
            height=150,
        )

        st.subheader("📁 Portfolio Management")
        st.write("Upload a CSV file with your portfolio projects")
        st.write("Required columns: `TechStack`, `Links`")

        portfolio_file = st.file_uploader("Upload Portfolio CSV", type="csv")

        if portfolio_file:
            try:
                df = pd.read_csv(portfolio_file)

                # Validate columns
                if "TechStack" not in df.columns or "Links" not in df.columns:
                    st.error("❌ CSV must contain 'TechStack' and 'Links' columns")
                else:
                    # Load portfolio
                    portfolio.load_portfolio_from_dataframe(df)
                    st.session_state.portfolio_loaded = True
                    st.success(f"✅ Loaded {len(df)} projects from portfolio")

                    # Show preview
                    with st.expander("📊 Portfolio Preview"):
                        st.dataframe(df, use_container_width=True)
            except Exception as e:
                st.error(f"Error loading portfolio: {str(e)}")
        else:
            # Try to load default portfolio
            if portfolio.data is not None and not portfolio.data.empty:
                st.info(f"ℹ️ Using default portfolio ({len(portfolio.data)} projects)")
                st.session_state.portfolio_loaded = True

    # ============ MAIN CONTENT - JOB POSTING & EMAIL GENERATION ============
    st.subheader("📧 Generate Cold Email")

    col1, col2 = st.columns([3, 1])

    with col1:
        url_input = st.text_input(
            "Paste Job Posting URL",
            placeholder="https://careers.example.com/job/...",
            label_visibility="visible",
        )

    with col2:
        submit_button = st.button(
            "Generate Email",
            disabled=st.session_state.generating,
            use_container_width=True,
        )

    # ============ VALIDATION & EMAIL GENERATION ============
    if submit_button:
        # Validate inputs
        errors = []
        if not employee_name.strip():
            errors.append("Please enter your name")
        if not designation.strip():
            errors.append("Please enter your designation")
        if not company_name.strip():
            errors.append("Please enter your company name")
        if not company_description.strip():
            errors.append("Please enter company description")
        if not url_input.strip():
            errors.append("Please enter a job posting URL")
        if not st.session_state.portfolio_loaded:
            errors.append(
                "Please upload your portfolio CSV or ensure default portfolio is loaded"
            )

        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            st.session_state.generating = True
            try:
                with st.spinner("🔄 Generating email..."):
                    # Load job posting
                    loader = WebBaseLoader([url_input])
                    data = clean_text(loader.load().pop().page_content)

                    # Extract job details
                    jobs = llm.extract_jobs(data)
                    emails = []

                    for job in jobs:
                        # Query portfolio for relevant links
                        links = portfolio.query_link(job.get("skills", []))

                        # Generate email with user details
                        email = llm.generate_email(
                            job_description=job,
                            links=links,
                            employee_name=employee_name,
                            designation=designation,
                            company_name=company_name,
                            company_description=company_description,
                        )

                        emails.append(
                            {
                                "role": job.get("role", "Unknown Position"),
                                "email": email,
                            }
                        )

                    st.session_state.generated_emails = emails
                    st.success("✅ Email generated successfully!")

            except Exception as e:
                st.error(f"❌ Error generating email: {str(e)}")
            finally:
                st.session_state.generating = False

    # ============ DISPLAY GENERATED EMAILS ============
    if st.session_state.generated_emails:
        st.divider()
        st.subheader("📬 Generated Emails")

        for idx, item in enumerate(st.session_state.generated_emails):
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.subheader(f"📌 {item['role']}")
                with col2:
                    if st.button("📋 Copy", key=f"copy_{idx}"):
                        st.toast("Copied to clipboard!")

                st.markdown(item["email"])

                # Email details
                with st.expander("ℹ️ Email Details"):
                    st.write(f"**To:** Hiring Manager for {item['role']}")
                    st.write(
                        f"**From:** {employee_name}, {designation} at {company_name}"
                    )


if __name__ == "__main__":
    llm_chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(llm_chain, portfolio, clean_text)
