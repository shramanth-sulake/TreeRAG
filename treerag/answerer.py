import os

# Optional LLM (only if available)
USE_LLM = False

try:
    from dotenv import load_dotenv
    from openai import OpenAI

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if os.getenv("OPENAI_API_KEY"):
        USE_LLM = True

except:
    USE_LLM = False


def generate_answer(question, nodes):
    combined_content = "\n".join([node.content.strip() for node in nodes])

    # ✅ LLM version
    if USE_LLM:
        prompt = f"""
You are answering a question based on document sections.

Question:
{question}

Content:
{combined_content}

Write a clear, concise answer.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()

    # ✅ Fallback version (no LLM)
    return simple_summarize(combined_content)


def simple_summarize(text):
    """
    Basic fallback summarization
    """
    lines = text.split("\n")

    # remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # join into paragraph
    return " ".join(lines)