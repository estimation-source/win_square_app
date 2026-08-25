import os
import streamlit as st
from src.data_models import init_session_state
from src.modules.documents_tab import render_documents_tab
from src.modules.design_tab import render_design_tab
from src.modules.pricing_tab import render_pricing_tab
from src.modules.report_tab import render_report_tab

# Page Layout & Configuration
st.set_page_config(
    page_title="WIN-SQUARE | Enterprise Design Studio",
    layout="wide",
    page_icon="🪟"
)

# Load External Styling
def load_css(file_path: str):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# Initialize Application State Data
init_session_state()

# Global Header Dashboard Summary
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    client = st.session_state["client_info"]
    st.markdown(f"### 🏢 **{client['name']}** &nbsp;&nbsp; <span style='font-size:14px; color:#64748b;'>{client['quotation_no']}</span>", unsafe_allow_html=True)
with col_h2:
    total_val = sum(w["price"] * w["qty"] for w in st.session_state["window_designs"])
    total_qty = sum(w["qty"] for w in st.session_state["window_designs"])
    st.markdown(f"<div style='text-align:right;'><b style='font-size:20px; color:#0f172a;'>₹{total_val:,.2f}</b><br><span style='font-size:12px; color:#64748b;'>Total Qty: {total_qty} Pcs</span></div>", unsafe_allow_html=True)

# Application Navigation Tabs
tab_docs, tab_design, tab_pricing, tab_report = st.tabs([
    "📄 Documents", 
    "✏️ Design Studio", 
    "💰 Pricing", 
    "📊 Quotation Report"
])

with tab_docs:
    render_documents_tab()

with tab_design:
    render_design_tab()

with tab_pricing:
    render_pricing_tab()

with tab_report:
    render_report_tab()
