from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        env=os.getenv("ENVIRONMENT", "unknown"),
        version=os.getenv("VERSION", "0.0.0"),
        commit=os.getenv("COMMIT_SHA", "unknown"),
        strategy=os.getenv("STRATEGY", "none")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
