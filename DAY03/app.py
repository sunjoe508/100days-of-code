from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    today = date.today().isoformat()

    if request.method == "POST":
        learned = request.form.get("learned", "").strip()
        built = request.form.get("built", "").strip()
        reflection = request.form.get("reflection", "").strip()

        if not learned or not built or not reflection:
            message = "❌ All fields are required."
        else:
            # Save log
            entry = f"""
Date: {today}
Learned: {learned}
Built: {built}
Reflection: {reflection}
-------------------------
"""
            with open("logs.txt", "a") as f:
                f.write(entry)

            # Save streak
            with open("streak.txt", "w") as f:
                f.write(today)

            message = "✅ Log saved successfully. Keep going!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()
