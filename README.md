# 🚀 AP02 Fisi Trainer

## 📋 Features
- Zufällige Fragen aus AP02 Prüfungsblock
- Score-Tracking mit Prozentanzeige
- Sidebar: Feld wählen, neue Session
- Buttons: Prüfen, Lösung zeigen, Nächste

## 🛠️ Setup & Start
1. **Dependencies** (Streamlit):
   ```
   pip install -r requirements.txt
   ```
2. **Start App** (wichtig!):
   ```
   streamlit run app.py
   ```
   Öffnet Browser automatisch (http://localhost:8501).

❌ **Nicht**: `python app.py` (verursacht Errors!)

## 📝 Fragen erweitern
**questions.json** bearbeiten:
```json
{
  "AP02_Pruefung_Block1": [
    {
      "question": "Deine Frage?",
      "options": ["A", "B", "C", "D"],
      "correct": 1  // Index (0-3)
    }
  ]
}
```
Füge Felder hinzu, z.B. `"LF2": [...]`.

## 🔧 Troubleshooting
- KeyError? Fix JSON-Struktur.
- Streamlit not found? `pip install streamlit`.
- Mehr Felder? Sidebar passt sich an.

**Genieße das Lernen! 🎯**
