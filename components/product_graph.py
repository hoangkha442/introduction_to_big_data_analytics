import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def render(db):
    st.subheader("🔗 Đồ thị đồng xuất hiện sản phẩm")
    st.markdown("""
    - Mỗi **nút** là một sản phẩm.
    - Mỗi **cạnh nối** biểu thị hai sản phẩm thường được mua chung trong cùng một đơn hàng.
    - **Độ dày cạnh** thể hiện tần suất đồng xuất hiện: càng dày → càng thường xuyên.
    """)

    # Lấy dữ liệu từ MongoDB
    df = pd.DataFrame(list(db.product_graph.find()))
    if df.empty:
        st.warning("Không có dữ liệu đồng xuất hiện sản phẩm.")
        return

    # Tạo đồ thị
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row["productA"], row["productB"], weight=row["weight"])

    # Vẽ đồ thị
    fig, ax = plt.subplots(figsize=(12, 9))
    pos = nx.spring_layout(G, k=0.4, seed=42)

    # Vẽ cạnh với độ dày phụ thuộc trọng số (weight)
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, alpha=0.5, width=[w * 0.5 for w in edge_weights])

    # Vẽ nút
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="#72A0C1")

    # Vẽ nhãn sản phẩm
    nx.draw_networkx_labels(G, pos, font_size=9)

    # Tiêu đề và hiển thị
    ax.set_title("Mối liên hệ giữa các sản phẩm thường được mua cùng nhau", fontsize=14)
    ax.axis('off')
    st.pyplot(fig)
