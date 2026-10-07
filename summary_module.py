import ollama


def generate_summary(customer_email):
    prompt = f"""
Summarize the following customer email in exactly 50 words or fewer.

Customer Email:
{customer_email}

Focus only on the customer's main issue and request.
Return only the summary.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()