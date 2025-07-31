import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    st.subheader("📊 Phân khúc khách hàng (RFM) + Phát hiện Outlier")

    # Load data từ MongoDB
    df = pd.DataFrame(list(db.customer_segments_summary.find()))
    if df.empty:
        st.warning("Không có dữ liệu phân cụm khách hàng.")
        return

    st.subheader("📋 Dữ liệu RFM")
    st.dataframe(df)

    # Gắn nhãn outlier dựa vào giá trị bất thường
    q1 = df["Avg_Monetary"].quantile(0.25)
    q3 = df["Avg_Monetary"].quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr

    df["Outlier"] = df["Avg_Monetary"].apply(lambda x: "Outlier" if x > upper_bound else "Normal")

    # Vẽ biểu đồ
    st.subheader("🎯 Biểu đồ phân khúc + Outliers")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=df, x="Avg_Recency", y="Avg_Monetary",
                    size="Avg_Frequency", hue="Outlier", sizes=(50, 500), ax=ax, palette={"Outlier": "red", "Normal": "blue"})
    ax.set_title("Phân cụm khách hàng theo RFM (có Outlier)")
    st.pyplot(fig)

    # Hiển thị bảng outlier riêng
    st.subheader("🚨 Các nhóm khách hàng Outlier (chi tiêu bất thường)")
    st.dataframe(df[df["Outlier"] == "Outlier"])
