import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render(db):
    df = pd.DataFrame(list(db.customer_frequency.find()))
    st.subheader("📈 Tần suất mua hàng theo khách hàng")

    # Sắp xếp và chọn số lượng hiển thị
    df = df.sort_values("Frequency", ascending=False)
    num = st.slider("Chọn số khách hàng hiển thị", 5, 50, 15)
    top_df = df.head(num)

    # Hiển thị bảng
    st.subheader("🔢 Dữ liệu chi tiết")
    st.dataframe(top_df)

    # Biểu đồ
    st.subheader("📊 Biểu đồ tần suất mua hàng")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=top_df, x="CustomerID", y="Frequency", ax=ax, palette="crest")
    ax.set_xlabel("Customer ID")
    ax.set_ylabel("Số lần mua")
    ax.set_title("Tần suất mua hàng của khách hàng")
    plt.xticks(rotation=45)
    st.pyplot(fig)
