# Edit Plan: Schwierigere Fragen für Fachinformatiker Systemintegration generieren

## Information Gathered
- **Project Structure**: Streamlit quiz app (`app.py`) lädt `questions.json` mit Block 'AP02_Pruefung_Block1' (50 einfache MC-Fragen zu Netzwerken, Sicherheit, Virtualisierung, ITIL).
- **Fragen-Format**: JSON-Objekt mit Arrays pro Block: `[{question: str, options: [str,str,str,str], correct: int (0-3)}]`.
- **Aktuelle Fragen**: Basiswissen (DHCP, TCP/UDP, VLAN, RAID, Docker basics). App zeigt zufällige Fragen, trackt Score/Zeit.
- **TODO.md**: Besteht, aber nicht relevant (Timer-Fertig).
- **Keine anderen relevanten Dateien** (requirements.txt hat Streamlit, kein Impact).

## Plan
1. **Neuen Block erstellen**: Füge 'AP02_Pruefung_Block2_Schwer' mit 25 schwierigen Fragen hinzu (nicht überschreiben!).
   - Themen: Erweiterte Netzwerke (OSPF, BGP, SDN), AD/Group Policy, Linux (systemd, SELinux), Cloud-Integration (Azure AD Connect), Kubernetes (Pods/Services), SIEM/IDS, PowerShell scripting, komplexe Troubleshooting-Szenarien.
   - Schwierigkeit: Prüfungs-nah (Szenarien, Fehlersuche, Konfigurationen, Vergleiche).
   - Format: Identisch (4 Optionen, 1 korrekt).
2. **questions.json erweitern** mit `edit_file` oder neuer `create_file` (backup zuerst?).
3. **App.py anpassen** (optional): Sidebar zum Block-Wechsel (Fach/Block1/Block2_Schwer).

## Dependent Files to be edited
- `questions.json` (Hauptänderung: Neuer Block hinzufügen).
- Optional: `app.py` (Multi-Block-Support für Sidebar-Auswahl).

## Followup steps
- Test: `streamlit run app.py`, prüfe neue Fragen (nach App-Anpassung).
- Validierung: JSON gültig, App lädt ohne Error.
- README.md erweitern mit neuen Blöcken.
- TODO.md: Neuen Eintrag für App-Erweiterung.
