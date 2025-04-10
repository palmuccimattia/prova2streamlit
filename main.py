import streamlit as st
from openai import OpenAI

# Configura la tua API key (puoi usare st.secrets per nasconderla in produzione)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def conta_negazioni_testo(testo):
    prompt = f"Conta quante negazioni contiene questo testo e scrivile come elenco: \"{testo}\""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sei un assistente che identifica negazioni in un testo."},
            {"role": "user", "content": prompt}
        ]
    )
    
    risposta = response.choices[0].message.content.strip()
    return risposta

# Interfaccia Streamlit
st.title("Contatore di Negazioni con GPT")

testo_input = st.text_area("Inserisci il testo:")

if st.button("Analizza"):
    if testo_input.strip():
        risultato = conta_negazioni_testo(testo_input)

        with open("negazioni.txt", "w") as f:
            f.write(risultato)

        st.success("Analisi completata. Scarica il file:")
        st.download_button(label="Scarica negazioni.txt", data=risultato, file_name="negazioni.txt")
    else:
        st.warning("Inserisci un testo prima di cliccare.")
