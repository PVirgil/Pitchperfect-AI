# streamlit_app.py

import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from groq import Groq
import logging

# Setup
logging.basicConfig(level=logging.INFO)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# Helper

def call_llm(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a professional pitch deck generator and startup strategist."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Modules

def generate_pitch_deck(df: pd.DataFrame, founder_name: str) -> str:
    columns = list(df.columns)
    prompt = (
        f"Founder: {founder_name}. This is their startup data with columns {columns}.\n"
        "Generate a complete investor-ready pitch deck summary with the following sections: Problem, Solution, Market, Product, Business Model, Traction, Team, Financials, Ask.\n"
        "Use clear, professional language."
    )
    return call_llm(prompt)

def generate_one_pager(df: pd.DataFrame, founder_name: str) -> str:
    prompt = (
        f"Create a one-pager startup summary for founder {founder_name} using this dataset with columns {list(df.columns)}.\n"
        "Include company name, vision, traction metrics, team summary, and funding ask."
    )
    return call_llm(prompt)

def simulate_investor_qa(question: str, founder_name: str) -> str:
    prompt = (
        f"A VC asks the startup founder ({founder_name}): {question}\n"
        "Respond with a concise, confident answer based on typical early-stage startup logic."
    )
    return call_llm(prompt)

# Streamlit UI

def main():
    st.set_page_config("PitchPerfect AI", page_icon="🎤", layout="wide")
    st.title("🎤 PitchPerfect AI")
    st.write("Upload your startup data. Get your pitch deck, one-pager, and investor Q&A — instantly.")

    founder = st.text_input("Your name (for personalization)")
    uploaded_file = st.file_uploader("Upload startup metrics CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Data uploaded!")
    else:
        df = pd.DataFrame()

    tab1, tab2, tab3 = st.tabs(["📊 Pitch Deck", "🧾 One-Pager", "💬 Investor Q&A"])

    with tab1:
        st.subheader("📊 Generate Pitch Deck Summary")
        if st.button("Generate Deck"):
            if df.empty:
                st.error("Upload data first.")
            else:
                output = generate_pitch_deck(df, founder or "Founder")
                st.text_area("Pitch Deck Output", value=output, height=400)

    with tab2:
        st.subheader("🧾 One-Pager Summary")
        if st.button("Generate One-Pager"):
            if df.empty:
                st.error("Upload data first.")
            else:
                output = generate_one_pager(df, founder or "Founder")
                st.text_area("One-Pager", value=output, height=400)

    with tab3:
        st.subheader("💬 Simulate Investor Questions")
        user_q = st.text_input("Ask an investor-style question")
        if st.button("Answer"):
            if not user_q:
                st.error("Enter a question.")
            else:
                response = simulate_investor_qa(user_q, founder or "Founder")
                st.markdown(f"**AI:** {response}")

if __name__ == "__main__":
    main()
