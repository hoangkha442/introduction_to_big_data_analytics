import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    df = pd.DataFrame(list(db.monthly_outlier_flag.find()))
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.sort_values("ds")

    st.subheader("📊 Phát hiện doanh thu bất thường theo tháng")

    # Filter theo năm
    years = sorted(df["ds"].dt.year.unique())
    selected_year = st.selectbox("Chọn năm", years)
    df = df[df["ds"].dt.year == selected_year]

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x="ds", y="y", marker="o", label="Doanh thu", ax=ax)

    # Highlight outliers
    outliers = df[df["outlier"] == "Outlier"]
    sns.scatterplot(data=outliers, x="ds", y="y", color="red", s=150, label="Outlier", ax=ax)

    # Ghi nhãn giá trị outlier
    for i, row in outliers.iterrows():
        ax.text(row["ds"], row["y"] + 10000, f'{int(row["y"]):,}', color='red', fontsize=9)

    ax.set_title(f"📉 Doanh thu theo tháng năm {selected_year}", fontsize=16)
    ax.set_xlabel("Thời gian")
    ax.set_ylabel("Doanh thu")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
