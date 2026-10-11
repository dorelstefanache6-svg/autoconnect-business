import streamlit as st
import sqlite3
import datetime

DB_NAME = "autoconnect_legal.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            date_time TEXT NOT NULL,
            gdpr_consent INTEGER NOT NULL,
            status TEXT DEFAULT 'În așteptare 🟡'
        )
    ''')
    conn.commit()
    conn.close()

def add_appointment(client_name, phone, service, date_time, gdpr):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (client_name, phone, service, date_time, gdpr_consent, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (client_name, phone, service, date_time, gdpr, 'În așteptare 🟡'))
    conn.commit()
    conn.close()

def get_appointments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT client_name, service, date_time, status FROM appointments')
    rows = cursor.fetchall()
    conn.close()
    return rows

init_db()

st.set_page_config(page_title="AutoConnect Business - Legal & Secure", layout="wide")

st.title("🛡️ AutoConnect Business - Panou de Gestiune Clienți")
st.markdown("Soluția ta sigură, legală și automatizată pentru afaceri locale.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Adaugă Client & Programare Nouă")
    client_name = st.text_input("Nume complet client")
    phone = st.text_input("Număr de telefon (ex: +407...)")
    service = st.text_input("Serviciul programat (ex: Revizie / Consultație)")
    
    app_date = st.date_input("Data programării")
    app_time = st.time_input("Ora programării")
    
    gdpr_check = st.checkbox("Clientul și-a dat acordul (GDPR) pentru primirea notificărilor automate prin SMS/WhatsApp.")
    
    if st.button("Salvează în Baza de Date"):
        if client_name and phone and service:
            if gdpr_check:
                date_time_str = f"{app_date} {app_time}"
                add_appointment(client_name, phone, service, date_time_str, 1)
                st.success(f"Programare salvată în siguranță pentru {client_name}!")
                st.rerun()
            else:
                st.warning("Eroare legală: Trebuie să bifezi acordul GDPR al clientului înainte de a salva.")
        else:
            st.error("Te rugăm să completezi toate câmpurile obligatorii.")

with col2:
    st.subheader("📋 Programări Salvate în Bază")
    data = get_appointments()
    
    if data:
        for idx, row in enumerate(data):
            st.info(f"**{row[0]}** — *{row[1]}* la data de {row[2]} | Status: {row[3]}")
    else:
        st.write("Nu există programări înregistrate momentan.")

st.markdown("---")
st.caption("AutoConnect Business v1.0 — Toate drepturile rezervate.")