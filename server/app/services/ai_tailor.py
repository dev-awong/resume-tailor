import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tailor_resume(resume_text: str, keywords: list[str]):
    prompt = f"""
    Improve the following resume bullets to match these keywords: {keywords}

    Resume:
    {resume_text}

    Return only improved bullet points.
    """
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]

