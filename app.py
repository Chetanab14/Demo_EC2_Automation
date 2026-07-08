from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Application 🚀</h1>
    <p>This is a basic Flask application hosted from GitHub.</p>
    """

@app.route("/about")
def about():
    return """
    <h2>About</h2>
    <p>This application is built using Python Flask.</p>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "message": "Application is running successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)