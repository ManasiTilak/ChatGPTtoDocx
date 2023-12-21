from openai import OpenAI
from dotenv import load_dotenv
import openai
import os
from docx import Document

def get_openai_response(client, model, question):
    """
    Function to get a response from the OpenAI API.
    """
    # print(model)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant and a coding expert. You are very good at writing coding blogs."},
            {"role": "user", "content": question}
        ],
        max_tokens=10,
    )
    return response.choices[0].message.content

def create_docx(content, filename):
    """
    Function to create a .docx file from the provided content.
    """
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)
    print(f"Response saved in '{filename}'")

def main():
    """
    Main function to orchestrate the OpenAI API call and document creation.
    """

    # Load environment variables
    load_dotenv()
    # Initialize the OpenAI client with API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # Specify model
    model="gpt-3.5-turbo"
    # Specify Question
    question="Capital of India?"
    # Specify Filename for output File
    filename="response.docx"
    try:
        response_content = get_openai_response(client,model,question)
        create_docx(response_content, filename)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
