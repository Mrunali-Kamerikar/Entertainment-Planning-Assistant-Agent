# app/prompts.py

def get_prompt(intent: str):

    prompts = {

        "recommendation": """
You are a professional Netflix-style movie recommendation system.

From the context below, choose ONE most relevant movie.

Respond strictly in this format:

Title: <Movie Name>
Genre: <Genre>
Why Watch: <Short Explanation>
Best For: <Audience Type>

Context:
{context}

Question:
{input}
""",

        "summary": """
Provide a concise and clean summary of ONLY the movie mentioned in the question.
Do not mention other titles.

Context:
{context}

Question:
{input}
""",

        "review": """
Write a short critical review of the mentioned movie.
Include strengths and emotional impact.
Give rating out of 5.

Context:
{context}

Question:
{input}
""",

        "reflection": """
Provide thoughtful reflection on themes and emotional depth.
Focus only on the movie mentioned.

Context:
{context}

Question:
{input}
""",

        "qna": """
Answer factually using only the context provided.

Context:
{context}

Question:
{input}
"""
    }

    return prompts[intent]
