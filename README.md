# Importation interventions

#- Projet sous Python & PostgreSQl-#

- Outils nécessaire -
Voici les outils dont vous avez besoin pour lancer le script
    - python avec ces libraries d'installés:
        - psycopg, pour les intéractions avec la base de données: 
            pip install psycopg
        - pandas, pour la lecture et manipulation de fichiers xlsx:
            pip install pandas
    - PostgreSQL avec une base de donnée appelé: Intervention (Modifier l'identifiant et mot de passe utilisateur si nécessaire dans DBConnection.py)

- Composition du Projet -
Voici les différents fichiers & dossiers du projet:
    - Dossier extractions_client: contient les fichiers xlsx et le dossier archive
      - Dossier archive: contiendra les fichiers xlsx qui seront utilisé après exécution
    - consignes.txt: consigne du projet
    - DBConnection.py: contient la connection à la base de données
    - Intervention.py: contien la classe intervention.py pour manipuler les données
    - main.py: contient le script d'exécution
    - rdv_table contient la requête SQl de création de la table interventions
    - utils.py: contient les fonctions utilisées par le script principal



- Lancer le script -

Procédure à suivre pour lancer le scirpt python:

Créer la table intervention à partir de la requête SQL présente dans le fichier rdv_table:

Dès lors que la table est créé et que toutes les librairies python sont importé sur votre poste, exécutez la commande:
    - python main.py

Le programme principal s'exécutera et un historique des actions apparaîtra dans votre invite de commande.


Afin d'utiliser le script de manière automatique, voici deux possibilités en fonction de votre environnement:
    - Windows: utiliser un planificateur de tâches
    - Linux: utiliser crontab


Note: si vous voulez relancer le code, il est nécessaire de déplacer les fichiers xlsx qui sont dans le dossier archive vers le dossier extractions_client
