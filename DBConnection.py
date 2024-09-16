import psycopg

def get_database_connection()-> psycopg:
    """
    Cette fonction se connecte à la base de donnnées Intervention.

    :return: Instance de connexion à la base de données
    """

    try:
        # Connexion à la base de données
        print('Tentative de connexion')

        connection = psycopg.connect(
            dbname = "Intervention",
            user = "postgres",
            password = "root",
            host = "localhost",
            port = 5432
        )
        print('Connexion à la base de données réussie')
        return connection  # Retourner l'objet connexion pour réutilisation
    except psycopg.OperationalError as e:
        print(f'Erreur de connexion : {e}')
        return None



