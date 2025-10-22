@app.route("/rooms", methods=['POST']) 
def create_room(): 
    data = request.get_json()

new_room = Room(
        room_number = data['room_number'],
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
    