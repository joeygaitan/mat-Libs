from flask import Flask, render_template,request
import random
import os
app = Flask(__name__)



stories = [
    ['Hello ',"Greetings ","Hola "," Nice to finally meet you ", " Welcome "],
    ["What brings you here ", " We meet again ", " Nice to see you again "," What brings you here "," Its always a pleasure to see you "],
    [". I bet you don't ",". Would you know the ",". Somehow the ",". The grand scale of the ",". I was amazed by the "],
    [" of these "," of this "],
    [". Please ",". Somehow can you "," I wonder if you can "," Could you be a dear and "," I will have to "]
]

def storyScrambler(stories):
    newList = []
    for story in stories:
        if len(story) == 2:
            newList.append(story[random.randint(1,2)-1])
            continue
        listNumber = random.randint(1,5)
        newList.append(story[listNumber-1])
    return newList

newlist = storyScrambler(stories)


@app.route("/")
def index():
    """Return homepage."""
    return render_template('home.html')
@app.route('/',methods=['POST'])
def formHandler():
    print('hello')
    pro = request.form['pronoun']
    noun = request.form['noun']
    adjective = request.form['adjective']
    verb = request.form['verb']
    return render_template('base.html',newlist=newlist, pro=pro, noun=noun, adjective=adjective, verb=verb)
# @app.route("/playlists")
# def playlist():
#     """Return playlists"""
#     return render_template('playlists_index.html', playlists=playlists)
port = int(os.environ.get('PORT', 5000))
app.run(host='127.0.0.1', port=port, debug=True)

