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

## 📝 Blocks verfügbar
- **AP02_Pruefung_Block1**: Basisfragen (Netzwerke, Sicherheit, Virtualisierung, ITIL) – ~47 Fragen
- **AP02_Pruefung_Block2_Schwer**: Schwierige Abschlussprüfungsfragen (25 Fragen):
  - Routing (OSPF LSA, BGP AS_PATH, ACL, SD-WAN)
  - Active Directory (GPO BitLocker, Azure AD Connect)
  - Kubernetes/Docker (Pod rescheduling, Swarm replicas)
  - Linux (systemd mount, SELinux enforcing, nftables SSH)
  - Sicherheit (SIEM Correlation, WPA3 EAP-TLS, Zero Trust)
  - Monitoring (Prometheus scrape, ELK grok)
  - Windows (DSC xWindowsFeature, SCCM Deployment, Hyper-V Live Migration)
  - VMware/ITIL (DRS Anti-Affinity, P1 Incident)

## 📝 Fragen erweitern
**questions.json** bearbeiten (Backup: questions_backup.json):
```json
{
  "NEUER_BLOCK": [
    {
      "question": "Deine Frage?",
      "options": ["A", "B", "C", "D"],
      "correct": 1  // Index 0-3
    }
  ]
}
```
App lädt neue Blocks automatisch (erweitere app.py für Auswahl).

## 🔧 Troubleshooting
- JSON Error? Validiere Syntax.
- Streamlit fehlt? `pip install streamlit`.

**Viel Erfolg bei der FISI Abschlussprüfung! 💪 Neue schwierige Fragen trainieren Block2_Schwer!**

