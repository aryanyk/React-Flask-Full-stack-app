from flask import Flask,jsonify,request
from config import app, db
from model import User

@app.route('/contacts',methods=['GET'])
def get_contacts():
    users = User.query.all()
    user_contacts = list(map(lambda user: user.to_json(), users))
    return jsonify({'contacts':user_contacts}) 

@app.route('/create_contacts',methods=['POST'])
def create_contact():
    first_name =request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')
    
    if not first_name or not last_name or not email:
        return (jsonify({'error':'Please provide all details'}),400)
    
    new_contact = User(first_name=first_name,last_name=last_name,email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e :
        return jsonify({'error':str(e)})
    
    return jsonify({'message':'Contact created successfully'}),201


@app.route('/update_contacts/<int:id>',methods=['PATCH'])
def update_contact(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error':'Contact not found'}),404
    
    
    first_name = request.json.get('firstName',user.first_name)
    last_name = request.json.get('lastName',user.last_name)
    email = request.json.get('email',user.email)

        
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'error':str(e)})
    
    return jsonify({'message':'Contact updated successfully'})

@app.route('/delete_contacts/<int:id>',methods=['DELETE'])
def delete_contact(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error':'Contact not found'}),404
    
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        return jsonify({'error':str(e)})
    
    return jsonify({'message':'Contact deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)