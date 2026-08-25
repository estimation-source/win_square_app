import streamlit as st
from src.cad_engine import generate_window_cad

@st.dialog("✏️ Interactive Window CAD Studio", width="large")
def edit_window_canvas_dialog(index: int):
    win = st.session_state["window_designs"][index]
    
    # Header Details Bar
    st.markdown(f"""
        <div style="background:#ffffff; padding:10px 15px; border-radius:6px; border:1px solid #e2e8f0; margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <b>Design Ref :</b> {win['code']} &nbsp;|&nbsp; <b>Location :</b> {win['location']} &nbsp;|&nbsp; <b>Qty :</b> {win['qty']}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2-Column Studio Layout: Left Sidebar + Canvas Area + Right Config
    col_tools, col_canvas, col_config = st.columns([0.8, 3.5, 2.2])

    with col_tools:
        st.caption("Tools")
        st.button("📄", help="Fixed Glass", use_container_width=True)
        st.button("🚪", help="Openable / Casement", use_container_width=True)
        st.button("↔️", help="Sliding Tracks", use_container_width=True)
        st.button("🎨", help="Profile Colors", use_container_width=True)

    # CAD Drawing inside Grid Background Canvas
    with col_canvas:
        st.markdown('<div class="cad-canvas-bg">', unsafe_allow_html=True)
        cad_img = generate_window_cad(win['width'], win['height'], win['type'])
        st.image(cad_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.caption("📐 Bottom Floor Aperture Distance = 900mm")

    # Side Edit Drawer Form
    with col_config:
        st.markdown("##### **Edit Properties**")
        with st.form(f"canvas_edit_form_{index}"):
            w_code = st.text_input("Design Ref *", value=win["code"])
            w_qty = st.number_input("Quantity *", min_value=1, value=win["qty"])
            w_location = st.text_input("Location", value=win["location"])
            
            w_type = st.selectbox(
                "Opening Type", 
                ["Fixed Glass", "2 Track Sliding", "Single Sash Casement", "Double Sash Casement"],
                index=["Fixed Glass", "2 Track Sliding", "Single Sash Casement", "Double Sash Casement"].index(win["type"]) if win["type"] in ["Fixed Glass", "2 Track Sliding", "Single Sash Casement", "Double Sash Casement"] else 0
            )
            
            c1, c2 = st.columns(2)
            with c1:
                w_width = st.number_input("Width (mm)", min_value=100, max_value=5000, value=win["width"])
            with c2:
                w_height = st.number_input("Height (mm)", min_value=100, max_value=5000, value=win["height"])

            w_glass = st.text_input("Selected Glass", value=win["glass"])
            w_price = st.number_input("Total Price (₹)", value=float(win["price"]))

            st.markdown("<br>", unsafe_allow_html=True)
            btn_save = st.form_submit_button("Apply Changes", type="primary", use_container_width=True)

            if btn_save:
                st.session_state["window_designs"][index] = {
                    "code": w_code,
                    "qty": w_qty,
                    "location": w_location,
                    "series": win.get("series", "KOMMERLING SYSTEM"),
                    "glass": w_glass,
                    "color": win.get("color", "WHITE"),
                    "width": w_width,
                    "height": w_height,
                    "type": w_type,
                    "price": w_price
                }
                st.toast("✅ Design changes applied successfully!")
                st.rerun()


def render_design_tab():
    """Renders the Window CAD Grid & Configurator Tab."""
    
    # Sub Toolbar
    st.markdown("<br>", unsafe_allow_html=True)
    tb1, tb2, tb3 = st.columns([1.5, 3, 1.5])
    
    with tb1:
        with st.popover("➕ Create New Design", use_container_width=True):
            st.markdown("#### **Window Configurator**")
            w_code = st.text_input("Window Code", f"W{len(st.session_state['window_designs'])+1}")
            w_type = st.selectbox("Type", ["Fixed Glass", "2 Track Sliding", "Single Sash Casement", "Double Sash Casement"])
            w_width = st.number_input("Width (MM)", min_value=200, max_value=5000, value=1200)
            w_height = st.number_input("Height (MM)", min_value=200, max_value=5000, value=1500)
            w_location = st.text_input("Location", "SECOND FLOOR")
            w_series = st.selectbox("Series", ["KOMMERLING SYSTEM", "KOMMERLING GOLD", "PROVENT CASEMENT"])
            w_glass = st.text_input("Glass Spec", "6 MM CLEAR TOUGHENED GLASS")
            w_rate_sqft = st.number_input("Rate per Sq.Ft (₹)", value=450)

            if st.button("Add Design to Project", type="primary", use_container_width=True):
                sqft = (w_width * w_height) / 92903.04
                calc_price = round(sqft * w_rate_sqft, 2)
                st.session_state["window_designs"].append({
                    "code": w_code,
                    "qty": 1,
                    "location": w_location,
                    "series": w_series,
                    "glass": w_glass,
                    "color": "WHITE",
                    "width": w_width,
                    "height": w_height,
                    "type": w_type,
                    "price": calc_price
                })
                st.toast(f"Design {w_code} Added Successfully!", icon="✅")
                st.rerun()

    with tb2:
        search_query = st.text_input("Search Designs...", placeholder="Search by Window Code, Glass, Location...", label_visibility="collapsed")

    with tb3:
        filter_series = st.selectbox("Filter Series", ["All Series", "KOMMERLING SYSTEM", "KOMMERLING GOLD", "PROVENT CASEMENT"], label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)

    designs = st.session_state["window_designs"]
    filtered_designs = [
        d for d in designs 
        if (search_query.lower() in d["code"].lower() or search_query.lower() in d["glass"].lower() or search_query.lower() in d["location"].lower())
        and (filter_series == "All Series" or filter_series in d["series"])
    ]

    if not filtered_designs:
        st.warning("No window designs found. Click '➕ Create New Design' to add one.")
        return

    # Render Cards Grid
    cards_per_row = 4
    for i in range(0, len(filtered_designs), cards_per_row):
        cols = st.columns(cards_per_row)
        for j, win in enumerate(filtered_designs[i:i+cards_per_row]):
            original_index = designs.index(win)
            with cols[j]:
                st.markdown(f"""
                    <div class="win-card">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="win-title">{win['code']}</span>
                            <span style="font-size:12px; font-weight:bold;">Qty : {win['qty']}</span>
                        </div>
                """, unsafe_allow_html=True)

                cad_img = generate_window_cad(win['width'], win['height'], win['type'])
                st.image(cad_img, use_container_width=True)

                st.markdown(f"""
                        <div class="win-meta"><b>Location :</b> {win['location']}</div>
                        <div class="win-meta"><b>Series :</b> {win['series']}</div>
                        <div class="win-meta" style="margin-bottom:8px;"><b>Glass :</b> {win['glass']} 
                            <span class="win-tag">{win.get('color', 'WHITE')}</span>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; border-top:1px solid #f1f5f9; padding-top:8px;">
                            <span class="win-price">₹{win['price']:,.2f}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                b1, b2 = st.columns(2)
                with b1:
                    if st.button("✏️ Edit Design", key=f"edit_{original_index}", use_container_width=True):
                        edit_window_canvas_dialog(original_index)
                with b2:
                    if st.button("🗑️ Delete", key=f"del_{original_index}", use_container_width=True):
                        st.session_state["window_designs"].pop(original_index)
                        st.rerun()
