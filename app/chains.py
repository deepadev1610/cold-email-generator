import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        # Try to get API key from Streamlit secrets first, then fall back to environment variables
        try:
            groq_api_key = st.secrets.get("GROQ_API_KEY")
        except FileNotFoundError:
            groq_api_key = None

        groq_api_key = groq_api_key or os.getenv("GROQ_API_KEY")

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=groq_api_key,
        )

    def extract_jobs(self, cleaned_job_description):
        prompt = PromptTemplate.from_template("""
            ###SCRAPED TEXT FROM WEBISTE:
            {page_data}
            INSTRUCTION:
            The scaped text is from the careers page of a website.
            Your job is to extract the job details and return it is JSON format with the following keys:
            - role
            - experience
            - skills
            - description
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
        """)

        chain_extract = prompt | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_job_description})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content is too big. Unable to parse jobs")

        return res if isinstance(res, list) else [res]

    def generate_email(
        self,
        job_description,
        links,
        employee_name,
        designation,
        company_name,
        company_description,
    ):
        email_prompt = PromptTemplate.from_template("""
            ### COMPANY DESCRIPTION:
            {company_description}

            ### EMPLOYEE DETAILS:
            Name: {employee_name}
            Designation: {designation}
            Company: {company_name}

            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are {employee_name}, a {designation} at {company_name}. You are trying to reach out to potential 
            clients through cold emails. Your task is to write a cold email to the 
            potential client based on the job description provided above. The email 
            should be concise and should highlight how your company can help the 
            potential client with their needs. Use the company description to tailor your message.
            Also add the most relevant ones from the following links to showcase your portfolio: {link_list}
            The email should also include a call to action for the potential client to schedule 
            a meeting with you. Do not provide a preamble. Maintain proper email formatting and structure. Make sure the email is professional and engaging.
            End the email with a personalized closing line (not generic like "Best regards" or "Sincerely") 
            that is relevant to the potential client and the job description.

            The signature must follow this exact format on separate lines:
            <closing line>,
            {employee_name}
            {designation}
            {company_name}

            ### EMAIL (NO PREAMBLE):
        """)

        chain_email = email_prompt | self.llm

        res = chain_email.invoke(
            input={
                "job_description": job_description,
                "link_list": links,
                "employee_name": employee_name,
                "designation": designation,
                "company_name": company_name,
                "company_description": company_description,
            }
        )
        return res.content


if __name__ == "__main__":
    model = ChatGroq(model="gpt-4o", temperature=0.7)
