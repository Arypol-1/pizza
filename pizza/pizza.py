import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


DB = "pizza.db"

connect = sqlite3.connect(DB)

cursor = connect.cursor()

cursor.execute("SELECT * FROM Pizza")

result = cursor.fetchall()


@app.route("/")
def home():
    return render_template("home.html", pizzas=result)

@app.route('/pizza/<int:id>')
def single_pizza(id):
    connect = sqlite3.connect(DB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Pizza WHERE id=?", (id,))
    
    repizzasult = cursor.fetchone()
    return render_template("pizza.html", pizza=repizzasult)

@app.route('/about')
def about():
    return render_template('about.html')
    #create HTML for this 

@app.route('/pizzaas')
def pizzaas():
    connect = sqlite3.connect(DB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Pizza")
    piszzas = cursor.fetchall()
    return render_template('index.html',pizzas=piszzas)



    


if __name__ == "__main__":
    app.run(debug=True)
