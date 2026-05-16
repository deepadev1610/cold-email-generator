# Cold Email Generator

An intelligent cold email generation system that automatically creates personalized outreach emails by analyzing job descriptions and matching them with relevant portfolio examples.

## Features

- **🔍 Job Extraction**: Automatically parse career pages and extract job details (role, experience, skills, description) using LangChain and Groq's Llama 3.3 LLM
- **🎯 Portfolio Matching**: Semantically match job requirements with relevant portfolio projects using ChromaDB vector database
- **✉️ Email Generation**: Generate professional, personalized cold emails highlighting how your services match job requirements
- **🎨 Interactive UI**: Streamlit web application for easy job posting input and email generation
- **📊 Jupyter Integration**: Explore and experiment with the pipeline using interactive notebooks

## Tech Stack

- **LLM**: Groq API with Llama 3.3 70B model
- **Vector Database**: ChromaDB for semantic portfolio retrieval
- **Web Framework**: Streamlit
- **Data Processing**: Pandas, LangChain
- **Python**: 3.8+

## Installation

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

## Configuration

### Local Development

1. **Set up environment variables**:
   Create a `.streamlit/secrets.toml` file in the project root (for local testing):

   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

   Alternatively, you can use a `.env` file:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Streamlit Cloud Deployment

1. **Add Secrets in Streamlit Cloud Dashboard**:
   - Go to your app settings (gear icon)
   - Click "Secrets" tab
   - Paste your API key in TOML format:
     ```toml
     GROQ_API_KEY = "your_actual_api_key_here"
     ```
   - Click "Save"

2. **Don't push `.env` or `secrets.toml` to GitHub** ✅ Already in `.gitignore`

### Portfolio Data Setup

**Option 1: Upload CSV via Web Interface (Recommended)**

- In the Streamlit app sidebar, upload your portfolio CSV file
- Required columns: `TechStack` and `Links`
- Example CSV format:
  ```
  TechStack,Links
  React Node.js MongoDB,https://github.com/project1
  Python FastAPI PostgreSQL,https://github.com/project2
  Vue.js Express.js MySQL,https://github.com/project3
  ```

**Option 2: Default Portfolio File**

- Place your portfolio file at `app/resources/portfolios.xlsx`
- The Excel file should have columns: `TechStack` and `Links`
- This will be used if no CSV is uploaded

## Usage

### Streamlit Web App

Run the interactive web application:

```bash
streamlit run app/main.py
```

**Using the App:**

1. Open your browser to `http://localhost:8501`
2. **Configure in Sidebar:**
   - Enter your name
   - Enter your designation (e.g., "Sales Executive", "Business Development Manager")
   - Enter your company name
   - Provide company description/about (highlight services, expertise, values)
   - Upload your portfolio CSV file or use the default portfolio
3. **Generate Email:**
   - Paste a job posting URL
   - Click "Generate Email"
   - Review the personalized cold email
   - Copy and customize as needed before sending

**Features:**

- ✅ Dynamic company and employee information
- ✅ CSV portfolio upload for easy portfolio management
- ✅ Automatic skill-based portfolio matching
- ✅ Personalized email generation with company context
- ✅ Multiple email generation from job postings with multiple roles

### Jupyter Notebook

For exploration and experimentation:

```bash
jupyter notebook email-generator.ipynb
```

The notebook provides a step-by-step workflow:

1. Load and configure LLM
2. Extract job details from URL
3. Query portfolio database
4. Generate personalized email

## Project Structure

```
cold-email-generator/
├── app/
│   ├── main.py              # Streamlit application entry point
│   ├── chains.py            # LangChain pipeline for job extraction & email generation
│   ├── portfolio.py         # Portfolio database management
│   ├── utils.py             # Utility functions (text cleaning)
│   └── resources/
│       └── portfolios.xlsx  # Portfolio data (user-provided)
├── .streamlit/
│   ├── secrets.toml.example # Template for local secrets (copy to secrets.toml)
│   └── config.toml          # Streamlit configuration
├── email-generator.ipynb    # Jupyter notebook for exploration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (local only, not in repo)
└── README.md               # This file
```

## How It Works

### Workflow

1. **Configuration**: User provides personal and company information:
   - Employee name, designation
   - Company name, description/about
   - Portfolio data (CSV upload or default file)

2. **URL Input**: User provides a job posting URL

