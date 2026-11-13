# 📖 Explorateur de catalogue — Poetry

Lister les livres correspondant à certains critères de sélection.

## Fonctionnalités

- Filtres dans la barre latérale : note minimale, fourchette de prix, recherche dans les titres
- 4 indicateurs recalculés sur la sélection : nombre de livres, prix moyen, note moyenne, prix le plus bas
- Palmarès : les 5 mieux notés et les 5 moins chers
- Message clair si aucun livre ne correspond aux filtres
- Données brutes consultables dans une section dépliable

## Lancer l'application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Données

19 livres de la catégorie Poetry, collectés sur [books.toscrape.com](https://books.toscrape.com) — fichier `data/livres_poetry.csv`.

## Stack

Python · pandas · Streamlit