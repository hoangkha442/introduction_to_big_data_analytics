import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    st.subheader("📦 Số lượng trung bình mỗi đơn hàng")

    df = pd.DataFrame(list(db.monthly_avg_quantity_per_invoice.find()))
    
    if df.empty:
        st.warning("Không có dữ liệu để hiển thị.")
        return

    # Làm sạch dữ liệu
    df["Year"] = df["Year"].astype(str)
    df["Month"] = df["Month"].astype(int).astype(str).str.zfill(2)
    df["Year-Month"] = df["Year"] + "-" + df["Month"]
    df = df.sort_values("Year-Month")

    # Filter tháng
    options = df["Year-Month"].tolist()
    selected_month = st.selectbox("📅 Chọn tháng", options[::-1])  # Hiện tháng mới nhất trước

    # Hiển thị metric
    selected_value = df[df["Year-Month"] == selected_month]["AvgQuantityPerInvoice"].values[0]
    st.metric(f"Trung bình sản phẩm / đơn hàng ({selected_month})", round(selected_value, 2))

    # Biểu đồ line
    st.subheader("📊 Biểu đồ theo thời gian")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=df, x="Year-Month", y="AvgQuantityPerInvoice", marker="o", ax=ax)
    ax.set_title("Số lượng trung bình mỗi đơn hàng theo thời gian")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Trung bình sản phẩm/đơn")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Hiển thị bảng
    st.subheader("📋 Dữ liệu chi tiết")
    st.dataframe(df[["Year-Month", "AvgQuantityPerInvoice"]].set_index("Year-Month"))
