from flask import Flask, render_template,request
import random
import os
app = Flask(__name__)



stories = [
    ['Hello ',"Greetings ","Hola "," Nice to finally meet you ", " Welcome "],
    [" What brings you here ", " We meet again ", " Nice to see you again "," What brings you here "," Its always a pleasure to see you "],
    [". I bet you don't ",". Would you know the ",". Somehow the ",". The grand scale of the ",". I was amazed by the "],
    [" of these "," of this "],
    [". Please finish the ",". Somehow can you complete the "," I wonder if you can destroy this"," Could you be a dear and end the "," I will have to wait and "],
    ['. If you do this for ', ". If this is done for ", ". If it is achieved by ", ". When it is completed by ", "They will ask when "]
]
#This function scrammbles the list of lists
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
    noun1 = request.form['noun1']
    pro1 = request.form['pro1']
    return render_template('base.html',newlist=newlist, pro=pro, noun=noun, adjective=adjective, verb=verb, noun1 = noun1, pro1=pro1)
if __name__ == '__main__':
    app.run(debug=True)

