from flask import Flask, jsonify, render_template,redirect,request,session
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/cupcakes')
def get_cupcakes():
    """1- With SQL alchemy, get a list of all Cupcake instances (objects)
    2- Using a list comprehension: for every Cupcake instance (object), add a dict
    for that instance with all it's attribute information using method .serialize() 
    3- Use the jsonify() to return a json answer, where cupcakes = a list of cupcakes 
    with their attributes in a dic"""
    cupcakes = Cupcake.query.all()
    json_response = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes = json_response)



@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    json_response = cupcake.serialize()
    
    return jsonify(cupcake = json_response)




@app.route('/api/cupcakes', methods=['POST'])
def create_new_cupcake():
    """Get the json data sent by user. Make a new empty Cupcake instance, so that
    we can then use the create_cupcake method. Add and commit to db. 
    Respond to the user with the json of the newly created cupcake, along with 201 code"""
    cupcake_json = request.json
    
    new_cupcake = Cupcake()
    new_cupcake.create_cupcake(cupcake_json)

    db.session.add(new_cupcake)
    db.session.commit()

    resp = {'cupcake': new_cupcake.serialize()}

    return (resp, 201)



@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """1- Get the instance of Cupcake base off of ID
    2- get the json data on the updates to be applied
    3- call the Cupcake instance methode update_cupcake with updated json data
    4- commit changes, return the new cupcake as json"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    updated_cupcake_json = request.json
    cupcake.update_cupcake(updated_cupcake_json)
    
    db.session.add(cupcake)
    db.session.commit()
   
    return {'cupcake': cupcake.serialize()}



@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    c = cupcake.id
  
    db.session.delete(cupcake)
    db.session.commit()

    return {"message": "Deleted"}