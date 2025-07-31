import streamlit as st

def render_sidebar():
    return st.sidebar.radio("📂 Chọn loại phân tích", [
        "Tổng chi tiêu theo khách hàng",
        "Sản phẩm bán chạy",
        "Doanh thu theo tháng",
        "Số lượng trung bình mỗi đơn hàng",
        "Phân khúc khách hàng (RFM)",
        "Gợi ý sản phẩm"
    ])
