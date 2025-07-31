import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    df = pd.DataFrame(list(db.monthly_revenue.find()))
    st.subheader("Doanh thu theo tháng")
    df["Year-Month"] = df["Year"].astype(str) + "-" + df["Month"].astype(str).str.zfill(2)
    df = df.sort_values("Year-Month")
    fig, ax = plt.subplots(figsize=(12,5))
    sns.lineplot(data=df, x="Year-Month", y="Revenue", marker="o", ax=ax)
    st.pyplot(fig)
