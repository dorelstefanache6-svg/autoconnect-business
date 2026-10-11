import streamlit as st
from datetime import datetime

# Configurare pagină
st.set_page_config(page_title="AutoConnect Business", page_icon="🤖", layout="wide")

# Inițializare bază de date în sesiunea curentă
if "database" not in st.session_state:
    st.session_state.database = []

# Titlu principal
st.title("🤖 AutoConnect Business Dashboard")
st.markdown("---")

# Layout pe 2 coloane
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Adaugă Programare / Solicitare")
    
    with st.form("formular_programare"):
        nume = st.text_input("Nume complet")
        serviciu = st.selectbox("Tip Serviciu", ["Abonament Lunar", "Configurare Robot", "Consultanță Tehnică"])
        telefon = st.text_input("Număr Telefon")
        data = st.date_input("Data programată")
        ora = st.time_input("Ora programată")
        
        # Opțiune GDPR
        gdpr = st.checkbox("Sunt de acord cu prelucrarea datelor cu caracter personal (GDPR)")
        
        submitted = st.form_submit_button("Salvează Programarea")
        
        if submitted:
            if nume and telefon and gdpr:
                programare = {
                    "nume": nume,
                    "serviciu": serviciu,
                    "telefon": telefon,
                    "data": str(data),
                    "ora": str(ora),
                    "status": "În așteptare 🟡"
                }
                st.session_state.database.append(programare)
                st.success(f"Programarea pentru {nume} a fost salvată cu succes!")
            else:
                st.error("Te rugăm să completezi toate câmpurile obligatorii și să bifezi acordul GDPR.")

with col2:
    st.subheader("📋 Programări Salvate în Bază")
    
    if not st.session_state.database:
        st.info("Nu există programări înregistrate momentan.")
    else:
        for idx, item in enumerate(st.session_state.database):
            with st.expander(f"👤 {item['nume']} – {item['serviciu']} ({item['data']})", expanded=True):
                st.write(f"📞 **Telefon:** {item['telefon']}")
                st.write(f"⏰ **Ora:** {item['ora']}")
                st.write(f"Status: {item['status']}")

# Secțiunea din Bara Laterală (Sidebar) pentru Abonament / Contact direct
st.sidebar.markdown("---")
st.sidebar.subheader("💎 Abonament Premium")

if st.sidebar.button("📩 Comandă / Contactează-ne"):
    st.sidebar.success("Mulțumim! Vei fi contactat în cel mai scurt timp pentru detalii.")
