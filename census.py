import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
@st.cache()
def load_data():
    df = pd.read_csv("adult.csv", header=None)
    df.head()
    column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    for i in range(df.shape[1]):
        df.rename(columns={i:column_name[i]},inplace=True)
    df.head()
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
census_df = load_data()
df = census_df

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Census Data Visualization App")
st.sidebar.subheader("Menu")
if st.sidebar.checkbox("Show raw data"):
    st.subheader("Full Dataset")
    st.dataframe(df)
st.sidebar.subheader("Visualization Selector")
plot_types = st.sidebar.multiselect("Select the Visualizers", ("Box Plot", "Count Plot", "Pie Chart"))
if "Box Plot" in plot_types:
    st.subheader("Box Plot")
    box_plot_columns = st.sidebar.multiselect("Select the Box Plot Features", ("income", "gender"))
    for i in box_plot_columns:
        plt.figure()
        plt.title(f"Box Plot for {i}")
        sns.boxplot(x = df["hours-per-week"], y = df[i])
        st.pyplot()
if "Pie Chart" in plot_types:
    st.subheader("Pie Charts")
    pie_chart_columns = st.sidebar.multiselect("Select the Pie Chart Features", ("income", "gender"))
    for i in pie_chart_columns:
        plt.figure()
        plt.title(f"Pie Chart for {i}")
        plt.pie(df[i].value_counts(), labels = df[i].value_counts().index, autopct = "%.2f%%")
        st.pyplot()
if "Count Plot" in plot_types:
    st.subheader("Count Plot")
    plt.figure()
    sns.countplot(x = df["workclass"], hue = df["income"])
    st.pyplot()