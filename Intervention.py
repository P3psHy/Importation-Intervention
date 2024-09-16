from datetime import datetime



class Intervention:
    def __init__(self, codeIntervention=None, nom=None, prenom=None, numeroTelephone=None, dateRDV=None, commentaire=None, email=None, adresse=None, statut=None, dateCreation=None):
        self.codeIntervention = codeIntervention
        self.nom = nom
        self.prenom = prenom
        self.numeroTelephone = numeroTelephone
        self.dateRDV = dateRDV
        self.commentaire = commentaire
        self.adresse = adresse
        self.email = email
        self.statut = statut



    def affichage(self):
        print(f'Code d\'intervention: {self.codeIntervention},Nom: {self.nom}, Prénom: {self.prenom}, Numéro de téléphone: {self.numeroTelephone}, Date de RDV: {self.dateRDV}, Commentaire: {self.commentaire}, Adresse: {self.adresse}, Email: {self.email}, Statut: {self.statut}')

    
