from flask import Flask, render_template, url_for

app = Flask(__name__)

user = {
    'name': 'Taveesh Sharma',
    'shortname': 'Taveesh',
    'description': "Hi, my name is Taveesh Sharma.",
    "social": {
        'twitter': 'https://twitter.com/staveesh',
        'linkedin': 'https://www.linkedin.com/in/taveesh-sharma-9385a8197',
        'github': 'https://github.com/staveesh',
        'instagram': 'https://instagram.com/_taveesh',
        'facebook': 'https://www.facebook.com/taveeshsharma'
    },
    'quote': "I figured I should have a website, because that's what everybody was doing ;-) "
}


@app.route("/")
def home():
    return render_template('index.html', user=user)


@app.route("/about")
def about():
    return render_template('about.html', user=user)


@app.route("/blog")
def blog():
    return render_template('about.html', user=user)


@app.route("/contact")
def contact():
    return render_template('about.html', user=user)


@app.route("/cv")
def cv():
    return render_template("about.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
