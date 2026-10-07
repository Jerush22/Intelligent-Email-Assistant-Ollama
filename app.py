from flask import Flask, render_template, request

from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        subject = request.form["subject"]
        customer_email = request.form["customer_email"]
        tone = request.form["tone"]

        intent = detect_intent(customer_email)

        previous_email, previous_reply = retrieve_similar_email(
            customer_email
        )

        generated_reply = generate_reply(
            customer_email,
            previous_reply
        )

        improved_reply = improve_tone(
            generated_reply,
            tone
        )

        summary = generate_summary(customer_email)

        save_reply(
            customer_email,
            improved_reply,
            intent
        )

        result = {
            "name": customer_name,
            "subject": subject,
            "email": customer_email,
            "intent": intent,
            "previous_email": previous_email,
            "previous_reply": previous_reply,
            "reply": improved_reply,
            "summary": summary,
            "tone": tone
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)