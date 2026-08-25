from __future__ import annotations
import streamlit as st
import datetime
import random

def init_session_state():
    """Initializes clean/blank session state models for new quotation."""
    
    # Auto-generate unique quotation number if not present
    if "client_info" not in st.session_state:
        random_id = random.randint(1000, 9999)
        st.session_state["client_info"] = {
            "name": "",
            "quotation_no": f"WIN-QT-{random_id}",
            "location": "",
            "date": datetime.date.today(),
            "sales_person": ""
        }

    # Start with empty window design list
    if "window_designs" not in st.session_state:
        st.session_state["window_designs"] = []
