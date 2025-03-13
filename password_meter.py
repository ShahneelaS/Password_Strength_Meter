import re
import random
import string
import streamlit as st
import pyperclip

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

    # ✅ Custom CSS for Sidebar & UI Fixes
    st.markdown("""
       <style>
    /* ✅ Sidebar - Light Greyish-Blue Background */
    [data-testid="stSidebar"] {
        background-color: #CFD8DC !important;
        color: black !important;
    }
    [data-testid="stSidebarNav"] div {
        color: black !important;
        font-size: 18px !important;
        font-weight: bold;
    }

    /* ✅ Sidebar Heading */
    [data-testid="stSidebarNav"]::before {
        content: "🔹 Menu";
        display: block;
        font-size: 20px;
        font-weight: bold;
        color: black;
        padding: 10px;
        text-align: center;
    }

    /* ✅ Header - Light Greyish-Blue Background */
    header[data-testid="stHeader"] {
        background-color: #CFD8DC;
        padding: 10px;
        border-radius: 5px;
    }
    header[data-testid="stHeader"] h1 {
        color: black !important;
        text-align: center;
    }

    /* ✅ Center App - Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #546E7A, #90A4AE);
        color: white;
    }

    /* ✅ Input Fields */
    .stTextInput label, .stButton button, .stSlider label {
        color: white !important;
    }
    .stTextInput input {
        background-color: #546E7A;
        color: white;
        border: 1px solid #90A4AE;
    }

    /* ✅ Buttons - Soft Blue with a darker hover effect (No Change) */
    .stButton button {
        background-color: #607D8B;  /* Soft Blue */
        color: white;
        border-radius: 8px;
        padding: 8px 15px;
        font-weight: bold;
        transition: background-color 0.3s ease-in-out;
    }
    .stButton button:hover {
        background-color: #455A64;  /* Darker Blue */
    }

    /* ✅ Error/Warning Messages - Deep Red */
    .stError {
        background-color: #B71C1C;  /* Deep Red */
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }

    /* ✅ Success Messages - Royal Blue (No Green) */
    .stSuccess {
        background-color: #1976D2;  /* Royal Blue */
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }

    /* ✅ Copied Successfully Alert - Dark Navy Blue */
    .stClipboardSuccess, .stPasswordCopied {
        background-color: #0D47A1;  /* Dark Navy Blue */
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
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
                st.markdown(f"<div class='stSuccess'>{feedback}</div>", unsafe_allow_html=True)
                st.progress(score / 4)

    elif menu == "Generate Password":
        st.subheader("Generate a Strong Password")
        length = st.slider("Select password length", min_value=8, max_value=20, value=12)

        if st.button("Generate Strong Password"):
            strong_password = generate_strong_password(length)
            st.session_state.generated_password = strong_password

        if "generated_password" in st.session_state:
            st.markdown(f"<div class='stSuccess'>🔑 Suggested Strong Password: `{st.session_state.generated_password}`</div>", unsafe_allow_html=True)

            # ✅ Copy Button
            if st.button("Copy to Clipboard"):
                pyperclip.copy(st.session_state.generated_password)
                st.session_state.copied = True

            if st.session_state.get("copied", False):
                st.success("✅ Password copied successfully!")

    elif menu == "Generate Passphrase":
        st.subheader("🔑 Generate a Secure Passphrase")
        num_words = st.slider("Select number of words", min_value=3, max_value=6, value=4)

        if st.button("Generate Passphrase"):
            passphrase = generate_passphrase(num_words)
            st.session_state.generated_passphrase = passphrase

        if "generated_passphrase" in st.session_state:
            st.markdown(f"<div class='stSuccess'>🔑 Secure Passphrase: `{st.session_state.generated_passphrase}`</div>", unsafe_allow_html=True)

            # ✅ Copy Button
            if st.button("Copy Passphrase"):
                pyperclip.copy(st.session_state.generated_passphrase)
                st.session_state.copied_phrase = True

            if st.session_state.get("copied_phrase", False):
                st.success("✅ Passphrase copied successfully!")

if __name__ == "__main__":
    main()
