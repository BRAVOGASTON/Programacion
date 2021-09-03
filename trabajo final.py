import requests as req  # importa la librería requests y se abrevia como req
import json

from requests.api import get

# chat id del telegram

def main():
     URL_API_TELEGRAM = "https://api.telegram.org" # url de telegram fija
     BOT = "1964840361:AAHKl32yIwl9l39t37LR2z7_knxUdybecWw" # bot creado para el fin
     ENDPOINT = "sendMessage" # 
     ID_CHAT = "-598679655"  # grupo o chat de telegram
     texto = "Mensaje de prueba " # texto a enviar
     URL_MENSAJE_TELEGRAM = f"{URL_API_TELEGRAM}/bot{BOT}/{ENDPOINT}?chat_id={ID_CHAT}&text={texto}" # url completa

     consulta = req.get (URL_MENSAJE_TELEGRAM) # recibe un parámetro donde indicamos la url, el get nos va a retornar la consulta
     if (consulta.status_code == 200): #el 200 es un estatus que devuelve el servidor que la petición es correcta
        print("Mensaje enviado de forma correcta") # imprime confirmación de envío
    
if (__name__ == "__main__"):  #condicional 
    main()



# stock en json

def cargar_datos (ruta):
    with open(ruta) as contenido:  #abre archivo, abierto el archivo abre el contenido
        stock = json.load(contenido)   #load de la librería json convierte el contenido a formato json
        for stock in stock:
            print(stock.get('id')) 

if (__name__ == "__main__"):  #condicional 
    ruta ='data/stock.json'
    cargar_datos(ruta)




# solicitud de usuario de artículo telegram

if 'bot' in text and 'id_10' in text True:
    bot.sendMessage(
        chat_id=chatId
        text=f'El articulo 10 está disponible '  #encontrar la forma de conectar la solicitud de información del listado JSON para obtener un TRUE O FALSE y dar el ok de si está disponible

elif 'bot' in text and 'id_10' in text False:
    bot.sendMessage(
        chat_id=chatId
        text=f'El articulo 10 no está disponible ' #encontrar la forma de conectar la solicitud de información del listado JSON para obtener un TRUE O FALSE y dar el ok de si está disponible
    )





