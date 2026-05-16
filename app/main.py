import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Email Generator")

    # Initialize session state for button disable tracking and email storage
    if "generating" not in st.session_state:
        st.session_state.generating = False
    if "generated_emails" not in st.session_state:
        st.session_state.generated_emails = []

    url_input = st.text_input("Enter the URL of the job description")
    submit_button = st.button("Generate Email", disabled=st.session_state.generating)

    if submit_button and not st.session_state.generating:
        st.session_state.generating = True
        try:
            with st.spinner("Generating email..."):
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                emails = []
                for job in jobs:
                    links = portfolio.query_link(job["skills"])
                    email = llm.generate_email(job, links)
                    emails.append({"role": job["role"], "email": email})
                st.session_state.generated_emails = emails
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            st.session_state.generating = False

    # Display generated emails
    for item in st.session_state.generated_emails:
        st.subheader(f"Generated Email for {item['role']}")
        st.code(item["email"], language="markdown")


if __name__ == "__main__":

    llm_chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(llm_chain, portfolio, clean_text)
