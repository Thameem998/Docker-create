from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI()

@app.post("/user/")
def create_user(user: User):
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="userdb"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (user.name, user.email)
    mycursor.execute(sql, val)
    mydb.commit()
    return {'id': mycursor.lastrowid}

@app.get("/user/{user_id}")
def read_user(user_id: int):
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="userdb"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE id=%s"
    val = (user_id,)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()
    return {'id': user[0], 'name': user[1], 'email': user[2]}

@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="userdb"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    val = (user.name, user.email, user_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return {'id': user_id, 'name': user.name, 'email': user.email}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="userdb"
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    val = (user_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {'status': 'User deleted'}

