import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualization:
    def __init__(self, data, attributes, plot_type, preprocess_options):
        self.data = data[attributes]
        self.plot_type = plot_type
        self.preprocess_options = preprocess_options
        
    
    def display_data_and_plots(self):
        st.write("### Graphiques")
        
        # if self.plot_type == "Scatter":
        #     self.display_scatter_plot()
        # elif self.plot_type == "Histogram":
        #     self.display_histogram()
        # elif self.plot_type == "Boxplot":
        #     self.display_boxplot()
        # elif self.plot_type == "Map":
        #     self.display_map()
            
        st.write("### Données sélectionnées")
        st.write(self.data)
        st.dataframe(self.data)
        
        
    # def show_column_information(self):
        st.subheader("Informations sur les Colonnes")
        for col in self.selected_data.columns:
            with st.expander(f"Détails sur la colonne : {col}"):
                # Afficher les informations de base pour chaque colonne
                st.write(f"Type : {self.selected_data[col].dtype}")
                st.write(f"Valeurs uniques : {self.selected_data[col].nunique()}")
                st.write(f"Valeurs manquantes : {self.selected_data[col].isna().sum()}")
                
                # Afficher les statistiques descriptives si la colonne est numérique
                if pd.api.types.is_numeric_dtype(self.selected_data[col]):
                    st.write(f"Moyenne : {self.selected_data[col].mean()}")
                    st.write(f"Écart-type : {self.selected_data[col].std()}")
                    st.write(f"Min : {self.selected_data[col].min()}")
                    st.write(f"Max : {self.selected_data[col].max()}")

    # def display_scatter_plot(self):
    #     plt.figure(figsize=(10, 6))
    #     sns.scatterplot(data=self.data, x=self.data.columns[0], y=self.data.columns[1])
    #     st.pyplot(plt)

    # def display_histogram(self):
    #     plt.figure(figsize=(10, 6))
    #     self.data[self.data.columns[0]].hist()
    #     st.pyplot(plt)
        
    # def display_boxplot(self):
    #     plt.figure(figsize=(10, 6))
    #     sns.boxplot(data=self.data)
    #     st.pyplot(plt)
    # def display_map(self):
    #     plt.figure(figsize=(10, 6))
    #     sns.scatterplot(data=self.data, x=self.data.columns[0], y=self.data.columns[1])
    #     st.pyplot(plt)
