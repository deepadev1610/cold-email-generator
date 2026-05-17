# Cold Email Generator

An intelligent, fully dynamic cold email generation system that automatically creates personalized outreach emails by analyzing job descriptions and matching them with your portfolio. Powered by AI, optimized for sales and business development teams.

## 🌟 What Makes It Different?

Unlike static email templates, this tool generates **truly personalized cold emails** by:

- Taking your **company information** (name, description, services)
- Using your **employee details** (name, designation)
- Uploading your **portfolio projects** (dynamically via CSV)
- Analyzing **job postings** to extract key requirements
- Matching portfolio skills with job requirements
- Generating emails **contextually relevant** to each opportunity

## ✨ Features

- **🔍 Intelligent Job Extraction**: Automatically parse career pages and extract job details (role, experience, skills, description) using LangChain and Groq's Llama 3.3 LLM
- **🎯 Smart Portfolio Matching**: Semantically match job requirements with your portfolio projects using ChromaDB vector database - shows only relevant work
- **✉️ AI-Powered Email Generation**: Generate professional, personalized cold emails that:
  - Include your company context and values
  - Reference your relevant portfolio projects
  - Address specific job requirements
  - Include professional sign-off with your details
- **🎨 Dynamic Configuration**: Change company, employee, and portfolio information **per session** - no code changes needed
- **📤 CSV Portfolio Upload**: Upload your projects via simple CSV - no databases or complex setup required
- **🎛️ Interactive Sidebar UI**: All configuration in an intuitive sidebar, job input on main screen
- **✅ Input Validation**: Comprehensive validation ensures all required fields are filled before generation
- **🚀 Real-time Feedback**: Spinner feedback and error messages guide you through the process
- **📊 Portfolio Preview**: See what projects are in your database before generating emails
- **📊 Jupyter Integration**: Explore and experiment with the pipeline using interactive notebooks

## 💼 Perfect For

- **Sales Teams**: Generate personalized outreach to potential clients
- **Business Development**: Create targeted proposals based on job requirements
- **Recruitment Agencies**: Customize pitches for different client profiles
- **Freelancers & Consultants**: Tailor proposals to specific opportunities
- **B2B Marketers**: Create contextualized cold emails at scale

## 🛠️ Tech Stack

- **LLM**: Groq API with Llama 3.3 70B model
- **Vector Database**: ChromaDB for semantic portfolio retrieval
- **Web Framework**: Streamlit with custom sidebar configuration
- **Data Processing**: Pandas for CSV handling, LangChain for orchestration
- **Web Scraping**: BeautifulSoup4, Requests
- **Python**: 3.8+

## 📋 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/deepadev1610/cold-email-generator.git
   cd cold-email-generator
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### Local Development Setup

