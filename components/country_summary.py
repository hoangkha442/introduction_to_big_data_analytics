import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render(db):
    st.subheader("🌍 Tổng quan doanh thu theo quốc gia")

    # Lấy dữ liệu từ MongoDB
    df = pd.DataFrame(list(db.summary_country.find()))
    if df.empty:
        st.warning("Không có dữ liệu quốc gia.")
        return

    df = df.sort_values("TotalRevenue", ascending=False)

    # Tuỳ chọn hiển thị
    top_n = st.selectbox("Hiển thị Top quốc gia theo doanh thu", [3, 4, 5, 10, 20], index=2)

    # Hiển thị bảng
    st.subheader(f"📋 Dữ liệu chi tiết – Top {top_n} quốc gia")
    st.dataframe(df.head(top_n))

    # Biểu đồ doanh thu
    st.subheader("📊 Biểu đồ doanh thu")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(df["Country"].head(top_n)[::-1], df["TotalRevenue"].head(top_n)[::-1], color="#3399FF")
    ax.set_xlabel("Doanh thu")
    ax.set_title(f"Top {top_n} quốc gia theo doanh thu")
    st.pyplot(fig)
