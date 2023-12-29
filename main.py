from flask import Flask, render_template
import requests

app = Flask(__name__)

POSTSURL = "https://api.npoint.io/f8f8e14db69b0d3f7e34"

response = requests.get(POSTSURL)
posts = response.json()
@app.route('/')
def index():
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
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
