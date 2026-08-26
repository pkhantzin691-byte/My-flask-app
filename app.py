from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <div style="text-align:center; margin-top:50px;">
        <h2>Website Logo</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username or Email" required><br><br>
            <input type="password" name="password" placeholder="Password" required><br><br>
            <button type="submit">Log In</button>
        </form>
    </div>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    
