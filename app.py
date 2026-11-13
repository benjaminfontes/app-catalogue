import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogue", page_icon="📖", layout="wide")

FICHIER = "data/livres_poetry.csv"

@st.cache_data
def charger_donnees(chemin):
    return pd.read_csv(chemin)

df = charger_donnees(FICHIER)

st.title("Catalogue de livres : l'explorateur")             # Titre
st.caption("source : books.toscrape.com")               # Légende sous le titre

with st.sidebar:                            # Barre latérale
    st.header("Filtres")
    note_mini = st.slider("Note minimale", 1, 5, 1)                                 # Curseur avec note minimale
    prix_min, prix_max = st.slider("Fourchette de prix", 0.0, 60.0, (10.0, 50.0))   # Fourchette de prix avec curseur à deux poignées
    recherche = st.text_input("Le titre contient")                                  # Recherche dans les titres

st.subheader("Livres sélectionnés")                                                     # Tableau listant les livres correspondant

selection = df.copy()                                                                   # Création d'une copie du fichier source

selection = selection[selection["note"] >= note_mini]                                   # Filtre 1

selection = selection[selection["prix_gbp"] <= prix_max]                                # Filtre 2

selection = selection[selection["prix_gbp"] >= prix_min]                                # Filtre 3
if recherche:
    selection = selection[selection["titre"].str.contains(recherche, case=False)]

st.write("Livres retenus :", len(selection), "sur", len(df))
st.dataframe(selection)

if len(selection) == 0:                                                                     # Message si aucun livre ne s'affiche
    st.warning("Aucun livre ne correspond a ces criteres.")
else:
    gauche, milieu_gauche, milieu_droite, droite = st.columns(4)                            # 4 colonnes pour 4 KPIs

    gauche.metric("Nombre de livres retenus", len(selection))                               # KPI 1

    milieu_gauche.metric("Prix moyen", f"{selection['prix_gbp'].mean():.2f} GBP")           # KPI 2

    milieu_droite.metric("Note moyenne", f"{selection['note'].mean():.2f} / 5")             # KPI 3

    droite.metric("Le moins cher", f"{selection['prix_gbp'].min():.2f} GBP")                # KPI 4

a, b = st.columns(2)
with a:                                                                                     # Tableau affichage des 5 mieux notés
    st.subheader("Les 5 mieux notés")
    st.dataframe(selection.nlargest(5, "note")[["titre", "note", "prix_gbp", "stock"]]) 

with b:                                                                                     # Tableau affichage des 5 - chers 
    st.subheader("Les 5 moins chers")
    st.dataframe(selection.nsmallest(5, "prix_gbp")[["titre", "prix_gbp"]]) 
   

with st.expander("Voir les donnees brutes"):                                                # Affichage des données brutes
    st.dataframe(df)