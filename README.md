📧 Détection de spam avec Scikit-learn
🚀 Présentation

Ce projet met en œuvre des modèles de Machine Learning supervisé pour classer automatiquement les messages en deux catégories : spam et non-spam.
L’objectif est de démontrer comment les techniques de traitement du langage naturel (NLP) et les algorithmes de classification peuvent être appliqués à un problème concret de filtrage d’emails.

🎯 Objectifs

Prétraiter les données textuelles (nettoyage, tokenisation, vectorisation).

Extraire des caractéristiques à l’aide de Bag of Words et TF-IDF.

Entraîner et comparer plusieurs modèles (Naïve Bayes, SVM, Logistic Regression, Random Forest, etc.).

Évaluer les performances avec des métriques adaptées (précision, rappel, f1-score, matrice de confusion).

⚙️ Fonctionnalités

Chargement d’un dataset de messages (spam/ham).

Prétraitement du texte (suppression des stopwords, normalisation).

Implémentation de plusieurs algorithmes de classification.

Comparaison des performances pour sélectionner le modèle le plus efficace.

Prédiction de nouveaux messages.

🛠️ Technologies utilisées

Python

scikit-learn (classification, métriques, pipelines)

Pandas & NumPy (manipulation de données)

NLTK / spaCy (prétraitement linguistique)

Matplotlib / Seaborn (visualisation des résultats)

🚀 Installation et exécution

Cloner le projet :

git clone https://github.com/ton-repo/spam-detection.git
cd spam-detection


Installer les dépendances :

pip install -r requirements.txt


Lancer le script principal :

python main.py

📌 Objectif pédagogique

Ce projet illustre les étapes d’un pipeline NLP + Machine Learning :

Nettoyage et transformation de données textuelles

Entraînement et évaluation de modèles de classification

Utilisation de métriques adaptées pour un problème déséquilibré comme le spam
