from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import tekore as tk

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

@app.route('/root')
def root():
    #import Spotify API
    #api = SPOTIFY.TODO()
    #first,second = SPOTIFY.TODO()
    #return either first or second
    pass

@app.route('/index')
def index():
    #import Spotify API
    #api = SPOTIFY.TODO()
    #first, second = api.measurements(one_attribute= ?, second_attribute= ?)
    #return first or second
    pass

@app.route('/refresh')
def refresh():
    #import SPOTIFY API
    #api = SPOTIFY.TODO()
    DB.drop_all()
    DB.create_all()
    return 'Data refreshed!'

if __name__=='__main__':
    app.run(debug=True)