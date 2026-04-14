import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False

# Input
guess = st.number_input("Guess a number between 1 to 100", min_value=1, max_value=100, step=1)

# Button
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.tries += 1

    if guess == st.session_state.number:
        st.success(f"🎉 Congratulations! You found the number in {st.session_state.tries} tries")
        st.balloons()
        st.session_state.game_over = True
    elif guess > st.session_state.number:
        st.warning("📉 Go lower!")
    else:
        st.warning("📈 Go higher!")

# Show tries
st.write(f"### Attempts: {st.session_state.tries}")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False