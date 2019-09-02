from flask import Flask, render_template,request
app = Flask(__name__)



stories = [
    ['Hello ',"Greetings ","Hola ","Nice to finally you ", "Welcome "],
    ["What brings you here ", "We meet again ", ""]
    {"second":"","third":"","fourth":"","fifth":""},
    {"second":"","third":"","fourth":"","fifth":""},
    {"second":"","third":"","fourth":"","fifth":""},
    {"second":"","third":"","fourth":"","fifth":""},
    {"second":"","third":"","fourth":"","fifth":""}
]

user = {"name":"","gender":""}
verbs = []
nouns = []
adjectives = []
pronouns=[]

def storyScrambler(stories):
    stories
    return 


@app.route("/")
def index():
    """Return homepage."""
    return render_template('home.html', stories=stories, verbs=verbs, nouns=nouns, adjectives=adjectives,pronouns=pronouns)
@app.route('/',methods=['POST'])
def formHandler():
    print('hello')
    first = request.form['first']
    second = request.form['second']
    verbs.append(first)
    verbs.append(second)
    return render_template('base.html',verbs=verbs)
# @app.route("/playlists")
# def playlist():
#     """Return playlists"""
#     return render_template('playlists_index.html', playlists=playlists)
app.run(debug=True)