3. **Web Scraping**: WebBaseLoader extracts the job posting content

4. **Text Cleaning**: Raw HTML is cleaned and processed

5. **Job Extraction**: LLM analyzes content and extracts structured job details:
   - Role/Position
   - Required experience
   - Key skills
   - Job description

6. **Portfolio Matching**: Skills from the job posting are matched against portfolio using vector similarity (ChromaDB)

7. **Email Composition**: LLM generates a personalized cold email incorporating:
   - Employee name and designation
   - Company name and description
   - Job requirements analysis
   - Relevant portfolio links (automatically matched)
   - Professional call to action
   - Personalized sign-off

8. **Display & Copy**: Generated email is displayed in the UI, ready to copy and send

### Example Workflow

```
Input: URL → https://careers.company.com/job/senior-engineer
          Employee: John Doe
          Designation: Sales Executive
          Company: TechCorp Solutions
          Portfolio: React, Node.js, AWS projects
  ↓
Extract: Role: "Senior Software Engineer"
         Skills: ["React", "Node.js", "AWS"]
         Experience: "5+ years"
  ↓
Match Portfolio: [React-NodeJS project, AWS infrastructure project]
  ↓
Generate Email: "Hi [Hiring Manager],
                 I noticed you're looking for a Senior Software Engineer...
                 At TechCorp Solutions, we specialize in...
                 We've successfully delivered [portfolio examples]...
                 John Doe
                 Sales Executive"
```

## API Keys & Secrets

Get your Groq API key:

1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Create an API key
4. For **local development**: Add it to `.streamlit/secrets.toml` or `.env`
5. For **Streamlit Cloud**: Add it via the Secrets tab in your app's settings dashboard

## Secret Management

### Local Development

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"
```

### Streamlit Cloud

Add via dashboard **Secrets** tab:

```toml
GROQ_API_KEY = "your_actual_api_key"
```

**Important**: Never commit secrets to GitHub - they're in `.gitignore` ✅

## Example Workflow

```
Input: https://careers.nike.com/.../job/R-83565
  ↓
Extract: {
  "role": "Senior Information Security Engineer",
  "skills": ["security", "cloud", "infrastructure"],
  "experience": "5+ years"
}
  ↓
Match Portfolio: [project1_link, project2_link]
  ↓
Generate Email: "Hi hiring manager, I noticed you're looking for..."
```

## Requirements

See `requirements.txt` for all dependencies:

- langchain-groq
- langchain-core
- langchain-community
- python-dotenv
- pandas
- chromadb
- streamlit
- beautifulsoup4
- requests
- ipywidgets
- openpyxl

## Troubleshooting

**Email generation fails**: Check that Groq API key is valid and has sufficient credits

**Portfolio CSV not loading**: Ensure CSV has `TechStack` and `Links` columns (case-sensitive)

**Portfolio not matching skills**: Verify TechStack contains relevant keywords for the job skills

**Web page won't load**: Some websites may have JavaScript content or anti-scraping measures. Try a direct job post URL

**Missing dependencies**: Run `pip install -r requirements.txt` to install all required packages

## Features Implemented

✅ **Dynamic Company & Employee Configuration** - Customize sender details per campaign
✅ **CSV Portfolio Upload** - Upload your portfolio projects dynamically via web interface
✅ **Company Context in Emails** - Company description is incorporated into the cold email
✅ **Automatic Portfolio Matching** - Skills-based vector matching with ChromaDB
✅ **Personalized Emails** - Emails include sender name, designation, and company info
✅ **Error Handling** - Comprehensive validation and error messages
✅ **Streamlit Secrets Integration** - Secure API key management

## Future Enhancements

- [ ] Email template selection (formal, casual, technical, etc.)
- [ ] Multi-language email generation
- [ ] A/B testing email variants with analytics
- [ ] Batch processing multiple job URLs
- [ ] Email sending integration (SMTP/Gmail API)
- [ ] Response tracking and analytics dashboard
- [ ] Database storage of generated emails and responses
- [ ] Email personalization with additional fields (recruiter name, company size, etc.)
- [ ] Integration with LinkedIn and other job boards
- [ ] Prompt customization interface
- [ ] Follow-up email sequences

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests

## License

MIT License - Feel free to use this project for personal or commercial purposes.

## Support

For questions or issues, please open an issue on GitHub.

---

**Built with ❤️ using LangChain and Groq**
