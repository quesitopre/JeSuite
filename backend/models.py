from flask_sqlalchemy import SQLAlchemy #
db = SQLAlchemy() # 
 
class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True) #unique id only
    room_number = db.Column(db.String(3), unique=True, nullable=False) 
    room_type = db.Column(db.String(10), nullable=False) 
    price_per_night = db.Column(db.Float, nullable=False)   

    def to_dict(self):  
        return{
            'id': self.id,
            'room_number': self.room_number, 
            'type': self.room_type,
            'price': self.price_per_night
        }