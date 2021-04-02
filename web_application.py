
import pandas as pd
import numpy as np
import streamlit as st  # please insatll the package first using pip install streamlit
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App
""")

st.sidebar.header('Input Parameters')


def input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.0, 8.0, 5.2)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 5.0, 3.5)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 7.0, 2.2)
    petal_width = st.sidebar.slider('Petal Width', 1.0, 3.0, 2.5)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


df = input_features()

st.subheader('User Input')
st.write(df)


iris = datasets.load_iris()
X = iris.data
Y = iris.target

model = RandomForestClassifier()
model.fit(X, Y)

prediction = model.predict(df)
prediction_probability = model.predict_proba(df)


st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])


st.subheader('Prediction Probability')
st.write(prediction_probability)

# Use command prompt to run the file use stremlit run [file name.py]
# Remember you need to go to the same folder using command prompt to run the file