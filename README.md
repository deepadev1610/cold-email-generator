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

1. **Set up environment variables**:
   Create a `.env` file in the project root:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

2. **Prepare portfolio data**:
   - Place your portfolio file at `app/resources/portfolios.xlsx`
   - The Excel file should have columns: `TechStack` and `Links`
   - Example:
     | TechStack | Links |
     |-----------|-------|
     | React, Node.js, MongoDB | https://github.com/project1 |
     | Python, FastAPI, PostgreSQL | https://github.com/project2 |

## Usage

### Streamlit Web App

Run the interactive web application:

```bash
streamlit run app/main.py
```

Then:

1. Open your browser to `http://localhost:8501`
2. Paste a job posting URL
3. Click "Generate Email"
4. Copy the generated email and customize as needed

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
├── email-generator.ipynb    # Jupyter notebook for exploration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
└── README.md               # This file
```

## How It Works

1. **URL Input**: User provides a job posting URL
2. **Web Scraping**: WebBaseLoader extracts the job posting content
3. **Text Cleaning**: Raw HTML is cleaned and processed
4. **Job Extraction**: LLM analyzes content and extracts structured job details (JSON format)
5. **Portfolio Search**: Skills from job are matched against portfolio using vector similarity
6. **Email Composition**: LLM generates a personalized cold email incorporating:
   - Job requirements analysis
   - Relevant portfolio links
   - Call to action
7. **Display**: Email is shown in the UI ready for sending

## API Keys

Get your Groq API key:

1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Create an API key
4. Add it to your `.env` file

## Environment Variables

```
GROQ_API_KEY=your_api_key_here
```

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
- ipywidgets
- openpyxl

## Troubleshooting

**Email generation fails**: Check that Groq API key is valid and has sufficient credits

**Portfolio not matching**: Ensure Excel file path is correct and TechStack column contains relevant technologies

**Web page won't load**: Some websites may have JavaScript content that WebBaseLoader can't parse

## Future Enhancements

- [ ] Support for multiple portfolio formats (JSON, API)
- [ ] Email customization templates
- [ ] A/B testing email variants
- [ ] Batch processing multiple job URLs
- [ ] Email sending integration (SMTP)
- [ ] Analytics and response tracking

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
