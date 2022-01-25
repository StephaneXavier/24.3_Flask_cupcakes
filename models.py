from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):

    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default ='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        """For the specific instance of Cupcake, return a dictionary of it's the instance's attributes"""
        return {
            'id':self.id,
            'flavor': self.flavor,
            'size':self.size,
            'rating':self.rating,
            'image':self.image
        }
    
    def create_cupcake(self, cupcake_json):
        """When called on a new empty (of attributes) instance
        of Cupcake, method will take the json data (cupcake_json) sent by the 
        API user and set all the attributes of the new instance of Cupcake to cupcake_json"""
        self.flavor = cupcake_json['flavor']
        self.size = cupcake_json['size']
        self.rating = cupcake_json['rating']
        self.image = cupcake_json['image'] or None

    def update_cupcake(self, updated_cupcake_json):
        """Take json from a patch request with updates from a user, then set the attributes
        of this instance of Cupcake to the new json data if it exists, if not keep to what it was
        before"""
        self.flavor = updated_cupcake_json.get('flavor',self.flavor)
        self.size = updated_cupcake_json.get('size', self.size)
        self.rating = updated_cupcake_json.get('rating', self.rating)
        self.image = updated_cupcake_json.get('image', self.image)