from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    message=""
    if request.method == "POST":
        message = request.form["message"]
        processed = message.lower()  # Optionally add full preprocessing here
        vec = vectorizer.transform([processed])
        pred = model.predict(vec)[0]
        prediction ="🚨 SPAM" if pred == "spam" else "✅ HAM (Not Spam)"
    return render_template("index.html", prediction=prediction, message=message)

if __name__ == "__main__":
    app.run(debug=True)

