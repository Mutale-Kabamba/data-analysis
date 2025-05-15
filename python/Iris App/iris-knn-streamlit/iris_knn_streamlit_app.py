import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Load your custom Iris dataset
file_path = "Data_CW2.xlsx"
df_iris = pd.read_excel(file_path, engine='openpyxl', sheet_name='Iris', header=None)
df_iris = df_iris[0].str.split(',', expand=True)
df_iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "variety"]
# Encode target labels
le = LabelEncoder()
df_iris['label'] = le.fit_transform(df_iris['variety'])

# Split features and target
X = df_iris.drop(columns=['variety', 'label'])
y = df_iris['label']

# Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

# Streamlit UI setup
st.set_page_config(page_title="Iris K-NN Classifier", layout="centered")
st.title("🌼 Iris Flower Classifier")
st.markdown("Use the sliders below to input flower measurements and predict the variety.")

# User input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.5)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

# Make prediction
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
predicted_class = le.inverse_transform(prediction)[0]

# Display result
st.success(f"Predicted Flower Variety: **{predicted_class}**")
st.write("### Input Data")
st.write(f"- Sepal Length: {sepal_length} cm")
st.write(f"- Sepal Width: {sepal_width} cm")
st.write(f"- Petal Length: {petal_length} cm")
st.write(f"- Petal Width: {petal_width} cm")