1. **Get Groq API Key**:
   - Visit [Groq Console](https://console.groq.com)
   - Sign up or log in
   - Create an API key

2. **Set up environment variables**:
   Create a `.streamlit/secrets.toml` file:

   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

   Or use a `.env` file:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Streamlit Cloud Deployment

1. **Add Secrets in Streamlit Cloud Dashboard**:
   - Go to your deployed app → Settings (gear icon)
   - Click "Secrets" tab
   - Paste your API key:
     ```toml
     GROQ_API_KEY = "your_actual_api_key_here"
     ```
   - Click "Save"

2. **Secrets are NOT committed to GitHub** ✅ Already in `.gitignore`

### Portfolio Setup

**Option 1: Upload CSV via Web Interface (Recommended)**

- In the app's sidebar, upload your portfolio CSV file
- Required columns: `TechStack`, `Links`
- Example format:
  ```csv
  TechStack,Links
  React Node.js MongoDB,https://github.com/project1
  Python FastAPI PostgreSQL,https://github.com/project2
  Vue.js Express.js MySQL,https://github.com/project3
  Kubernetes Docker AWS,https://github.com/project4
  ```
- Portfolio persists in ChromaDB for the session

**Option 2: Default Portfolio File**

- Place file at `app/resources/portfolios.xlsx`
- Same column structure: `TechStack` and `Links`
- Used if no CSV is uploaded

## 🚀 Usage

### Running the Web App

```bash
streamlit run app/main.py
```

Then open your browser to `http://localhost:8501`

### Step-by-Step Walkthrough

#### 1. **Configure in Sidebar (Left Panel)**

- **Your Details**:
  - Enter your full name
  - Enter your job designation (e.g., "Sales Executive", "BDE", "Account Manager")
- **Company Details**:
  - Company name
  - Company description (highlight services, expertise, unique value proposition)
- **Portfolio**:
  - Upload your portfolio CSV file
  - View portfolio preview to verify upload

#### 2. **Generate Email (Main Panel)**

- Paste job posting URL from LinkedIn, company careers page, etc.
- Click "Generate Email"
- Wait for LLM to analyze and generate

#### 3. **Review & Copy**

- Review generated email
- Check automatically matched portfolio projects
- Copy email and customize as needed
- Send to prospect!

### UI Layout

```
┌─────────────────────────────────────────────────────────┐
│                    SIDEBAR (Left)                │ MAIN CONTENT (Right)      │
├──────────────────────────────────┤───────────────────────┤
│  ⚙️ Configuration                 │   🚀 Cold Email Gen  │
│  ┌─────────────────────────────┐  │  ┌─────────────────┐ │
│  │ 👤 Your Details             │  │  │ Paste Job URL   │ │
│  │ Name: ________________       │  │  │ [________...]   │ │
│  │ Designation: ________        │  │  │  [Generate]     │ │
│  └─────────────────────────────┘  │  └─────────────────┘ │
│  ┌─────────────────────────────┐  │                      │
│  │ 🏢 Company Details          │  │  📬 Generated Email  │
│  │ Name: ________________       │  │  ┌─────────────────┐ │
│  │ Description: _________       │  │  │ Hi [Hiring...   │ │
│  │ ___________________           │  │  │ ...             │ │
│  └─────────────────────────────┘  │  │ [📋 Copy]       │ │
│  ┌─────────────────────────────┐  │  └─────────────────┘ │
│  │ 📁 Portfolio Management      │  │                      │
│  │ [Choose File] portfolio.csv   │  │                      │
│  │ ✅ Loaded 4 projects         │  │                      │
│  │ [Show Preview] ▼              │  │                      │
│  └─────────────────────────────┘  │                      │
└──────────────────────────────────┴───────────────────────┘
```

## 📊 How It Works

### Complete Workflow

1. **Configuration Step** (Sidebar):
   - Enter personal details: name, designation
   - Enter company info: name, description
   - Upload portfolio CSV with your projects

2. **Input Step** (Main):
   - Paste job posting URL
   - System validates all required fields

3. **Analysis Phase**:
   - WebBaseLoader scrapes job posting
   - Text cleaning removes HTML/noise
   - LLM extracts: role, skills, experience, requirements

4. **Matching Phase**:
   - ChromaDB searches portfolio against extracted skills
   - Returns 2 most relevant projects
   - Projects include tech stack and links

5. **Generation Phase**:
   - LLM generates personalized email using:
     - Your company context
     - Your details (name, designation)
     - Job requirements
     - Matched portfolio projects
     - Professional best practices

6. **Display Phase**:
   - Email shown in UI
   - Portfolio matches highlighted
   - Ready to copy and customize

### Data Flow Diagram

```
Job URL Input
    ↓
WebBaseLoader (scrape)
    ↓
Text Cleaning (clean_text)
    ↓
Job Extraction (extract_jobs via LLM)
    ↓ gets: role, skills, experience
    ↓
ChromaDB Query (query portfolio by skills)
    ↓
LLM Email Generation (with company context)
    ↓
Personalized Cold Email Output
```

### Concrete Example

**Input:**

- Name: Sarah Johnson
- Designation: Enterprise Sales Manager
- Company: CloudFirst Solutions
- Company Description: "We provide enterprise cloud infrastructure and DevOps consulting"
- Portfolio: AWS projects, Kubernetes, Docker
- Job URL: LinkedIn → Senior Cloud Engineer

**Processing:**

- Extract: Role="Senior Cloud Engineer", Skills=["AWS", "Kubernetes", "Docker"], Experience="5+ years"
- Match: Find 2 portfolio projects with AWS + Kubernetes + Docker
- Generate: Email from Sarah about CloudFirst's DevOps expertise, mentioning matched projects

**Output:**

```
Hi [Hiring Manager],

I came across your Senior Cloud Engineer opening and was impressed by your
focus on scalable infrastructure. At CloudFirst Solutions, we specialize in
exactly this - building and managing enterprise-grade cloud environments.

We recently delivered:
- [Project 1: AWS + Kubernetes infrastructure link]
- [Project 2: Docker container orchestration link]

I'd love to discuss how our expertise might benefit your team and potentially
explore partnership opportunities.

Best regards,
Sarah Johnson
Enterprise Sales Manager
CloudFirst Solutions
```

## 📁 Project Structure

```
cold-email-generator/
├── app/
│   ├── main.py                  # Streamlit app with sidebar config
│   ├── chains.py                # LangChain pipeline (extraction + generation)
│   ├── portfolio.py             # Portfolio management (CSV upload + ChromaDB)
│   ├── utils.py                 # Text cleaning utilities
│   └── resources/
│       └── portfolios.xlsx      # Optional: default portfolio file
├── .streamlit/
│   ├── secrets.toml.example     # Template for secrets
│   └── config.toml              # Streamlit theme & config
├── email-generator.ipynb        # Jupyter notebook for experimentation
├── requirements.txt             # Dependencies
├── .gitignore                   # Excludes secrets, portfolios
└── README.md                    # This file
```

## 🔑 API Keys & Secrets

### Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Create an account or sign in
3. Go to API Keys section
4. Create a new API key
5. Copy the key

### Storing Secrets Safely

**Local Development:**

```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"
```

**Streamlit Cloud:**

- App Settings → Secrets
- Paste the same format

**Never commit secrets to GitHub** ✅ Both `.env` and `.streamlit/secrets.toml` are in `.gitignore`

## 📦 Requirements

See `requirements.txt`:

```
langchain-groq==0.1.3
langchain-core==0.1.52
langchain-community==0.0.38
python-dotenv==1.0.0
pandas>=2.2.0
chromadb==0.4.24
streamlit==1.41.0
beautifulsoup4>=4.11.0
requests>=2.28.0
ipywidgets==8.1.1
openpyxl==3.1.5
```

## 🛠️ Troubleshooting

| Issue                         | Solution                                                                      |
| ----------------------------- | ----------------------------------------------------------------------------- |
| **Email generation fails**    | Check Groq API key is valid and has credits                                   |
| **Portfolio CSV not loading** | Ensure CSV has `TechStack` and `Links` columns (exact spelling)               |
| **Portfolio not matching**    | Add relevant tech keywords to TechStack column matching job requirements      |
| **Job URL won't load**        | Some sites block scrapers; try direct job posting link instead of search page |
| **Missing dependencies**      | Run `pip install -r requirements.txt` again                                   |
| **Secrets.toml not found**    | Create `.streamlit/secrets.toml` with your API key locally                    |

## ✅ What's New (v2.0)

**Dynamic Configuration Features:**

- ✅ User/employee name and designation in sidebar
- ✅ Company name and description for contextualized emails
- ✅ CSV portfolio upload (no database setup needed)
- ✅ Portfolio preview before generation
- ✅ Dynamic portfolio switching per session
- ✅ Input validation for all required fields
- ✅ Real-time feedback during generation
- ✅ Better error messages and UI feedback

**Email Enhancements:**

- ✅ Company context automatically included in email body
- ✅ Sender name and designation in sign-off
- ✅ Emails reference company expertise and values
- ✅ Portfolio projects matched to job requirements
- ✅ Professional, personalized tone

**UX Improvements:**

- ✅ Sidebar-based configuration (cleaner layout)
- ✅ Portfolio preview feature
- ✅ Copy button for easy sharing
- ✅ Email details expandable section
- ✅ Better visual hierarchy with containers

## 🚦 Future Enhancements

- [ ] Email template selection (formal, casual, technical, etc.)
- [ ] Multi-language email generation
- [ ] A/B testing email variants
- [ ] Batch processing (upload multiple URLs)
- [ ] Email sending integration (Gmail API)
- [ ] Response tracking dashboard
- [ ] Email history/archive in database
- [ ] Additional personalization fields (recruiter name, company size, etc.)
- [ ] LinkedIn job board integration
- [ ] Custom prompt builder
- [ ] Follow-up email sequences

## 🤝 Contributing

Contributions welcome! You can:

- Report bugs via GitHub issues
- Suggest features
- Submit pull requests
- Share ideas for improvements

## 📄 License

MIT License - Free for personal and commercial use

## 💬 Support & Questions

- Open an issue on GitHub
- Check existing issues for common problems
- Review the Troubleshooting section above

---

<div align="center">

**Built with ❤️ using LangChain, Groq, and Streamlit**

⭐ If you find this useful, consider giving it a star on GitHub!

</div>
