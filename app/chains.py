import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
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

    def generate_email(self, job_description, links):
        email_prompt = PromptTemplate.from_template("""
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Delala, a business development executive at AIFirst - 
            a software development company. You are trying to reach out to potential 
            clients through cold emails. Your task is to write a cold email to the 
            potential client based on the job description provided above. The email 
            should be concise and should highlight how your company can help the 
            potential client with their needs. Also add the most relevant ones from 
            the following links to showcase AIFirst's portfolio: {link_list} The email 
            should also include a call to action for the potential client to schedule 
            a meeting with you. Do not provide a preamble.

            ### EMAIL (NO PREAMBLE):

        """)

        chain_email = email_prompt | self.llm

        res = chain_email.invoke(
            input={"job_description": job_description, "link_list": links}
        )
        return res.content


if __name__ == "__main__":
    model = ChatGroq(model="gpt-4o", temperature=0.7)
