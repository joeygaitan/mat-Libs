from flask import Flask, render_template,request
app = Flask(__name__)


stories = [
    {"first":"Hello ","second":"","third":"","fourth":"","fifth":""},
    {"first":"Greetings ","second":"","third":"","fourth":"","fifth":""},
    {"first":"Hola ","second":"","third":"","fourth":"","fifth":""},
    {"first":"Welcome ","second":"","third":"","fourth":"","fifth":""},
    {"first":"","second":"","third":"","fourth":"","fifth":""}
]

user = {"name":"","gender":""}
verbs = []
nouns = []
adjectives = []
pronouns=[]


@app.route("/")
def index():
    """Return homepage."""
    return render_template('home.html', stories=stories, verbs=verbs, nouns=nouns, adjectives=adjectives,pronouns=pronouns)
@app.route('/',methods=['POST'])
def formHandler():
    print('hello')
    first = request.form['first']
    verbs.append(first)
    return render_template('base.html',first=first)
# @app.route("/playlists")
# def playlist():
#     """Return playlists"""
#     return render_template('playlists_index.html', playlists=playlists)
app.run(debug=True)

