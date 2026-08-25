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
col_h1, col_h2, col_h3 = st.columns([2.5, 1, 1])

with col_h1:
    client = st.session_state["client_info"]
    client_title = client['name'] if client['name'].strip() else "NEW CLIENT"
    st.markdown(
        f"### 🏢 **{client_title}** &nbsp;&nbsp; "
        f"<span style='font-size:14px; color:#64748b;'>{client['quotation_no']}</span>", 
        unsafe_allow_html=True
    )

with col_h2:
    if st.button("🔄 Start New Quote", use_container_width=True):
        st.session_state.clear()
        st.rerun()

with col_h3:
    total_val = sum(w["price"] * w["qty"] for w in st.session_state["window_designs"])
    total_qty = sum(w["qty"] for w in st.session_state["window_designs"])
    st.markdown(
        f"<div style='text-align:right;'><b style='font-size:20px; color:#0f172a;'>₹{total_val:,.2f}</b>"
        f"<br><span style='font-size:12px; color:#64748b;'>Total Qty: {total_qty} Pcs</span></div>", 
        unsafe_allow_html=True
    )

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
