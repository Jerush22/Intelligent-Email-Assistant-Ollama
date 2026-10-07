import ollama


def generate_reply(customer_email, previous_reply):
    prompt = f"""
You are a professional customer support email assistant.

Generate a polite and professional reply to the customer's email.

Customer Email:
{customer_email}

Previous Similar Reply:
{previous_reply}

Use the previous reply as context, but create a suitable response
for the current customer email.

Reply format:
Dear Customer,

[Professional response]

Regards,
Support Team

Return only the email reply.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()