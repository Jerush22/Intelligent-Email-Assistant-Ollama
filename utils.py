from datetime import datetime


def save_reply(customer_email, generated_reply, intent):
    with open("outputs/generated_reply.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Intent: {intent}\n")
        file.write(f"Customer Email: {customer_email}\n")
        file.write(f"Generated Reply:\n{generated_reply}\n")
        file.write("=" * 60 + "\n")

    print("\nReply saved successfully!")