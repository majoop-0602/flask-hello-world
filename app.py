from flask import Flask, render_template, request, jsonify, make_response, session
from flask_cors import CORS, cross_origin
app = Flask(__name__)

CORS(app)

@app.route('/pagos')
def pagos():
    import mysql.connector

    try:
        mydb = mysql.connector.connect(
            host="46.28.42.226",
            user="u760464709_24005242_usr",
            password="u7?Jpkt>Y*E7",
            database="u760464709_24005242_bd"
        )

        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM view_InfoPagos")
        myresult = mycursor.fetchall()

        return jsonify(myresult)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ob_idpedido')
def ob_idp():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005242_usr",
        password="u7?Jpkt>Y*E7",
        database="u760464709_24005242_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM view_obt_id_pedido")
    myresult2 = mycursor.fetchall()
    return make_response(jsonify(myresult2))

    mycursor.close()
    mydb.close()

@app.route('/agrega_pago', methods=['POST'])
def agrePagos():
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005242_usr",
        password="u7?Jpkt>Y*E7",
        database="u760464709_24005242_bd"
    )
    mycursor = mydb.cursor()

    valores = (
        request.form['txtid_pedido'],
        request.form['txtMonto'],
        request.form['cboEstadoPago'],
        request.form['txtReferenciaPaypal']
    )

    mycursor.execute("""
    CALL AgregarPagos(%s,%s,%s,%s,
    @NUEVOid_pago,
    @NUEVOid_pedido,
    @NUEVOmonto,
    @NUEVOestado_pago,
    @NUEVOreferencia_paypal)
    """, valores)

    mycursor.nextset()  

    mycursor.execute("""
    SELECT
    @NUEVOid_pago,
    @NUEVOid_pedido,
    @NUEVOmonto,
    @NUEVOestado_pago,
    @NUEVOreferencia_paypal
    """)

    resultado = mycursor.fetchone()
    mydb.commit()

    return jsonify({
        "@NUEVOid_pago": resultado[0],
        "@NUEVOid_pedido": resultado[1],
        "@NUEVOmonto": resultado[2],
        "@NUEVOestado_pago": resultado[3],
        "@NUEVOreferencia_paypal": resultado[4]
    })

    mycursor.close()
    mydb.close()
