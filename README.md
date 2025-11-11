# 🎤 PitchPerfect AI

**PitchPerfect AI** turns raw startup data into investor-ready pitch decks, one-pagers, and VC Q&A. It's a full-stack AI tool for founders, accelerators, and pitch consultants.

## 🚀 Live App
[Launch PitchPerfect AI](https://your-streamlit-link.com)

## 🧠 Features
- 📊 Upload startup data
- 🧾 Generate pitch decks & one-pagers
- 💬 Simulate VC questions and answers
- 🧠 Powered by Groq (Mixtral or LLaMA 3)
- 💻 Built with Streamlit, Python, and LLMs

## 🛠 Usage

1. Clone the repo and install:
```bash
git clone https://github.com/yourusername/pitchperfect-ai.git
cd pitchperfect-ai
pip install -r requirements.txt
```

2. Create `.env` with your Groq key:
```
GROQ_API_KEY=your_key_here
```

3. Run locally:
```bash
streamlit run streamlit_app.py
```

## ☁️ Streamlit Cloud Deployment

1. Push to GitHub  
2. Set up on [Streamlit Cloud](https://streamlit.io/cloud)  
3. Add secret in Settings > Secrets:
```toml
GROQ_API_KEY = "your_key_here"
```

---

## 📁 Structure
```
pitchperfect-ai/
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```
