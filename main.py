from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

POSTSURL = "https://api.npoint.io/f8f8e14db69b0d3f7e34"
EMAIL = ""
PASSWORD = ""
TOEMAIL = ""

response = requests.get(POSTSURL)
posts = response.json()
@app.route('/')
def index():
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=TOEMAIL,
                msg=f"Subject:Form message\n\n{name}\n\n{email}\n\n{phone}\n\n{message}"
            )
        return render_template("form-entry.html")
    return render_template("contact.html")

@app.route('/post/<postId>')
def post(postId):
    post = ''
    for p in posts:
        if int(p['id']) == int(postId):
            post = p
    return render_template("post.html", post=post)


if __name__ == '__main__':
    app.run(debug=True)
