from flask import Flask, render_template, request, redirect, url_for, flash
from Utility import Postgres
import Queries

db_obj = Postgres.PostgresClass()
app = Flask(__name__)
app.secret_key = 'my_key'


@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        db_obj.db_connect()
        query = Queries.select_user_password
        db_obj.cursor.execute(query, (email,))
        result = db_obj.cursor.fetchone()
        db_obj.db_disconnect()

        if result == None:
            flash("Your not registerd.")
            return redirect(url_for("login"))
        else:
            user_password = result[0]
            if password != user_password:
                flash("Incorrect password")
            else:
                return render_template('Result.html')
    return render_template("login.html")

@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        db_obj.db_connect()
        query = Queries.select_user_email
        db_obj.cursor.execute(query, (email,))
        result = db_obj.cursor.fetchone()
        if result:
            flash("Email already exists.")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Password does not match with confirm password.")
            return redirect(url_for("register"))

        query1 = Queries.insert_user_register_info
        db_obj.cursor.execute(query1, (name, email, password))
        db_obj.commit_changes()
        db_obj.db_disconnect()
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route('/password', methods = ['GET','POST'])
def password():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Password does not match with confirm password.")
            return redirect(url_for("register"))

        db_obj.db_connect()
        query = Queries.update_user_password
        db_obj.cursor.execute(query, (password, name, email))
        db_obj.commit_changes()
        db_obj.db_disconnect()
        return redirect(url_for("login"))
    return render_template('password.html')

if __name__ == "__main__":
    app.run(debug=True)