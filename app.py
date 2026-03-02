
from flask import Flask, render_template, request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/pagos')
def pagos():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005242_usr",
        password="u7?Jpkt>Y*E7",
        database="u760464709_24005242_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM pagos")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
