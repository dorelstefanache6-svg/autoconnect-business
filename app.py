import streamlit as st
import datetime
import urllib.parse

st.set_page_config(page_title="AutoConnect Business", page_icon="🛡️", layout="wide")

st.title("🛡️ AutoConnect Business - Panou de Gestiune Clienți")
st.caption("Soluția ta sigură, legală și automatizată pentru afaceri locale.")

# Inițializare bază de date în sesiune
if "database" not in st.session_state:
    st.session_state.database = []

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Adaugă Client & Programare Nouă")
    nume = st.text_input("Nume complet client")
    telefon = st.text_input("Număr de telefon (ex: +32465525017 sau +407...)")
    serviciu = st.text_input("Serviciul programat (ex: Revizie / Consultație)")
    data_p = st.date_input("Data programării", datetime.date.today())
    ora_p = st.time_input("Ora programării", datetime.time(10, 0))
    gdpr = st.checkbox("Clientul și-a dat acordul (GDPR) pentru primirea notificărilor automate")

    if st.button("Salvează în Baza de Date"):
        if nume and telefon and serviciu and gdpr:
            # Curățare și validare număr
            tel_curat = telefon.replace(" ", "").replace("-", "")
            
            # Generare mesaj automat WhatsApp
            mesaj = f"Salut {nume}! Îți confirmăm programarea pentru {serviciu} pe data de {data_p} la ora {ora_p.strftime('%H:%M')}. Mulțumim că ai ales serviciile noastre!"
            mesaj_encoded = urllib.parse.quote(mesaj)
            
            link_wa = f"https://wa.me/{tel_curat.replace('+', '')}?text={mesaj_encoded}"

            programare = {
                "nume": nume,
                "telefon": tel_curat,
                "serviciu": serviciu,
                "data": str(data_p),
                "ora": str(ora_p),
                "link_wa": link_wa,
                "status": "În așteptare 🟡"
            }
            st.session_state.database.append(programare)
            st.success(f"Programarea pentru {nume} a fost salvată cu succes!")
        else:
            st.error("Te rugăm să completezi toate câmpurile și să bifezi acordul GDPR.")

with col2:
    st.subheader("📋 Programări Salvate în Bază")
    if not st.session_state.database:
        st.info("Nu există programări înregistrate momentan.")
    else:
        for idx, item in enumerate(st.session_state.database):
            with st.expander(f"👤 {item['nume']} — {item['serviciu']} ({item['data']})", expanded=True):
                st.write(f"📱 **Telefon:** {item['telefon']}")
                st.write(f"⏰ **Ora:** {item['ora']}")
                st.write(f"Status: {item['status']}")
                
                
st.sidebar.markdown("---")
st.sidebar.subheader("💳 Abonament Premium")
st.sidebar.link_button("💳 Plătește Abonamentul (29 EUR)", "https://buy.stripe.com/8x29ASa7JeEr9A8eZ0oco000")
