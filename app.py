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
    
