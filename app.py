import streamlit as st
import seaborn as sns
from config.db_connection import get_database

# Import component
from components.total_spent import render as render_total_spent
from components.frequency import render as render_frequency
from components.top_products import render as render_top_products
from components.monthly_revenue import render as render_monthly_revenue
from components.avg_quantity import render as render_avg_quantity
from components.rfm_segment import render as render_rfm_segment
from components.pca_rfm import render as render_pca_rfm
from components.outlier_flag import render as render_outlier_flag
from components.forecast import render as render_forecast
from components.recommendations import render as render_recommendations
from components.country_summary import render as render_country_summary
from components.product_graph import render as render_product_graph

# UI cấu hình
st.set_page_config(page_title="📊 E-Commerce Dashboard", layout="wide")
sns.set_style("whitegrid")

# DB
db = get_database()

# Sidebar menu
menu = st.sidebar.selectbox("🔍 Chọn nhóm phân tích", [
    "👤 Phân tích khách hàng",
    "📈 Hiệu suất bán hàng",
    "📊 Dự báo & bất thường",
    "🌍 Tổng quan & Gợi ý",
    "📦 Phân tích sản phẩm"
])

# ------------------------ NHÓM 1: PHÂN TÍCH KHÁCH HÀNG ------------------------
if menu == "👤 Phân tích khách hàng":
    st.header("👤 Phân tích khách hàng")

    col1, col2 = st.columns(2)
    with col1:
        render_total_spent(db)
    with col2:
        render_frequency(db)

    st.markdown("---")
    render_rfm_segment(db)
    render_pca_rfm(db)

# ------------------------ NHÓM 2: HIỆU SUẤT BÁN HÀNG ------------------------
elif menu == "📈 Hiệu suất bán hàng":
    st.header("📈 Hiệu suất bán hàng")

    col1, col2 = st.columns(2)
    with col1:
        render_top_products(db)
    with col2:
        render_avg_quantity(db)

    st.markdown("---")
    render_monthly_revenue(db)

# ------------------------ NHÓM 3: DỰ BÁO & BẤT THƯỜNG ------------------------
elif menu == "📊 Dự báo & bất thường":
    st.header("📊 Dự báo & phát hiện bất thường")

    col1, col2 = st.columns(2)
    with col1:
        render_forecast(db)
    with col2:
        render_outlier_flag(db)

# ------------------------ NHÓM 4: TỔNG QUAN & GỢI Ý ------------------------
elif menu == "🌍 Tổng quan & Gợi ý":
    st.header("🌍 Tổng quan theo quốc gia & Gợi ý sản phẩm")

    col1, col2 = st.columns(2)
    with col1:
        render_country_summary(db)
    with col2:
        render_recommendations(db)

# ------------------------ NHÓM 5: PHÂN TÍCH SẢN PHẨM ------------------------
elif menu == "📦 Phân tích sản phẩm":
    st.header("📦 Đồ thị phân tích sản phẩm")
    render_product_graph(db)
