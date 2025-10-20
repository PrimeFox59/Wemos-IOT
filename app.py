import streamlit as st
import requests

# Konfigurasi internal
WEMOS_IP = "http://192.168.1.2"  # IP Wemos kamu
GOOGLE_API_KEY = "AIzaSyB1nFDDzDCmiS4KlK2L5njDqjnPbRAo_jA"  # Key validasi (opsional backend check)

# Fungsi kontrol LED
def led_control(action):
    try:
        r = requests.get(f"{WEMOS_IP}/led/{action}", timeout=3)
        if r.status_code == 200:
            return r.text
        else:
            return f"Error: {r.status_code}"
    except Exception as e:
        return f"Gagal terhubung ke WeMos: {e}"

# UI Streamlit
st.set_page_config(page_title="WeMos LED Control", page_icon="💡", layout="centered")

st.title("💡 IoT LED Controller - WeMos D1 Mini")
st.markdown("Kontrol LED built-in langsung dari browser.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔆 Nyalakan LED"):
        result = led_control("on")
        st.success(result)

with col2:
    if st.button("💤 Matikan LED"):
        result = led_control("off")
        st.warning(result)

# Status monitoring opsional
try:
    status = requests.get(f"{WEMOS_IP}/", timeout=3)
    st.caption(f"Terhubung ke WeMos di {WEMOS_IP}")
except:
    st.error("⚠️ Tidak bisa terhubung ke WeMos. Pastikan WiFi sama dan board sudah aktif.")
