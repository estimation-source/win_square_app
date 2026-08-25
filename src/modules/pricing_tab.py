import streamlit as st
import pandas as pd

def render_pricing_tab():
    """Renders the Detailed Pricing Breakdown & Costing Table."""
    st.markdown("#### **💰 Pricing & Area Breakdown Summary**")
    st.markdown("<hr style='margin-top:5px; margin-bottom:20px;'>", unsafe_allow_html=True)

    designs = st.session_state["window_designs"]
    if not designs:
        st.info("No window designs available to show pricing.")
        return

    df = pd.DataFrame(designs)
    
    # Square feet calculation formula: (Width_mm * Height_mm) / 92903.04
    df["Sq.Ft"] = ((df["width"] * df["height"]) / 92903.04).round(2)
    df["Total Price (₹)"] = (df["price"] * df["qty"]).round(2)
    
    # Column Renaming for Professional Presentation
    df_display = df.rename(columns={
        "code": "Window Code",
        "type": "Design Type",
        "width": "Width (mm)",
        "height": "Height (mm)",
        "qty": "Quantity",
        "price": "Unit Price (₹)"
    })

    st.dataframe(
        df_display[["Window Code", "Design Type", "Width (mm)", "Height (mm)", "Sq.Ft", "Quantity", "Unit Price (₹)", "Total Price (₹)"]],
        use_container_width=True,
        hide_index=True
    )

    # Costing Overview Metrics
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Windows Quantity", f"{df['qty'].sum()} Pcs")
    with c2:
        st.metric("Total Area Covered", f"{df['Sq.Ft'].sum():,.2f} Sq.Ft")
    with c3:
        st.metric("Grand Total Cost", f"₹{df['Total Price (₹)'].sum():,.2f}")
