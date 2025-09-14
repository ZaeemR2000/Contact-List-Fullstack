#CRUD

#Create:
# - first name
# - last name
# - email

from flask import request, jsonify
from config import app, db
from models import Contact


@app.route('/contacts', methods = ['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contact = list(map(lambda x: x.to_json(), contacts))
    return jsonify({'contacts': json_contact})


@app.route('/create_contact', methods = ['POST'])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')
    
    if first_name and last_name and email:
        new_contact = Contact(first_name=first_name, last_name=last_name, email = email)
        try:
            db.session.add(new_contact)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 400
        
        return jsonify({'message': 'User Created!'}), 201
    
    return jsonify({'message': 'You must include a first name, last name and email'}), 400


@app.route('/update_contact/<int:user_id>', methods = ['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({'message': 'User not found'}), 400
    
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400
    
    return jsonify({'message': 'User has been updated!'}), 201


@app.route('/delete_contact/<int:user_id>', methods = ['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({'message': 'User not found'}), 400
    
    try:
        db.session.delete(contact)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

    return jsonify({'message': f'{contact.first_name} has been deleted!'}), 201
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=5001)