import streamlit as st

st.set_page_config(
    page_title="FightTrack",
    page_icon="🥊",
    layout="centered"
)

st.title("🥊 FightTrack")
st.subheader("Jouw persoonlijke kickboks-tracker")

st.write(
    "Houd je trainingen bij, bekijk je voortgang "
    "en ontdek waar je jezelf kunt verbeteren."
)

st.divider()

st.header("➕ Training toevoegen")

datum = st.date_input("Datum")

training_type = st.selectbox(
    "Type training",
    [
        "Techniek",
        "Conditie",
        "Sparren",
        "Zaktraining",
        "Krachttraining"
    ]
)

duur = st.number_input(
    "Duur van de training (minuten)",
    min_value=1,
    max_value=300,
    value=60
)

intensiteit = st.slider(
    "Intensiteit",
    min_value=1,
    max_value=10,
    value=5
)

onderdelen = st.multiselect(
    "Wat heb je getraind?",
    [
        "Stoten",
        "Trappen",
        "Combinaties",
        "Verdediging",
        "Voetenwerk",
        "Conditie",
        "Sparren"
    ]
)

notitie = st.text_area(
    "Notitie over je training"
)

if st.button("🥊 Training opslaan"):
    st.success("Training opgeslagen!")
    
    st.write("### Training")
    st.write(f"**Datum:** {datum}")
    st.write(f"**Type:** {training_type}")
    st.write(f"**Duur:** {duur} minuten")
    st.write(f"**Intensiteit:** {intensiteit}/10")
    st.write(
        f"**Onderdelen:** {', '.join(onderdelen) if onderdelen else 'Geen'}"
    )
    
    if notitie:
        st.write(f"**Notitie:** {notitie}")

st.divider()

st.header("📊 Mijn voortgang")

col1, col2 = st.columns(2)

with col1:
    st.metric("Trainingen", "0")

with col2:
    st.metric("Trainingsminuten", "0")

st.info(
    "💡 Binnenkort kun je hier je volledige trainingsgeschiedenis "
    "en persoonlijke AI-adviezen bekijken."
)
