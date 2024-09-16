import pandas as pd

import os
import shutil
import re

from datetime import datetime

from Intervention import Intervention
from DBConnection import get_database_connection

def get_list_file_from_directory_order_by_date()-> list:
    """
    Cette fonction récupère la liste des fichiers présent dans le dossier extractions_client en les triant par date

    :return: Liste des noms des fichiers
    """
    
    # Lis et récupère les noms des fichiers xlsx dans le dossier extractions_client
    files = os.listdir('extractions_client/')

    # Compile une recherche de date YYYY-MM-DD ou DDMMYYYY
    date_regex = re.compile(r'(\d{4}-\d{2}-\d{2})|(\d{2}\d{2}\d{4})')

    # Liste des fichiers contenant
    xlsx_files = [file for file in files if file.endswith('.xlsx') and date_regex.search(file)]

    # On trie l'ordre des fichiers en fonction de la date associé de la plus ancienne à la plus récente
    files_sorted = sorted(xlsx_files, key=get_date_to_extract)

    return files_sorted



def get_date_to_extract(fileName)-> datetime:
    """
    Cette fonction récupère une date dans le nom d'un fichier

    :param fileName: nom du fichier

    :return: Liste des noms des fichiers
    """

    # Recherche l'expression dans le nom du fichier
    match = re.search(r'(\d{4}-\d{2}-\d{2})|(\d{2}\d{2}\d{4})', fileName)
    if match:

        # Récupération de la chaine contenant la date
        date_str = match.group(0)

        # Si la date est au format 'YYYY-MM-DD', on la convertie
        if '-' in date_str:
            return datetime.strptime(date_str, '%Y-%m-%d')
        
        # Si la date est au format 'DDMMYYYY', on la convertie
        else:
            return datetime.strptime(date_str, '%d%m%Y')

    return None



def move_file_to_archive(filePath)-> None:
    """
    Cette fonction déplace les fichiers utilisés vers le dossier archive
    """

    shutil.move(f'extractions_client/{filePath}', f'extractions_client/archive/')
    # os.remove(filePath) Si il est préférable de supprimer le fichier (nom de la méthode à modifier dans ce cas là)




def load_interventions_from_xlsx(filePath)-> list:
    """
    Cette fonction déplace les fichiers utilisés vers le dossier archive

    :param filePath: chaîne de caractère contenant le nom du fichier à traiter

    :return: Liste d'objet Intervention contenant les valeurs du fichier excel

    """

    # lecture le fichier Excel
    df = pd.read_excel(filePath, engine='openpyxl')

    # Connexion à la base de donnée
    connection = get_database_connection()

    if connection:

        # Création de nos liste d'interventions
        newInterventions = []
        updatedIntervention = []

        #Lister toutes les lignes du fichier excel
        for _, item in df.iterrows():

            codeIntervention = int(item.get('Code intervention'))

            with connection.cursor() as cur:
                cur.execute("SELECT code_intervention FROM Interventions WHERE code_intervention = %s", (codeIntervention,))

                # Récupération des résultats
                rows = cur.fetchall()


                if not rows:

                    intervention = Intervention(
                        codeIntervention = codeIntervention,
                        nom = item.get('Nom'),
                        prenom = item.get('Prénom'),
                        numeroTelephone = item.get('Numéro de téléphone'),
                        dateRDV = item.get('Date rdv'),
                        commentaire = item.get('Commentaire'),
                        adresse = item.get('Adresse'),
                        email = item.get('email'),
                        statut = item.get('Statut'),
                    )

                    #Ajout de l'instance à la liste des interventions à ajouter
                    newInterventions.append(intervention)

                else:
                    intervention = Intervention(
                        codeIntervention = codeIntervention,
                        nom = item.get('Nom'),
                        prenom = item.get('Prénom'),
                        numeroTelephone = item.get('Numéro de téléphone'),
                        dateRDV = item.get('Date rdv'),
                        commentaire = item.get('Commentaire'),
                        adresse = item.get('Adresse'),
                        email = item.get('email'),
                        statut = item.get('Statut'),
                    )

                    #Ajout de l'instance à la liste des interventions à mettre à jour
                    updatedIntervention.append(intervention)
    else:
        print('Impossible de se connecter à la base de données')


    return newInterventions, updatedIntervention



def insert_interventions_to_database(interventions)-> None:
    """
    Cette fonction prépare les requètes SQL et les envoient à la base de donnée

    :param interventions: chaîne de caractère contenant le nom du fichier à traiter


    """

    # Récupération de l'instance de connexion
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cur:
                # Requête d'insertion SQL

                for item in interventions:

                    # Préparation de la requête
                    qb = """
                    INSERT INTO Interventions 
                    (code_intervention, nom, prenom, numero_telephone, date_rdv, commentaire, adresse, email, statut) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    # Exécution de la requête avec toutes les données
                    cur.execute(qb, (
                        item.codeIntervention,
                        item.nom,
                        item.prenom,
                        item.numeroTelephone,
                        item.dateRDV,
                        item.commentaire,
                        item.adresse,
                        item.email,
                        item.statut
                        )
                    )
                
                
                # Exécution des requêtes
                connection.commit()
                print('Les interventions ont été insérées avec succès')


        except Exception as e:
            print(f"Erreur lors de l'insertion : {e}")

             # Annuler si une erreur survient
            connection.rollback() 

        finally:
            # Fermer la connexion à la base de données
            connection.close()

    else:
        print('Impossible de se connecter à la base de données')
    

def update_interventions_database(interventions):

    # Récupération de l'instance de connexion
    connection = get_database_connection()

    if connection:
        try:
            with connection.cursor() as cur:
                # Requête d'insertion SQL

                for item in interventions:
                     
                    qb = """
                            UPDATE Interventions
                            SET nom = %s, prenom = %s, numero_telephone = %s, date_rdv = %s, commentaire = %s, adresse = %s, email = %s, statut = %s
                            WHERE code_intervention = %s
                        """
                    # Exécution de la requête avec toutes les données
                    cur.execute(qb, (
                        item.nom,
                        item.prenom,
                        item.numeroTelephone,
                        item.dateRDV,
                        item.commentaire,
                        item.adresse,
                        item.email,
                        item.statut,
                        item.codeIntervention 
                        )
                    )
                
                
                # Exécution des requêtes
                connection.commit()
                print('Les interventions ont été mise à jour avec succès')



        except Exception as e:
                    print(f"Erreur lors de l'insertion : {e}")

                    # Annuler si une erreur survient
                    connection.rollback() 

        finally:
            # Fermer la connexion à la base de données
            connection.close()

    else:
        print('Impossible de se connecter à la base de données')






