import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict  # make sure this exists

# App title
st.title("🌸 Iris Flower Classifier")

# Description
st.markdown("""
Welcome to the **Iris Flower Classifier**!  
This is a simple toy model that classifies iris flowers into:
- *Setosa*
- *Versicolor*
- *Virginica*

Based on the **sepal** and **petal** dimensions 🌿
""")

# Tabs for different features
tab1, tab2 = st.tabs(["🔍 Iris Classifier", "📌 Feature 2 (Coming Soon)"])

# ===================== TAB 1 =====================
with tab1:
    st.header("🌼 Enter Plant Features")

    st.markdown("Customize the features of your flower below:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌿 Sepal")
        sepal_l = st.slider('Sepal Length (cm)', 1.0, 8.0, 5.0)
        sepal_w = st.slider('Sepal Width (cm)', 2.0, 4.4, 3.0)

    with col2:
        st.subheader("🌸 Petal")
        petal_l = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
        petal_w = st.slider('Petal Width (cm)', 0.1, 2.5, 1.0)

    st.markdown("---")

    if st.button("🔮 Predict Type of Iris"):
        result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
        st.success(f"🌼 Predicted Iris Type: **{result[0].capitalize()}**")

# ===================== TAB 2 =====================
with tab2:
    st.header("🚧 Feature Under Construction")

    st.markdown("""
    <div style='text-align:center;'>
        <h2 style='color:#555;'>Coming Soon...</h2>
        <p style='color:blue; font-size:20px;'>
            <em>Thank you so much for your patience 💙</em>
        </p>
        <img src="https://media.giphy.com/media/xTk9ZvMnbIiIew7IpW/giphy.gif" width="300">
    </div>
    """, unsafe_allow_html=True)
