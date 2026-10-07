from input_module import get_email_input
from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


def process_email():
    print("\n===== Customer Email Details =====")

    customer_name, subject, customer_email = get_email_input()

    print("\n===== Entered Email Details =====")
    print("Customer Name :", customer_name)
    print("Subject       :", subject)
    print("Customer Email:", customer_email)

    print("\nDetecting customer intent...")
    intent = detect_intent(customer_email)
    print("Detected Intent:", intent)

    print("\nSearching previous interactions...")
    previous_email, previous_reply = retrieve_similar_email(customer_email)

    print("\n===== Similar Previous Interaction =====")
    print("Previous Email :", previous_email)
    print("Previous Reply :", previous_reply)

    print("\nGenerating professional reply...")
    generated_reply = generate_reply(customer_email, previous_reply)

    print("\n===== AI Generated Reply =====")
    print(generated_reply)

    print("\n===== Tone Improver =====")
    print("1. Friendly")
    print("2. Formal")
    print("3. Empathetic")

    choice = input("Choose a tone (1-3): ")

    tone_options = {
        "1": "Friendly",
        "2": "Formal",
        "3": "Empathetic"
    }

    tone = tone_options.get(choice, "Formal")

    improved_reply = improve_tone(generated_reply, tone)

    print(f"\n===== {tone} Tone Reply =====")
    print(improved_reply)

    print("\nGenerating conversation summary...")
    summary = generate_summary(customer_email)

    print("\n===== Conversation Summary =====")
    print(summary)

    save_reply(customer_email, improved_reply, intent)

    print("\nEmail processing completed successfully!")


def main():
    while True:
        print("\n" + "=" * 60)
        print("        INTELLIGENT EMAIL ASSISTANT")
        print("=" * 60)
        print("1. Process Customer Email")
        print("2. Exit")

        choice = input("\nEnter your choice (1-2): ")

        if choice == "1":
            process_email()

        elif choice == "2":
            print("\nThank you for using Intelligent Email Assistant!")
            break

        else:
            print("\nInvalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()