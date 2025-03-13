import re
import random
import string
import streamlit as st

# ✅ Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    emoji = ""

    blacklist = {"password", "123456", "password123", "qwerty", "abc123"}
    if password.lower() in blacklist:
        return "❌ Very Weak - Commonly used password! 😞", 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include a special character (!@#$%^&*).")

    if score == 4:
        emoji = "😃"
        return f"✅ Strong Password! {emoji}", score
    elif score == 3:
        emoji = "😐"
        return f"⚠️ Moderate - Add more security. {emoji}", score
    else:
        return "\n".join(feedback) + " 😞", score

# ✅ Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# ✅ Function to generate a passphrase
def generate_passphrase(num_words=4):
    wordlist = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "theta", "lambda", "omega", "sigma", "tau", "kappa"]
    return " ".join(random.sample(wordlist, num_words))

# ✅ Streamlit UI
def main():
    st.set_page_config(page_title="Password Strength Meter", layout="centered")

    # ✅ Apply Custom CSS
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #546E7A, #90A4AE) !important;
                color: white !important;
            }
            [data-testid="stSidebar"] {
                background-color: #CFD8DC !important;
            }
            [data-testid="stSidebarNav"] div {
                color: black !important;
                font-size: 18px !important;
                font-weight: bold;
            }
            [data-testid="stSidebarNav"]::before {
                content: "🔹 Menu";
                display: block;
                font-size: 20px;
                font-weight: bold;
                color: black;
                padding: 10px;
                text-align: center;
            }
            header[data-testid="stHeader"] {
                background-color: #CFD8DC;
                padding: 10px;
                border-radius: 5px;
            }
            header[data-testid="stHeader"] h1 {
                color: black !important;
                text-align: center;
            }
            .stButton button {
                background-color: #607D8B;
                color: white;
                border-radius: 8px;
                padding: 8px 15px;
                font-weight: bold;
                transition: background-color 0.3s ease-in-out;
            }
            .stButton button:hover {
                background-color: #455A64;
            }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Sidebar Menu
    menu = st.sidebar.radio("🔹 Menu", ["Check Password Strength", "Generate Password", "Generate Passphrase"], index=0)

    if menu == "Check Password Strength":
        st.title("🔐 Password Strength Meter")

        password = st.text_input("Enter your password:", type="password")

        if st.button("Check Strength"):
            if password:
                feedback, score = check_password_strength(password)
                st.markdown(f"<div style='background-color:#1976D2; padding:10px; border-radius:5px; color:white; text-align:center; font-weight:bold;'>{feedback}</div>", unsafe_allow_html=True)
                st.progress(score / 4)

    elif menu == "Generate Password":
        st.subheader("Generate a Strong Password")
        length = st.slider("Select password length", min_value=8, max_value=20, value=12)

        if st.button("Generate Strong Password"):
            strong_password = generate_strong_password(length)
            st.session_state.generated_password = strong_password

        if "generated_password" in st.session_state:
            st.text_input("Copy the password manually:", value=st.session_state.generated_password)
            st.success("✅ You can copy the password from the text box above!")

    elif menu == "Generate Passphrase":
        st.subheader("🔑 Generate a Secure Passphrase")
        num_words = st.slider("Select number of words", min_value=3, max_value=6, value=4)

        if st.button("Generate Passphrase"):
            passphrase = generate_passphrase(num_words)
            st.session_state.generated_passphrase = passphrase

        if "generated_passphrase" in st.session_state:
            st.text_input("Copy the passphrase manually:", value=st.session_state.generated_passphrase)
            st.success("✅ You can copy the passphrase from the text box above!")

if __name__ == "__main__":
    main()
