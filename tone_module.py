import ollama


def improve_tone(reply, tone):
    prompt = f"""
Rewrite the following customer support email in a {tone} tone.

Original Reply:
{reply}

Keep the meaning the same.
Make it clear, professional, and suitable for a customer.

Return only the rewritten email.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()