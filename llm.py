import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_answer(context, question):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are an AI assistant.
    Answer only from the context below.

    Context:
    {context}

    Question:
    {question}

    If answer is not in context, say "Not found in document"
    """

    response = model.generate_content(prompt)
    return response.text