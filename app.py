from flask import Flask, render_template    
app = Flask(__name__)


playlists = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route("/")
def index():
    """Return homepage."""
    return render_template('home.html', playlists=playlists)
    
@app.route("/playlists")
def playlist():
    """Return playlists"""
    return render_template('playlists_index.html', playlists=playlists)
app.run(debug=True)

