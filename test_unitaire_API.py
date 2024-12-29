import pandas as pd
import joblib

# Charger les données de test
data = pd.read_csv('batiment_a_predire.csv')
donne_predire = data.iloc[0: 1,:]  

# Charger le modèle
model_enregistre = joblib.load('Model_final.pkl')

def test_predire():
    # Utiliser la méthode predict pour obtenir les valeurs de régression
    prediction = model_enregistre.predict(donne_predire)

    assert prediction is not None, "La prédiction est nulle."

    # Afficher la prédiction
    print("Test passé avec succès. Valeur prédite :", prediction[0])

# Lance le test et vérifier la sortie
test_predire()
