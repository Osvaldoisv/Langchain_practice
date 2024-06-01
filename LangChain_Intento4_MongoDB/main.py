from pymongo import MongoClient
import datetime

try:
    client = MongoClient('localhost', 27017)

    database = client['LangChain_Intento4']

    collection = database['lenguajes']

    # collection.insert_one({"name":"Osvaldo", "email": "osvaldo@email.com", "phone": "12345678", "cita": "15 de mayo del 2024 a las 13 horas"})
    # collection.insert_one({"name":"Juan", "email": "juan@email.com", "phone": "21313678", "cita": "16 de mayo del 2024 a las 13 horas"})
    # collection.insert_one({"name":"Gian", "email": "gian@email.com", "phone": "3123131678", "cita": "17 de mayo del 2024 a las 13 horas"})


    user_email = 'osvaldo@email.com'

    # funcion1 buscar usuario
    documents = collection.find({'email': user_email})
    user_agenda = []
    for document in documents:
        user_agenda.append(document)
        # print(user_agenda)
        # estas son tus citas, deseas una cita nueva?


    # funcion2 agendar cita

    user_dia = "15"
    user_mes = "mayo"
    user_hora = "14"
  
    user_cita = user_dia + " de " + user_mes + " del 2024 a las " + user_hora + " horas"
    agenda_local = collection.find({'cita': user_cita})
    repetidas = []

    for agenda_citas in agenda_local:
        repetidas.append(agenda_citas)
    if len(repetidas)>0:
        print("agenda otra hora")
    else:
        print("añadir cita")
        
    
 


    agenda_general = collection.find()

    # for agendaciones in agenda_general:
    #     print(agendaciones)
        

except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    print("Conexión finalizada.")