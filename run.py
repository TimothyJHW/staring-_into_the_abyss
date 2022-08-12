
# "flask" is capitalised "Flask" beacaus it is a class.
import os
import json
# request library handles form objects, flash handles 'flashed' messages.Flashed messages only stay on screen until the browser is refreshed or you move away. To use flashed messages you need an encrypted key.

from flask import Flask, render_template, request, flash
# imports env only if the file actually exists.
if os.path.exists("env.py"):
    import env


# name of the application's module. Built in Python variable.

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# Python decorator: a decorator is a way of wrapping functions
# the function under the decorator is bound to the decorator
@app.route("/")
def index():
    # return "<h1>Hello</h1> <h2>World!</h2>"
    return render_template("index.html")


@app.route("/about")
def about():
    data =[]
    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
    #page_title is a user defined variable, there can be other args as well. It is passed into the template and can be accessed by double curly brackets.
    return render_template("about.html", page_title = "About",articles = data)

@app.route("/about/<article_name>")
def article_contents(article_name):
    content = {}
    with open("data/articles.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == article_name.replace(" ","-").lower():
                content = obj
    return render_template("article.html", article = content)

## allows the contact form to accept data. Second variable allows GET and POST from the page.
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # "print(request.form.get("name"))"
        # this gets the name field from the html form submission
        flash("Thanks {}, we have received your message".format(
            request.form.get("name")))
    return render_template("contact.html", page_title = "Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Careers")


# TO run locally open in localhost:5000
if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug = True
        #only have debug = True for development
    )

