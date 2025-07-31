import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    df = pd.DataFrame(list(db.top_selling_products.find()))
    st.subheader("Sản phẩm bán chạy")
    num = st.slider("Hiển thị top", 5, 30, 10)
    df = df.sort_values("TotalSold", ascending=False).head(num)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(data=df, x="TotalSold", y="Description", ax=ax, palette="viridis")
    st.pyplot(fig)
