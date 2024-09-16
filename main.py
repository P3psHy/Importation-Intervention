#Importation des fonctions utilitaire
from utils import *


if __name__ == "__main__":
    print('\n--Début du script--')

    #Récupération des fichiers dans le dossier extractions_client
    files = get_list_file_from_directory_order_by_date()

    #Pour chaque fichier
    for filePath in files:
        print(f'\n-Lecture du fichier: {filePath}-')

        #créer deux liste contenant les nouvelles interventions et celles mise à jour
        newInterventions, updatedInterventions = load_interventions_from_xlsx(f'extractions_client/{filePath}')


        # #Envoyer les données vers la base de données

        if newInterventions:
            print(f'Importation de {len(newInterventions)} intervention(s) \n')
            insert_interventions_to_database(newInterventions)
        if updatedInterventions:
            print(f'Modification de {len(updatedInterventions)} intervention(s) \n')
            update_interventions_database(updatedInterventions)
        
        #Archiver les fichiers utilisés
        move_file_to_archive(filePath)

    print('\n--Fin du script--')
