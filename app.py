from flask import Flask,jsonify,request
from datetime import datetime
import uuid
import re
from usuarios import usuarios
# Crea la Aplicación
app = Flask(__name__)

emails = []
# Chequea validez del mail
def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex,email)):
        print("200 OK - Email válido")
        return True
    else:
        print("400 Bad Request - Email inválido")
        return False
#Chequea el formato de la fecha
def check_fecha(fecha):
    formato = "%Y-%m-%d"
    try:
        if datetime.strptime(fecha,formato):
            print("200 OK")
            return True
        raise ValueError
    except ValueError:
        return False

def fecha_a_tipo(fecha):
    str_fecha = fecha
    nueva_fecha_tipo = datetime.strptime(fecha, "%Y-%m-%d").date()

    return nueva_fecha_tipo

# RUTAS GET, POST, PUT y DELETE
@app.route("/usuarios")
def obtener_usuarios():
    print("200 OK")
    return jsonify({"message": "200 OK" , "Usuarios": usuarios})

@app.route("/usuarios/<uuid:usuario_id>")
def obtener_usuario(usuario_id):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["id"]== usuario_id]
    if len(usuario_encontrado)>0:
        print("200 OK")
        return jsonify({"message": "200 OK" , "usuario": usuario_encontrado[0]})
    print("404 Resource Not Found")
    return jsonify({"message": "404 Resource Not Found - Usuario no encontrado"})

@app.route("/usuarios", methods = ["POST"])
def new_usuario():
    nuevo_usuario = {
        "id": uuid.uuid4(),
        "nombre":request.json["nombre"],
        "apellido":request.json["apellido"] ,
        "email":request.json["email"] ,
        "fecha_nacim": request.json["fecha_nacim"]
    }

    if check_fecha(nuevo_usuario["fecha_nacim"]):
        True
    else:
        print("400 Bad Request")
        return jsonify({"message": "400 Bad Request - El formato de fecha es incorrecto, debe ser del tipo YYYY-MM-DD"})

    fechas = datetime.strptime(nuevo_usuario["fecha_nacim"], "%Y-%m-%d").date()
    nuevo_usuario["fecha_nacim"] = fechas

    if check_email(nuevo_usuario["email"]):
        True
    else:
        print("400 Bad Request")
        return jsonify({"message": "400 Bad Request - Email inválido, debe ser del tipo name@example.xxx"})
    if nuevo_usuario["email"] in emails:
        print("400 Bad Request")
        return jsonify({"message": "400 Bad Request - Ya existe un usuario con ese email"})
    else:
        True
    emails.append(nuevo_usuario["email"])
    usuarios.append(nuevo_usuario)
    print("200 OK")
    return jsonify({"message": "200 OK - Usuario añadido con éxito","usuarios":usuarios})

@app.route("/usuarios/<string:usuario_nombre>", methods =["PUT"])
def editar_usuario(usuario_nombre):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["nombre"] == usuario_nombre]
    if (len(usuario_encontrado)>0):
        if usuario_encontrado[0]["email"] in emails:
            email_anterior = usuario_encontrado[0]["email"]
            emails.remove(email_anterior)
        else:
            True
        usuario_encontrado[0]["nombre"] = request.json["nombre"]
        usuario_encontrado[0]["apellido"] = request.json["apellido"]
        usuario_encontrado[0]["fecha_nacim"] = request.json["fecha_nacim"]
        usuario_encontrado[0]["email"] = request.json["email"]

        if check_fecha(usuario_encontrado[0]["fecha_nacim"]):
            True
        else:
            print("400 Bad Request")
            return jsonify({"message": "400 Bad Request - El formato de fecha es incorrecto, debe ser del tipo YYYY-MM-DD"})

        fechas = datetime.strptime(usuario_encontrado[0]["fecha_nacim"], "%Y-%m-%d").date()
        usuario_encontrado[0]["fecha_nacim"] = fechas

        if check_email(usuario_encontrado[0]["email"]):
            True
        else:
            print("400 Bad Request")
            return jsonify({"message": "400 Bad Request - Email inválido, debe ser del tipo name@example.xxx"})
        if usuario_encontrado[0]["email"] in emails:
            print("400 Bad Request")
            return jsonify({"message": "404 Bad Request - Ya existe un usuario con ese email"})
        else:
            True
        emails.append(usuario_encontrado[0]["email"])

        print("200 OK")
        return jsonify({"message": "200 OK - Usuario actualizado con éxito","usuario modificado": usuario_encontrado[0], "usuarios": usuarios})
    print("404 Resourse Not Found")
    return jsonify({"message": "404 Resourse Not Found - Usuario no encontrado"})

@app.route("/usuarios/<uuid:usuario_id>", methods =["DELETE"])
def eliminar_usuario(usuario_id):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["id"] == usuario_id]
    if (len(usuario_encontrado) > 0):
        usuarios.remove(usuario_encontrado[0])
        print("200 OK")
        return jsonify({"message": "200 OK - Usuario Eliminado", "usuarios": usuarios})
    print("404 Resourse Not Found")
    return jsonify({"message": "404 Resourse Not Found - Usuario no encontrado"})


if __name__ == '__main__' :
    app.run(debug = True , port = 5000)

