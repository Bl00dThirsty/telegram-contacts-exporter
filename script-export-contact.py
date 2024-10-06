# TelegramContactsExporter.

# Importation des modules nécessaires. / Importing necessary modules.
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
import csv

# Informations d'identification pour l'API Telegram. / Telegram API credentials.
api_id = 'enterYourApiId'
api_hash = 'enterYourApiHAsh'
phone_number = '+2376#########'

# Création d'une instance du client Telegram. / Creating a Telegram client instance.
client = TelegramClient('session_name', api_id, api_hash)

# Démarrage de la session client / Starting the client session.
client.start(phone=phone_number)

# Récupération de la liste des contacts. / Fetching the contacts list.
contacts = client(GetContactsRequest(hash=0)).users

# Ouverture du fichier CSV en mode écriture. / Opening CSV file in write mode.
with open('skpContacts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Écriture de l'en-tête du fichier CSV. / Writing CSV file header.
    writer.writerow(['Name', 'Phone'])  
    
    # Parcours de chaque contact et écriture dans le fichier CSV.
    # Looping through each contact and writing to CSV file.
    for contact in contacts:
        name = (contact.first_name or '') + (f" {contact.last_name}" if contact.last_name else '')
        phone = contact.phone if contact.phone else 'N/A'  
        writer.writerow([name, phone])

# Affichage du message de confirmation. / Displaying confirmation message.
print("Contacts exported successfully from Telegram to skpContacts.csv")

# Fermeture de la connexion au client Telegram. / Closing Telegram client connection.
client.disconnect()