import getpass
import os
#Langchain imports
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    #GET API key as OS environment so it's not created in plain text
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=1,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )    

if __name__== "__main__":
    main()