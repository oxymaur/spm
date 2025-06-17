# 🧠 SPM Quiz App

This is an interactive quiz application to prepare for Sourcing Management module.  
Built with [Streamlit](https://streamlit.io/), it supports both:

- ✅ Multiple Choice Questions (with single or multiple correct answers)
- 🔀 Drag & Drop Order Questions (e.g. process steps, models, etc.)

---

## 📁 Project Structure

```
SPM-quizz-v2/
├── quiz.py                  ← Main Streamlit app
├── welcome.py               ← Welcome screen with leaderboard
├── questions/
│   ├── questions_db.json    ← Your full question pool
│   └── scores.json          ← Stores quiz results
├── ui/
│   ├── styles.py            ← Visual style constants
├── utils/
│   └── data.py              ← JSON load/save helpers
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourname/SPM-quizz-v2.git
cd SPM-quizz-v2
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/Scripts/activate       # Windows
# or
source venv/bin/activate           # macOS/Linux
```

### 3. Install dependencies

```bash
pip install streamlit
```

### 4. Run the app

```bash
streamlit run quiz.py
```

---

## 📊 Features

- 🎯 18 randomly selected multiple choice questions
- 🔄 2 randomly selected ordering questions
- 💾 High score tracking (saved in `scores.json`)
- 🧑 Name entry & leaderboard

---

## 🛠️ Add New Questions

Add more entries in `questions/questions_db.json`. Each entry should follow this format:

### ✅ Multiple Choice Example:
```json
{
  "id": "1",
  "question": "What is the purpose of EAM?",
  "choices": {
    "a": "To reduce cost",
    "b": "To align strategy and IT",
    "c": "To write code",
    "d": "To design furniture"
  },
  "correct_answers": ["b"],
  "explanation": "EAM aligns strategy, business and IT.",
  "type": "mc"
}
```

### 🔀 Order Question Example:
```json
{
  "id": "order_sourcing_1",
  "question": "Order the phases of the Sourcing Strategy",
  "choices": {
    "items": [
      "Analyse Ist-Situation",
      "Definition Ziele",
      "Evaluation Optionen",
      "Umsetzungsplanung"
    ]
  },
  "correct_order": [
    "Analyse Ist-Situation",
    "Definition Ziele",
    "Evaluation Optionen",
    "Umsetzungsplanung"
  ],
  "type": "order",
  "explanation": "This is the classic 4-step sourcing approach."
}
```

---

## 📚 Requirements

- Python 3.8+
- [Streamlit](https://docs.streamlit.io/) (`pip install streamlit`)

---

## 👨‍🎓 Author

Built by Oxymaur with ChatGPT for personal learning and exam preparation.

---

## 📝 License

This project is open-source and free to use.
