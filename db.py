import sqlite3
import requests
from data_dict import random_users, create_random_user



def createTable():
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY , 
            first_name TEXT, 
            last_name TEXT,
            birth_date TEXT,
            email TEXT,
            phonenumber TEXT,
            address TEXT,
            nationality TEXT,
            active BOOLEAN,
            github_username TEXT
            )""")
       
    

    conn.executemany('''INSERT INTO students (
             first_name,
             last_name,
             birth_date,
             email,
             phonenumber,
             address,
             nationality,
             active,
             github_username
             ) VALUES (:first_name, :last_name, :birth_date, :email, :phonenumber, :address, :nationality, :active, :github_username)''', random_users)
    
    conn.commit()

    

def read():

    students = []
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM students')

        for i in cur.fetchall():
            students.append(i)

    return students

# Function to get all students from the database
def get_all_students():
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT id, first_name, last_name, github_username FROM students')
        students = cur.fetchall()  # Get all students
    return students

# Funcktion to update students github username
def update_student(id, github_username):
    students = []

    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
         # Update the github_username for the member with the given id
        cur.execute('UPDATE students SET github_username = ? WHERE id = ?', (github_username, id))
        conn.commit()

        if cur.rowcount > 0:
            return {"message": f"Student with id: {id} successfully updated"}, 200
        else:
            return {"error": "Student not found"}, 404

    return students

# Function to fetch public repositories of a GitHub user
def fetch_github_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    #headers = {
    #     "Authorization": "<token>"  # Add a token to iliminate rate limit and i can make as many requests as i would like
    #}
    response = requests.get(url) # add <headers=headers> if rate limit is reached

    if response.status_code == 200:
        repos_data = response.json()
        return [{"name": repo["name"], "url": repo["html_url"]} for repo in repos_data]
    elif response.status_code == 404:
        return {"error": "GitHub username not found"}
    else:
        return {"error": f"Failed to fetch repositories (Status Code: {response.status_code})"}



# Remember to remove this after running the db first time
#createTable()     