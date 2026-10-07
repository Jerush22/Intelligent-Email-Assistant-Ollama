import csv
from difflib import SequenceMatcher


def retrieve_similar_email(current_email):
    with open("data/emails.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        best_email = ""
        best_reply = ""
        best_score = 0

        for row in reader:
            score = SequenceMatcher(
                None,
                current_email.lower(),
                row["Email"].lower()
            ).ratio()

            if score > best_score:
                best_score = score
                best_email = row["Email"]
                best_reply = row["Reply"]

    return best_email, best_reply