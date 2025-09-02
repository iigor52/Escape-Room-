import streamlit as st
from urllib.parse import unquote

st.set_page_config(page_title="ICU Escape Room", layout="wide")
st.title("ICU Escape Room – Hub")

st.markdown("Open sidebar (Pages) or scan a QR code that deep-links to a station.")

# Optional: handle deep-link via ?page=Station%2001
params = st.query_params
if "page" in params:
    target = unquote(params["page"])
    try:
        st.switch_page(f"pages/{target}.py")
    except Exception:
        st.warning(f"Page '{target}' not found. Use the sidebar.")
