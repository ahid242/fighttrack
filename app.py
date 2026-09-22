import streamlit as st
from openai import OpenAI

# -----------------------------
# PAGINA INSTELLEN
# -----------------------------

st.set_page_config(
    page_title="FightTrack",
    page_icon="🥊",
    layout="centered"
)

# -----------------------------
# OPENAI
# -----------------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# -----------------------------
# TITEL
# -----------------------------

st.title("🥊 FightTrack")
st.subheader("Jouw persoonlijke kickboks-tracker")

st.write(
    "Houd je trainingen bij en krijg persoonlijke "
    "tips van de FightTrack AI Coach."
)

st.divider()

# -----------------------------
# TRAINING TOEVOEGEN
# -----------------------------

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

    if onderdelen:
        st.write(
            f"**Onderdelen:** {', '.join(onderdelen)}"
        )

    if notitie:
        st.write(f"**Notitie:** {notitie}")

st.divider()

# -----------------------------
# AI COACH
# -----------------------------

st.header("🤖 FightTrack AI Coach")

st.write(
    "Stel een vraag over je kickbokstraining."
)

vraag = st.text_input(
    "Jouw vraag",
    placeholder="Bijvoorbeeld: Waar moet ik de komende weken aan werken?"
)

if st.button("💬 Vraag aan AI Coach"):

    if not vraag:
        st.warning("Vul eerst een vraag in.")
    else:

        with st.spinner("AI Coach denkt na..."):

            response = client.responses.create(
                model="gpt-5-mini",
                instructions=(
                    "Je bent de FightTrack AI Coach. "
                    "Je helpt kickboksers met training, techniek, "
                    "conditie, herstel en trainingsplanning. "
                    "Geef praktische en duidelijke antwoorden. "
                    "Geef geen medische diagnoses."
                ),
                input=vraag
            )

            antwoord = response.output_text

        st.success("🥊 AI Coach")
        st.write(antwoord)

st.divider()

# -----------------------------
# VOORTGANG
# -----------------------------

st.header("📊 Mijn voortgang")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Trainingen",
        "0"
    )

with col2:
    st.metric(
        "Trainingsminuten",
        "0"
    )

st.info(
    "💡 Meer trainingsdata en persoonlijke statistieken "
    "worden later toegevoegd."
)
