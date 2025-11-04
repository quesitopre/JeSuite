from flask import Flask, jsonify, request
from models import db, Room # asking the models to have access to db and Room class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rooms.db' #database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable modification tracking for performance

db.init_app(app) #intialize the database w/ flask app

@app.route("/") #
def home():
    return "Welcome to the Room Management System" # when directed to http-> directly lead to this message

@app.route("/rooms", methods = ['GET']) # create a route to get all rooms
def get_rooms(): #create a route to get all rooms
    rooms = Room.query.all() #fetch all room records
    return jsonify([room.to_dict() for room in rooms]) # convert each room to dictionary and return as JSON

@app.route("/rooms", methods=['POST']) 
def create_room(): 
    data = request.get_json()

    new_room = Room( #
        room_number = data['room_number'], # 
        room_type = data['room_type'],
        price_per_night = data['price_per_night'],
    ) 
    db.session.add(new_room) 
    db.session.commit() #commit the new room to the database

    return jsonify(new_room.to_dict()),201 #if everything works return the new room with a 201 status code

if __name__ == "__main__": #add new room to session
    with app.app_context(): 
        db.create_all() #create the database tables
    app.run(debug=True)