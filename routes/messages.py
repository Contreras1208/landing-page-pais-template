from flask import Blueprint

messages= Blueprint("messages", __name__)

@messages.route("/messages")
def msj():
    return "ruta mensajes"