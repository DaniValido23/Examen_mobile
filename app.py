# app.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.get("/")
def hola():
    return "hola"

@app.get("/clientes")
def get_mysql_clientes():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        #port="3306",
        user="root",
        password="example",
        database="store"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'id': result[0], 'nombre': result[1], 'apellido': result[2],  'telefono': result[3],  'direccion': result[4],  'email': result[5],  'ciudad': result[6],  'estado': result[7],  'Codigo Postal': result[8]}
        registro_json.append(registro)
        registro = {}

    return jsonify(registro_json)


@app.get("/productos")
def get_mysql_productos():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        #port="3306",
        user="root",
        password="example",
        database="store"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM productos")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'producto_id': result[0], 'descripcion': result[1], 'cantidad_disponible': result[2],  'costo_unitario': result[3],  'precio_venta': result[4]}
        registro_json.append(registro)
        registro = {}

    return jsonify(registro_json)


@app.get("/facturas")
def get_mysql_facturas():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        #port="3306",
        user="root",
        password="example",
        database="store"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM factura")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'factura_id': result[0], 'producto_id': result[1], 'cantidad': result[2],  'subtotal': result[3],  'IVA': result[4],  'total': result[5],  'cliente_id': result[6],  'registro_id': result[7]}
        registro_json.append(registro)
        registro = {}

    return jsonify(registro_json)


@app.post("/mysql")
def post_mysql():
    if request.is_json:
        registro = request.get_json()
        sql = "insert into ejemplo1 values ('" + registro['cliente_id'] + "','" + registro['nombre'] + "'," + registro['apellido'] + registro['telefono'] + registro['email'] + registro['direccion'] + registro['ciudad'] + registro['estado'] + registro['codigo postal'] + ");"
        mydb = mysql.connector.connect(
            #host="mysql-db-1",
            host="db",
            #port="3306",
            user="root",
            password="example",
            database="store"
        )
        mycursor=mydb.cursor()
        mycursor.execute(sql)

        return sql