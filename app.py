import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Talking Rabbitt")

st.title("🐰 Talking Rabbitt")
st.write("Talk to your business data")

uploaded_file = st.file_uploader("Upload your Sales CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question")

    if question:

        question = question.lower()

        if "region" in question:

            result = df.groupby("Region")["Revenue"].sum()

            top_region = result.idxmax()

            st.success(f"Highest revenue region: {top_region}")

            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        elif "product" in question:

            result = df.groupby("Product")["Revenue"].sum()

            top_product = result.idxmax()

            st.success(f"Top product: {top_product}")

            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)

            st.pyplot(fig)

        else:
            st.write("Try asking about region or product revenue.")
