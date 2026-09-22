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
# TRAININGEN OPSLAAN
# -----------------------------

if "trainingen" not in st.session_state:
    st.session_state.trainingen = []

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

# -----------------------------
# TRAINING OPSLAAN
# -----------------------------

if st.button("🥊 Training opslaan"):

    training = {
        "datum": str(datum),
        "type": training_type,
        "duur": duur,
        "intensiteit": intensiteit,
        "onderdelen": onderdelen,
        "notitie": notitie
    }

    st.session_state.trainingen.append(training)

    st.success("✅ Training succesvol opgeslagen!")

st.divider()

# -----------------------------
# VOORTGANG
# -----------------------------

st.header("📊 Mijn voortgang")

# Aantal trainingen berekenen
aantal_trainingen = len(st.session_state.trainingen)

# Alle trainingsminuten bij elkaar optellen
trainingsminuten = sum(
    training["duur"]
    for training in st.session_state.trainingen
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🥊 Trainingen",
        aantal_trainingen
    )

with col2:
    st.metric(
        "⏱️ Trainingsminuten",
        trainingsminuten
    )

# -----------------------------
# OPGESLAGEN TRAININGEN
# -----------------------------

st.divider()

st.header("📋 Mijn trainingen")

if len(st.session_state.trainingen) == 0:

    st.info(
        "Je hebt nog geen trainingen opgeslagen."
    )

else:

    for i, training in enumerate(
        reversed(st.session_state.trainingen),
        start=1
    ):

        with st.expander(
            f"🥊 {training['type']} - {training['datum']}"
        ):

            st.write(
                f"**Duur:** {training['duur']} minuten"
            )

            st.write(
                f"**Intensiteit:** "
                f"{training['intensiteit']}/10"
            )

            if training["onderdelen"]:
                st.write(
                    f"**Onderdelen:** "
                    f"{', '.join(training['onderdelen'])}"
                )

            if training["notitie"]:
                st.write(
                    f"**Notitie:** {training['notitie']}"
                )

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
    placeholder=(
        "Bijvoorbeeld: Waar moet ik de komende "
        "weken aan werken?"
    )
)

if st.button("💬 Vraag aan AI Coach"):

    if not vraag:

        st.warning(
            "Vul eerst een vraag in."
        )

    else:

        with st.spinner(
            "AI Coach denkt na..."
        ):

            response = client.responses.create(
                model="gpt-5-mini",

                instructions=(
                    "Je bent de FightTrack AI Coach. "
                    "Je helpt kickboksers met training, "
                    "techniek, conditie, herstel en "
                    "trainingsplanning. "
                    "Geef praktische en duidelijke "
                    "antwoorden. "
                    "Geef geen medische diagnoses."
                ),

                input=vraag
            )

            antwoord = response.output_text

        st.success("🥊 AI Coach")

        st.write(antwoord)

st.divider()

# -----------------------------
# EXTRA INFORMATIE
# -----------------------------

st.info(
    "💡 Je trainingen worden tijdens deze sessie "
    "bijgehouden. Trainingsaantallen en minuten "
    "worden automatisch berekend."
)
