import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import base64
from DataVisualization import DataVisualization
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import gaussian_kde
import numpy as np


    
# Configurer la page en premier
st.set_page_config(page_title="Climat App", page_icon="🌍", layout="wide")



# Loadin_dataset
data = pd.read_excel(r"data\soil_dz_allprops.xlsx")
data2 = pd.read_excel(r"data\soil_dz_allprops.xlsx")
print(len(data))

# Initialisation de l'état dans session_state
if 'choices_validated' not in st.session_state:
    st.session_state['choices_validated'] = False
if 'selected_data' not in st.session_state:
    st.session_state['selected_data'] = data

class ClimatApp:
    def __init__(self):
        self.selected_data = None
        self.selected_attributes = []
        self.plot_type = None
        self.preprocess_options = {}
        self.choices_validated = False
    
    def get_image_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    
    def show_welcome_image(self,placeholder):
    # Affiche l'image seulement si les choix n'ont pas encore été validés
        
        if not self.choices_validated:
            welcome_image_path = os.path.join("assets", "XfQ8.gif")
            if os.path.exists(welcome_image_path):
                placeholder.markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: center; padding-top: 100px;">
                        <img src="data:image/gif;base64,{self.get_image_base64(welcome_image_path)}" 
                            alt="Bienvenue ! Configurez vos paramètres pour commencer." width="300"/>
                        <p style="text-align: center; padding-top: 20px; font-size: 18px;">
                            Bienvenue ! Configurez vos paramètres pour commencer.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
            else:
                st.warning("L'image de bienvenue n'a pas été trouvée.")
        else:
            placeholder.empty()
        
    def configure_page(self):
        st.sidebar.title("Configuration")

    def select_dataset(self):
        st.sidebar.subheader("Datasets disponibles")
        dataset_choice = st.sidebar.selectbox("Choisir un dataset", ["Dataset 1", "Dataset 2"])
        self.selected_data = data if dataset_choice == "Dataset 1" else data2

    def show_attributes(self):
        st.sidebar.subheader("Attributs disponibles")
        self.selected_attributes = st.sidebar.multiselect("Sélectionnez les attributs", options=self.selected_data.columns, default=self.selected_data.columns)
        return self.selected_attributes

    def select_plot_type(self):
        st.sidebar.subheader("Visualisation")
        plot_attributes = {}

        # Ajouter une liste des types de visualisation disponibles
        available_plot_types = ["Boxplot", "Scatter","Map"]
        
        
        # Choisir le type de visualisation
        self.plot_type = st.sidebar.selectbox("Choisir le type de visualisation", available_plot_types)

        # Attributs pour chaque type de visualisation
        if self.plot_type == "Boxplot":
            self.boxplot_attr = st.sidebar.multiselect("Choisir l'attribut pour le boxplot", options=self.selected_data.columns, default=self.selected_attributes)
            plot_attributes['boxplot'] = self.boxplot_attr

        elif self.plot_type == "Scatter":
            self.x_attr = st.sidebar.selectbox("Choisir l'attribut pour l'axe X", self.selected_attributes)
            self.y_attr = st.sidebar.selectbox("Choisir l'attribut pour l'axe Y", self.selected_attributes)
            plot_attributes['scatter'] = {'x': self.x_attr, 'y': self.y_attr}

        elif self.plot_type == "Map":
            # st.sidebar.write("Affichage de la carte disponible pour les datasets contenant des coordonnées géographiques.")
            plot_attributes['map'] = {'latitude': 'latitude', 'longitude': 'longitude'}

        return self.plot_type, plot_attributes

    def select_preprocessing(self):
        st.sidebar.subheader("Pré-traitement")
        # Normalisation
        normalisation = st.sidebar.selectbox("Choisir une méthode de normalisation", ["None","Z-score", "Min-Max"])
        norm_attributes = st.sidebar.multiselect("Attributs à normaliser", self.selected_data.columns) if normalisation != "None" else []

        # Discrétisation
        discretisation = st.sidebar.selectbox("Choisir une méthode de discrétisation", ["None", "Equal Frequency", "Amplitude"])
        disc_attributes = st.sidebar.multiselect("Attributs à discrétiser", self.selected_data.columns) if discretisation != "None" else []

        # Réduction
        reduction = st.sidebar.selectbox("Choisir une méthode de réduction", ["None","Horizontal", "Vertical"])
        red_attributes = st.sidebar.multiselect("Attributs à réduire", self.selected_data.columns) if reduction != "None" else []

        # Handling outliers
        outliers = st.sidebar.selectbox("Choisir une méthode de traitement des valeurs aberrantes", ["None", "Delete", "Mean", "Median", "Mode"])
        outlier_attributes = st.sidebar.multiselect("Attributs avec des valeurs aberrantes", self.selected_data.columns) if outliers != "None" else []
        
        # rodondance 
        rodondance = st.sidebar.selectbox("Choisir une méthode de traitement des valeurs rodondantes", ["None", "Delete"])  
        rodondance_attributes = st.sidebar.multiselect("Attributs avec des valeurs rodondantes", self.selected_data.columns) if rodondance != "None" else []

        self.preprocess_options = {
            "normalisation": (normalisation, norm_attributes),
            "discretisation": (discretisation, disc_attributes),
            "reduction": (reduction, red_attributes),
            "outliers": (outliers, outlier_attributes),
            "rodondance": (rodondance, rodondance_attributes)
        }
    
    def validate_button(self):
        st.markdown(
            """
            <style>
            div.stButton > button:first-child {
                background-color: transparent;
                border: 1px solid #FF4B4B;
                color: #FF4B4B;
                width: 100%;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 16px;
                text-align: center;
                transition: all 0.5s ease-in-out;
            }
            div.stButton > button:first-child:hover {
                background-color: #FF4B4B;
                border: 1px solid #FF4B4B;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )
        if st.sidebar.button("Valider"):
            st.session_state['choices_validated'] = True
            self.choices_validated = True
            return True
        return False
    
    def show_dataset_overview(self):
        st.subheader("Aperçu du Dataset")
        st.dataframe(self.selected_data)  # Affiche les premières lignes du dataset

    def show_column_information(self):
        st.subheader("Informations sur les Colonnes")
        for col in self.selected_data.columns:
            with st.expander(f"Détails sur la colonne : {col}"):
                # Divise l'espace en deux colonnes : Infos à gauche, Histogramme à droite
                info_col, plot_col = st.columns([1, 2])

                # Afficher les informations de base pour chaque colonne dans la première colonne
                with info_col:
                    st.write(f"Type : {self.selected_data[col].dtype}")
                    st.write(f"Valeurs uniques : {self.selected_data[col].nunique()}")
                    st.write(f"Valeurs manquantes : {self.selected_data[col].isna().sum()}")
                    
                    # Afficher les statistiques descriptives si la colonne est numérique
                    if pd.api.types.is_numeric_dtype(self.selected_data[col]):
                        st.write(f"Moyenne : {self.selected_data[col].mean()}")
                        st.write(f"Écart-type : {self.selected_data[col].std()}")
                        st.write(f"Min : {self.selected_data[col].min()}")
                        st.write(f"Max : {self.selected_data[col].max()}")

                
                # Afficher le histogramme dans la deuxième colonne
                with plot_col:
                    if pd.api.types.is_numeric_dtype(self.selected_data[col]):
                        # Histogramme
                        fig = go.Figure()
                        hist_data = self.selected_data[col].dropna()
                        fig.add_trace(go.Histogram(
                            x=hist_data,
                            nbinsx=30,
                            name="Histogramme",
                            marker=dict(
                                color="skyblue",                 # Couleur de remplissage
                                line=dict(color="black", width=1)  # Bordure noire
                            ),
                            opacity=0.75,
                        ))
                        # Calculer la densité et ajouter la courbe
                        density = gaussian_kde(self.selected_data[col].dropna())
                        x_vals = np.linspace(self.selected_data[col].min(), self.selected_data[col].max(), 100)
                        fig.add_trace(go.Scatter(
                            x=x_vals,
                            y=density(x_vals) * len(self.selected_data[col]) * (x_vals[1] - x_vals[0]),  # Mise à l'échelle
                            mode="lines",
                            name="Densité",
                            line=dict(color="orange", width=2)
                        ))

                        # Mettre à jour la mise en page
                        fig.update_layout(
                            title=f"Distribution de {col}",
                            xaxis_title=col,
                            yaxis_title="Count",
                            template="plotly_dark"
                        )
                        st.plotly_chart(fig, use_container_width=True)
                        
                        
            
        
    def run(self):
        # Configure la page latérale et l'image de bienvenue
        self.configure_page()
        # self.show_welcome_image(st.empty())
        self.select_dataset()
        self.select_plot_type()
        self.select_preprocessing()
        # Bouton de validation pour confirmer les choix
        if self.validate_button():
            # st.empty()
            # self.show_welcome_image(st.empty())
            
            # Affiche les onglets pour passer entre "Data" et "Columns"
            tabs = st.tabs(["Data", "Columns","Visualisation"])
            
            with tabs[0]:  # Onglet "Data"
                self.show_dataset_overview()  # Affiche l'aperçu du dataset

            with tabs[1]:  # Onglet "Columns"
                self.show_column_information()  # Affiche les informations détaillées sur les colonnes

            
            

if __name__ == "__main__":
    app = ClimatApp()
    app.run()



