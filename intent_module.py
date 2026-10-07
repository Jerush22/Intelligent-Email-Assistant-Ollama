import ollama


def detect_intent(email):
    email_lower = email.lower()

    # Check important keywords first
    if "refund" in email_lower or "money back" in email_lower:
        return "Refund Request"

    if "cancel" in email_lower or "cancellation" in email_lower:
        return "Order Cancellation"

    if "damaged" in email_lower or "defective" in email_lower or "wrong product" in email_lower:
        return "Product Complaint"

    if "not working" in email_lower or "technical" in email_lower:
        return "Technical Support"

    if "delayed" in email_lower or "not arrived" in email_lower or "delivery" in email_lower:
        return "Delivery Issue"

    # Use Ollama for general questions
    prompt = f"""
Classify this customer email into exactly ONE category:

Delivery Issue
Refund Request
Product Complaint
Technical Support
Order Cancellation
General Inquiry

Customer Email:
{email}

Return ONLY the category name.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    intent = response["message"]["content"].strip()

    categories = [
        "Delivery Issue",
        "Refund Request",
        "Product Complaint",
        "Technical Support",
        "Order Cancellation",
        "General Inquiry"
    ]

    for category in categories:
        if category.lower() in intent.lower():
            return category

    return "General Inquiry"