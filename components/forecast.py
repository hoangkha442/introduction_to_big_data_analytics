import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    st.subheader("📈 Dự báo doanh thu 3 tháng tới")

    # Lấy dữ liệu từ MongoDB
    df = pd.DataFrame(list(db.monthly_forecast.find()))
    df["ds"] = pd.to_datetime(df["ds"])
    df = df.sort_values("ds")

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x="ds", y="yhat", label="Dự báo", marker="o", color="#1f77b4", ax=ax)

    # Vùng dự báo (confidence interval)
    ax.fill_between(df["ds"], df["yhat_lower"], df["yhat_upper"], color="#1f77b4", alpha=0.2, label="Khoảng tin cậy")

    # Tùy chỉnh
    ax.set_title("🔮 Dự báo doanh thu 3 tháng tới", fontsize=16)
    ax.set_xlabel("Thời gian", fontsize=12)
    ax.set_ylabel("Doanh thu dự báo", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    # Hiển thị biểu đồ
    st.pyplot(fig)

    # Hiển thị bảng dữ liệu
    with st.expander("📋 Xem dữ liệu chi tiết"):
        st.dataframe(df[["ds", "yhat", "yhat_lower", "yhat_upper"]].rename(columns={
            "ds": "Thời gian",
            "yhat": "Dự báo",
            "yhat_lower": "Giới hạn dưới",
            "yhat_upper": "Giới hạn trên"
        }))
