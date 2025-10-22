from flask import Flask, jsonify, request
from models import db, Room # asking the models to have access to db and Room class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rooms.db' #database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return "Welcome to the Room Management System"

@app.route("/rooms", methods = ['GET'])
def get_rooms(): #create a route to get all rooms
    rooms = Room.query.all() #fetch all room records
    return jsonify([room.to.dict() for room in rooms]) # convert each room to dictionary and return as JSON



