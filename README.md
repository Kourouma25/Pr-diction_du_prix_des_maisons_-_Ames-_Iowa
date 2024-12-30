# **Prédiction des Prix des Maisons à Ames, Iowa**

**Description du Projet**

Ce projet a pour objectif de développer un modèle de machine learning capable de prédire les prix des maisons dans la ville d'Ames, Iowa, à partir de différentes caractéristiques . Ce projet sera réalisé en équipe de trois personnes :

X (Data Scientist en formation)

Y (Consultant CRM)

Z (Développeur Web)


Dans le cadre de ce projet, nous aurons l'opportunité de bénéficier d'un échange de connaissances enrichissant et d'une collaboration étroite entre trois disciplines complémentaires. En tant que Data Scientist, X apportera son expertise en analyse de données et modélisation, tandis que Y, en tant que Consultant CRM, contribuera à la compréhension des besoins métier et à la gestion des relations avec les utilisateurs. Z, en tant que Développeur Web, facilitera l'intégration des solutions dans une interface utilisateur fonctionnelle. Cette synergie nous permettra de développer une solution performante, tout en favorisant le partage de compétences et l'amélioration continue au sein de l'équipe.

Nous allons réaliser toutes les étapes suivantes dans le cadre de ce projet :

# **Mission 1**



**Exploration des données et prétraitement**

* Exploration des données et prétraitement
Avant de commencer à entraîner le modèle, nous allons bien explorer les données. Cela inclut :

* Analyse des distributions des variables et identification des anomalies ou valeurs manquantes.
* Application d’une réduction de dimension si le nombre de variables est élevé.
* Division des données en ensembles de formation et de test, avec éventuellement un ensemble de validation pour l’évaluation pendant l’entraînement.


**Suivi des expérimentations avec MLFlow**
Nous utiliserons MLFlow pour :

* Suivre l’évolution de nos expérimentations en enregistrant les hyperparamètres et les performances des modèles (par exemple, RandomForest, XGBoost, etc.).
* Enregistrer les modèles performants dans un Model Registry, afin de garder une trace des versions au fur et à mesure de leur amélioration.


**Métriques de performance**
Nous nous concentrerons sur les métriques suivantes pour évaluer les modèles :

* RMSE (Root Mean Squared Error) : Mesure de l’erreur de prédiction.
* MAE (Mean Absolute Error) : Erreur absolue moyenne.
* R² (coefficient de détermination) : Indicateur de la qualité des prédictions.
* Nous utiliserons également des graphiques de résidus pour vérifier la qualité des prédictions et ajuster le modèle si nécessaire.

**MLOps et gestion du code**
Pour assurer la qualité et la reproductibilité de notre travail :

* Versionnement du code : Utilisation de Git pour suivre les changements, avec un hébergement sur GitHub.
* Tests unitaires et fonctionnels : Mise en place de tests pour valider chaque nouvelle fonctionnalité.
* Déploiement continu : Configuration de GitHub Actions pour automatiser les tests et le déploiement continu. Nous prévoyons de déployer le modèle sur des plateformes cloud gratuit.

**Déploiement de l’API**
Une fois le modèle validé, nous le déploierons sous forme d’API REST :

* Utilisation de frameworks comme Flask ou FastAPI pour exposer le modèle en ligne.
* Tests de l’API via une interface Streamlit, qui permettra aux utilisateurs d’envoyer des données (caractéristiques de maison) et d’obtenir des prédictions sur les prix.

# **Mission 2**
**Réalisation d’un dashboard interactif:**


Une fois la Mission 1 terminée avec succès, nous passerons à la Mission 2 du projet : la création d’un dashboard interactif. Ce dashboard sera conçu pour permettre aux utilisateurs, comme les agents immobiliers ou les gestionnaires de biens, de visualiser facilement les prédictions de prix pour chaque maison, ainsi que les facteurs influençant ces prédictions. Il offrira également la possibilité de comparer les caractéristiques d’une maison spécifique avec l’ensemble du marché ou avec un groupe de propriétés similaires. Nous veillerons également à ce que le dashboard soit intuitif, accessible à tous, et déployé sur une plateforme cloud pour être utilisé en temps réel par les professionnels de l’immobilier. Cette étape sera essentielle pour transformer notre modèle en un outil concret et pratique pour la prise de décisions dans le secteur immobilier.

# **Description des des fichiers essentiels**
* **modelisation.ipynb** contient l’analyse exploratoire des données, la modélisation avec divers algorithmes de machine learning pour prédire les prix des maisons, et le suivi des expérimentations avec MLflow. Il inclut aussi une évaluation détaillée des performances du modèle final à l’aide de métriques comme le RMSE, MAE et R². Ce notebook est essentiel pour garantir un modèle précis et robuste.
* **main.py** est un fichier de construction de l'API 
* **test.csv/train.csv** Le fichier train.csv contient les données d'entraînement, incluant les caractéristiques des maisons ainsi que la cible, SalePrice, qui représente le prix de vente des maisons. Le fichier test.csv, quant à lui, contient uniquement les caractéristiques des maisons sans la cible, et sert à tester les modèles entraînés en soumettant les prédictions sur Kaggle (dont c'est pas l'objectif).
* **test_unitaire_API** est un fichier de test de notre API avec la commande terminal,  pytest test_unitaire_API
* **streamlit_app.py** est un fichier de réalisation du dashboard avec les fonctionnalités que l'on souhaite mettre en place pour répondre aux utilisateurs. Ce fichier permet de créer une interface interactive avec Streamlit, où les utilisateurs peuvent soumettre des données et obtenir des prédictions du modèle de machine learning, tout en visualisant des informations supplémentaires ou des graphiques associés.
* **requirements.txt** est utilisé pour spécifier les dépendances nécessaires pour faire fonctionner l'application.
* **batiment_a_predire**  est un fichier CSV contenant les caractéristiques de bâtiments, utilisé pour tester les prédictions du modèle
* **test_requette_API.py** est un fichier de test qui permet de tester localement notre API en envoyant des requêtes pour prédire le prix d'une maison. 
