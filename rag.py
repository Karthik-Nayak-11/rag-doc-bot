from openai import AzureOpenAI
from config import *

def generate_answer(question: str, docs: list):
    if not docs:
        return "No relevant information found in your documents."

    MAX_CHARS = 1500  # safe for S0 tier

    context = "\n\n".join(
        [
            f"Source: {d['source']}\n{d['content'][:MAX_CHARS]}"
            for d in docs
        ]
    )

    client = AzureOpenAI(
        azure_endpoint=OPENAI_ENDPOINT,
        api_key=OPENAI_KEY,
        api_version=OPENAI_VERSION
    )

    system_prompt = (
        "You are a helpful assistant.\n"
        "Answer ONLY using the provided context.\n"
        "If the answer is not present, say you do not know."
    )

    response = client.chat.completions.create(
        model=OPENAI_DEPLOYMENT,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content
