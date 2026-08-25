from __future__ import annotations
import streamlit as st

def init_session_state():
    """Initializes global data models in Streamlit session state."""
    
    # Client & Project Documents Info
    if "client_info" not in st.session_state:
        st.session_state["client_info"] = {
            "name": "ID RAJ KOTHARI",
            "quotation_no": "WIN-QT-00000365",
            "location": "SECOND FLOOR, PUNE",
            "date": "2026-08-25",
            "sales_person": "Win-Square Team"
        }

    # Initial Mock Window Designs Data
    if "window_designs" not in st.session_state:
        st.session_state["window_designs"] = [
            {
                "code": "W4A",
                "qty": 1,
                "location": "SECOND FLOOR",
                "series": "KOMMERLING SYSTEM ORTA SLIDING SERIES NEW",
                "glass": "(1,2) 6 MM CLEAR TOUGHENED GLASS",
                "color": "WHITE",
                "width": 1219,
                "height": 1956,
                "type": "2 Track Sliding",
                "price": 30459.94
            },
            {
                "code": "SLIT 4",
                "qty": 1,
                "location": "SECOND FLOOR",
                "series": "KOMMERLING PROVENT CASEMENT SERIES NEW",
                "glass": "(1) 5mm Clear Toughened",
                "color": "WHITE",
                "width": 304,
                "height": 1549,
                "type": "Single Sash Casement",
                "price": 3518.54
            },
            {
                "code": "W2C",
                "qty": 1,
                "location": "SECOND FLOOR",
                "series": "KOMMERLING GOLD ASEA CASEMENT SERIES",
                "glass": "(1) 8 MM CLEAR TOUGHENED GLASS",
                "color": "WHITE",
                "width": 2596,
                "height": 1549,
                "type": "Fixed Glass",
                "price": 34133.73
            },
            {
                "code": "W5",
                "qty": 1,
                "location": "SECOND FLOOR",
                "series": "KOMMERLING GOLD ASEA CASEMENT SERIES",
                "glass": "(1) 8 MM CLEAR TOUGHENED GLASS",
                "color": "WHITE",
                "width": 889,
                "height": 2870,
                "type": "Fixed Glass",
                "price": 18786.65
            }
        ]
