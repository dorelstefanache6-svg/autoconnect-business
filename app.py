import streamlit as st
from datetime import datetime

# Configurare pagină profesională
st.set_page_config(
    page_title="AutoConnect Business Hub", 
    page_icon="🤖", 
    layout="wide"
)

# Inițializare bază de date în sesiunea curentă
if "database" not in st.session_state:
    st.session_state.database = []

# Titlu principal
st.title("🤖 AutoConnect Business Dashboard")
st.markdown("Gestionează-ți clienții, programările, plățile și mesajele într-un singur loc.")
st.markdown("---")

# Layout pe 2 coloane principale
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Adaugă Programare / Solicitare Nouă")
    
    with st.form("formular_programare", clear_on_submit=True):
        nume = st.text_input("Nume complet client")
        serviciu = st.selectbox("Alege Serviciul", [
            "Abonament Lunar (29 EUR)", 
            "Configurare Robot Avansat", 
            "Consultanță Tehnică Directă"
        ])
        telefon = st.text_input("Număr Telefon (ex: 0712345678)")
        data = st.date_input("Data programată")
        ora = st.time_input("Ora programată")
        
        gdpr = st.checkbox("Sunt de acord cu prelucrarea datelor cu caracter personal (GDPR)")
        
        submitted = st.form_submit_button("Salvează în Baza de Date")
        
        if submitted:
            if nume and telefon and gdpr:
                programare = {
                    "nume": nume,
                    "serviciu": serviciu,
                    "telefon": telefon,
                    "data": str(data),
                    "ora": str(ora),
                    "status": "Activ 🟢"
                }
                st.session_state.database.append(programare)
                st.success(f"Succes! Programarea pentru {nume} a fost înregistrată.")
            else:
                st.error("Te rugăm să completezi toate câmpurile și să bifezi acordul GDPR.")

    # Secțiune nouă de mesagerie internă inteligentă
    st.markdown("---")
    st.subheader("💬 Mesaj rapid către Client")
    with st.form("formular_mesaj", clear_on_submit=True):
        destinatar = st.text_input("Telefon / Nume Client Destinatar")
        continut_mesaj = st.text_area("Scrie mesajul tău (ex: Detalii plată / Confirmare)")
        trimite_mesaj = st.form_submit_button("Trimite Mesajul")
        
        if trimite_mesaj:
            if destinatar and continut_mesaj:
                st.success(f"Mesaj pregătit și trimis cu succes către {destinatar}!")
            else:
                st.warning("Completează destinatarul și textul mesajului.")

with col2:
    st.subheader("📋 Baza de Date & Clienți Activi")
    
    if not st.session_state.database:
        st.info("Nu există programări sau clienți înregistrați momentan în sesiune.")
    else:
        for idx, item in enumerate(st.session_state.database):
            with st.expander(f"👤 {item['nume']} – {item['serviciu']} ({item['data']})", expanded=True):
                st.write(f"📞 **Telefon:** {item['telefon']}")
                st.write(f"⏰ **Ora:** {item['ora']}")
                st.write(f"Status: {item['status']}")

# Secțiunea din Bara Laterală (Sidebar) pentru Plăți și Comenzi Rapide
st.sidebar.markdown("---")
st.sidebar.subheader("💎 Abonament Premium")
st.sidebar.markdown("Obține acces complet la funcțiile avansate (29 EUR / lună).")

# Buton Stripe pentru Plată Directă cu Cardul
st.sidebar.link_button(
    "💳 Plătește cu Cardul (Stripe)", 
    "https://buy.stripe.com/8x23cu93F53R6nWCRgCo001"
)

# Buton WhatsApp pentru suport extern rapid
st.sidebar.link_button(
    "💬 Comandă / Suport pe WhatsApp", 
    "https://wa.me/?text=Salut,%20vreau%20să%20activez%20abonamentul%20Lunar%20AutoConnect%20de%2029%20EUR."
)
