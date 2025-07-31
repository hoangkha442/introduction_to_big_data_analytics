import streamlit as st
import pandas as pd

def render(db):
    df = pd.DataFrame(list(db.customer_total_spent.find()))
    st.subheader("Tổng chi tiêu theo khách hàng")
    num = st.slider("Số khách hàng hiển thị", 5, 50, 10)
    df = df.sort_values("TotalSpent", ascending=False).head(num)
    st.dataframe(df)
    st.bar_chart(df.set_index("CustomerID")["TotalSpent"])
