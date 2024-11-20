from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'prithi'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'client_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    cur.close()
    if user:
        session['username'] = username
        return redirect(url_for('client'))
    return render_template('home.html', error="Invalid credentials!")

@app.route('/client')
def client():
    if 'username' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clients")
        clients = cur.fetchall()
        cur.close()
        return render_template('client.html', clients=clients)
    return redirect(url_for('home'))

@app.route('/add_client', methods=['POST'])
def add_client():
    name = request.form['name']
    email = request.form['email']
    company = request.form['company']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO clients (name, email, company) VALUES (%s, %s, %s)", (name, email, company))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('client'))

@app.route('/client/edit', methods=['POST'])
def edit_client():
    client_id = request.form['id']
    client_name = request.form['name']
    client_email = request.form['email']
    client_company = request.form['company']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE clients 
        SET name=%s, email=%s, company=%s 
        WHERE id=%s
    """, (client_name, client_email, client_company, client_id))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('client'))

@app.route('/delete_client/<int:id>')
def delete_client(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM clients WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('client'))

if __name__ == '__main__':
    app.run(debug=True)
