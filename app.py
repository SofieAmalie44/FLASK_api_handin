# Working with API's

from flask import Flask, jsonify, request
from data_dict_simple import simple
from db import read, update_student, get_all_students, fetch_github_repos
import db 

app = Flask(__name__)



# routes, CRUD operations, GET, POST, PUT, PATCH. DELETE

@app.route('/students', methods=['GET'])  # GET (automaticly GET if no method is specified)
def read_all():
    return jsonify(read())



# exercises: get members by id
@app.route('/students/<int:id>', methods=['GET'])  # GET method (operator) 
def read_member(id):
    # 'simple' is a list of dictionaries, and each dictionary has an 'id' key
    student = next((item for item in read if item.get("id") == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404



# exercises: change students to member
@app.route('/members', methods=['POST'])  # POST method (operator) 
def create_member():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    # Append the new member to the simple list
    simple.append(data)
    
    return jsonify(simple), 201



# remove a member from the list using the id
@app.route('/members/<int:id>', methods=['DELETE'])  # DELETE method (operator) 
def delete_member(id):
    # 'simple' is a list of dictionaries, and each dictionary has an 'id' key
    member = next((item for item in simple if item.get("id") == id), None)
    if member:
        simple.remove(member)
        return jsonify({"message": f"Member with id: {id}, is successfully deleted"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404



# use PUT to change the value in an object
@app.route('/members/<int:id>', methods=['PUT'])  # PUT method (operator)
def update_member(id):
    # Find the member with the  ID
    member = next((item for item in simple if item.get("id") == id), None)

    if not member:
        return jsonify({"error": "Member not found"}), 404

    # Get the new data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update the member's data completely (PUT replaces the whole resource)
    member['id'] = data.get('id', member['id'])  # Replace if if provided, else keep the current one
    member['github_username'] = data.get('github_username', member['github_username'])  # Same for username

    return jsonify({"message": f"Member with id: {id} is successfully updated", "member": member}), 200


# use PATCH to change the value in an object
@app.route('/members/<int:id>', methods=['PATCH'])  # PATCH method (operator)
def change_member(id):
    # Find the member with the given ID
    member = next((item for item in simple if item.get("id") == id), None)

    if not member:
        return jsonify({"error": "Member not found"}), 404

    # Get the new data from the request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Update the member's data completely (PUT replaces the whole resource)
    member['id'] = data.get('id', member['id'])  # Replace if if provided, else keep the current one
    member['first_name'] = data.get('first_name', member['first_name'])  # Same for name

    return jsonify({"message": f"Member with id: {id} is successfully updated", "member": member}), 200


# Students db exercices

# PUT route to update a member's github_username
@app.route('/students/<int:id>', methods=['PUT'])  # PUT method for updating member
def update_students_route(id):
    # Get the new github_username from the request body
    data = request.get_json()
    
    # Handle error
    if not data or 'github_username' not in data:
        return jsonify({"error": "No github_username provided"}), 400
    
    github_username = data.get("github_username")

    # Call update_member to update the database
    result, status_code = update_student(id, github_username)
    

    return jsonify(result), status_code


# Route to get the list of public repositories for each student
@app.route('/students/repos', methods=['GET'])
def get_students_repos():
    students = db.get_all_students()
    
    students_with_repos = []
    
    for student in students:
        student_id, first_name, last_name, github_username = student

        if github_username:
            # Fetch the public repositories for students using GitHub username
            repos = fetch_github_repos(github_username)
        else:
            repos = []

        students_with_repos.append({
            "id": student_id,
            "name": f"{first_name} {last_name}",
            "github_username": github_username,
            "repositories": repos
        })
    
    return jsonify(students_with_repos)

if __name__ == '__main__':
    app.run(debug=True)
