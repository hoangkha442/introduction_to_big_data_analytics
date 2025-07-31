import streamlit as st
import pandas as pd

def render(db):
    st.subheader("📊 Gợi ý sản phẩm theo khách hàng")

    # Lấy dữ liệu từ MongoDB
    df = pd.DataFrame(list(db.product_recommendations.find()))

    if df.empty:
        st.warning("Không có dữ liệu.")
        return

    # Cho chọn số lượng hiển thị
    num_display = st.selectbox("Chọn số lượng khách hàng hiển thị", [10, 20, 30, 50, 100], index=1)

    # Hiển thị bảng
    st.dataframe(df.head(num_display))
