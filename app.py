from flask import Flask, render_template, request
from Utility import Postgres
import Queries

db_obj = Postgres.PostgresClass()
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "password not match"
        try:
            db_obj.db_connect()
            query1 = Queries.insert_user_register_info
            db_obj.cursor.execute(query1, (name, email, password))
            db_obj.commit_changes()
            db_obj.db_disconnect()
            return "Registration successful"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)