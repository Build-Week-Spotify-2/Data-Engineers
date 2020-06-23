from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk
from dotenv import load_dotenv
import os

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# initialize Spotify cursor
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
cred = tk.Credentials(CLIENT_ID,CLIENT_SECRET)
access_token = cred.request_client_token()
spotify = tk.Spotify(access_token)

@app.route('/')
def root():
    return "You don't want to look at this page"

@app.route('/request')
def request():
    tracks, = spotify.search('5 best songs',types=('track',), limit=5)
    result = ''
    for track in tracks.items:
        result = result + track.name + '\n'#' by ' + track.artists.name + 
    return result

if __name__=='__main__':
    app.run(debug=True)