import streamlit as st

def render_documents_tab():
    """Renders the Blank Client & Project Information Form."""
    st.markdown("#### **📄 Client & Project Information**")
    st.markdown("<hr style='margin-top:5px; margin-bottom:20px;'>", unsafe_allow_html=True)
    
    client_info = st.session_state["client_info"]
    
    col1, col2 = st.columns(2)
    with col1:
        client_info["name"] = st.text_input(
            "Client / Project Name", 
            value=client_info["name"], 
            placeholder="Enter Client Name (e.g., ID RAJ KOTHARI)"
        )
        client_info["location"] = st.text_input(
            "Site / Project Location", 
            value=client_info["location"], 
            placeholder="Enter Location (e.g., Pune, Second Floor)"
        )
        client_info["sales_person"] = st.text_input(
            "Sales Representative", 
            value=client_info["sales_person"], 
            placeholder="Enter Sales Executive Name"
        )
        
    with col2:
        client_info["quotation_no"] = st.text_input(
            "Quotation Number", 
            value=client_info["quotation_no"]
        )
        client_info["date"] = st.date_input(
            "Quotation Date", 
            value=client_info["date"]
        )
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **Note:** Enter client details here to automatically populate across all reports and PDF quotes.")
