import streamlit as st
from PIL import Image

# Option scores
option_scores = {1: 5.0, 2: 2.5, 3: -2.5}

# Situations dictionary
situations = {
    1: {
        "text": "📍 Situation 1: A tweet from a former employee goes viral, accusing the company of unethical practices.",
        "image": "A.png",
        "options": {
            1: ("Issue a public statement", "A1.png"),
            2: ("Privately reach out to the accuser", "A2.png"),
            3: ("Remain silent for now", "A3.png")
        },
        "threshold": 5.0
    },
    2: {
        "text": "📍 Situation 2: A major news outlet is planning to release an article on the controversy.",
        "image": "B.png",
        "options": {
            1: ("Give an exclusive interview", "B1.png"),
            2: ("Send a prepared press release", "B2.png"),
            3: ("Deny all allegations", "B3.png")
        },
        "threshold": 10.0
    },
    3: {
        "text": "📍 Situation 3: Customers start demanding answers on social media.",
        "image": "C.png",
        "options": {
            1: ("Hold a press conference", "C1.png"),
            2: ("Do a live Q&A on Instagram", "C2.png"),
            3: ("Send internal communication only", "C3.png")
        },
        "threshold": 15.0
    }
}

# Initialize session state
if "situation" not in st.session_state:
    st.session_state.situation = 0
    st.session_state.score = 0.0
    st.session_state.choices = 0

def show_intro():
    st.image("intro.png")
    st.title("🎮 Welcome to the PR Crisis Simulator")
    st.write("Make choices to handle escalating PR issues. Try to meet the score threshold for each situation.")
    if st.button("▶️ Start Game"):
        st.session_state.situation = 1

def display_situation(sit_num):
    situation = situations[sit_num]
    st.header(situation["text"])
    st.image(situation["image"])
    st.info(f"🎯 Score Required: {situation['threshold']} pts")
    st.warning(f"📊 Your Score: {st.session_state.score:.1f} pts")

    for opt_num, (label, img_file) in situation["options"].items():
        if st.button(f"{opt_num}. {label}"):
            process_choice(sit_num, opt_num, label, img_file)

def process_choice(sit_num, opt_num, label, img_file):
    points = option_scores[opt_num]
    st.session_state.score += points
    st.session_state.choices += 1

    st.image(img_file, caption=label)
    st.markdown(f"🧮 Points earned: `{points:+.1f}`")
    st.markdown(f"📊 Updated Score: `{st.session_state.score:.1f}`")

    if st.session_state.score >= situations[sit_num]["threshold"]:
        st.success("✅ You've met the required score!")
        st.session_state.situation += 1
    else:
        st.error("⚠️ Not enough points. Try a different option.")

def show_final_result():
    st.image("conclusion.png")
    st.title("🎉 Game Over - PR Crisis Managed")
    st.write(f"🏁 Final Score: {st.session_state.score:.1f}")
    st.write(f"🎲 Total Choices: {st.session_state.choices}")
    st.success("🏅 Grade: Amazing" if st.session_state.choices <= 3 else "👍 Grade: Keep it up")

    st.markdown("### 🗺 Recommended Strategy")
    st.markdown("✔️ Situation 1: Option 1")
    st.markdown("✔️ Situation 2: Option 1")
    st.markdown("✔️ Situation 3: Option 1")

    if st.button("🔁 Play Again"):
        st.session_state.situation = 0
        st.session_state.score = 0.0
        st.session_state.choices = 0

# Main logic
if st.session_state.situation == 0:
    show_intro()
elif st.session_state.situation > len(situations):
    show_final_result()
else:
    display_situation(st.session_state.situation)
