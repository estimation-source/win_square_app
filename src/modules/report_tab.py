import streamlit as st
from src.pdf_generator import generate_pdf_quotation

def render_report_tab():
    """Renders the Final Quotation Preview and Export Tab."""
    st.markdown("#### **📊 Final Quotation Export**")
    st.markdown("<hr style='margin-top:5px; margin-bottom:20px;'>", unsafe_allow_html=True)

    client_info = st.session_state["client_info"]
    designs = st.session_state["window_designs"]

    st.success("✅ Quotation data is synchronized and ready for client delivery!")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"**Client Name:** {client_info['name']}")
        st.markdown(f"**Quotation Ref No:** {client_info['quotation_no']}")
        st.markdown(f"**Total Configured Windows:** {len(designs)} Items")

    with col2:
        pdf_buffer = generate_pdf_quotation(client_info, designs)
        st.download_button(
            label="📥 Download Official PDF Quotation",
            data=pdf_buffer,
            file_name=f"Quotation_{client_info['quotation_no']}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
