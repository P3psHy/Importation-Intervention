CREATE TABLE Interventions (
    code_intervention INT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    numero_telephone TEXT,
    date_rdv DATE, 
    commentaire TEXT,
    adresse TEXT,
    email TEXT,
    statut TEXT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


