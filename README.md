
# 🦊 Zootopia Animal Web Generator

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Bootcamp](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal%20%2B%20HTML-lightgrey)

> A dynamic **API‑to‑HTML generator** built in Python.  
> Fetches animal data from the **API Ninjas Animals API** and converts it into a styled HTML website.

---

# 📌 Overview

This project demonstrates how to:

- Fetch live animal data from an external API
- Manage API keys securely using `.env`
- Process nested JSON responses safely
- Generate HTML dynamically using a template
- Separate application architecture into modules

The application follows a **clean architecture** approach where:

```
User Input
    │
    ▼
animals_web_generator.py
    │
    ▼
data_fetcher.py  →  API Ninjas
    │
    ▼
HTML Template Injection
    │
    ▼
animals.html (Generated Website)
```

---

# 🖥️ Demo Flow

1. User enters an animal name in the terminal
2. The program fetches matching animals from the **API Ninjas Animals API**
3. The response JSON is processed
4. Animal information is injected into an HTML template
5. A new webpage is generated → `animals.html`

Example:

```bash
python animals_web_generator.py
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.
```

---

# ✨ Core Features

- Live API data fetching
- Environment variable configuration (`.env`)
- Secure API key management
- Dynamic HTML generation
- Clean modular architecture
- Graceful handling of missing animal fields
- Error message if animal does not exist

---

# 📂 Project Structure

```
zootopia-animal-generator/
│
├── animals_web_generator.py   # Website generator
├── data_fetcher.py            # API data fetcher
├── animals_template.html      # HTML template
├── animals.html               # Generated webpage
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

# 🚀 Installation & Usage

## Requirements

- Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```
API_KEY='your_api_ninjas_key_here'
```

This keeps sensitive data out of the source code.

---

## Run the Program

```bash
python animals_web_generator.py
```

Then open the generated file:

```
animals.html
```

in your browser.

---

# 🧠 Technical Concepts Applied

| Concept | Implementation |
|------|------|
| API Requests | `requests` |
| Environment Variables | `python-dotenv` |
| JSON Processing | Python dictionaries |
| Template Rendering | Placeholder replacement |
| Modular Architecture | `data_fetcher` + generator |

---

# 🔐 Error Handling

The program safely handles cases such as:

- Missing animal fields
- Non‑existing animals
- Invalid user input
- Empty API responses

Example message shown in the generated HTML:

```
The animal "goadohjasgfas" doesn't exist.
```

---

# 🎓 Learning Objectives

- Work with external APIs
- Handle JSON responses safely
- Use environment variables for secrets
- Separate code into modules
- Generate HTML dynamically

---

# 📈 Portfolio Upgrade Ideas

Possible future improvements:

- Convert the project into a **Flask web application**
- Add **animal images**
- Implement **search suggestions**
- Add **pagination**
- Add **unit tests**
- Dockerize the project
- Deploy online (Render / Railway)

---

# 🇩🇪 Kurzbeschreibung

Ein Python‑Projekt zur dynamischen Generierung einer HTML‑Webseite aus **API‑Tierdaten**.  
Der Nutzer gibt ein Tier ein, das Programm ruft Daten von der **API Ninjas Animals API** ab und erstellt automatisch eine Webseite mit den Ergebnissen.

---

# 📄 License

MIT License

---

# 👤 Author

Hakan Yildirim  
Python Software Developer (AI Track)  
Masterschool Bootcamp

GitHub: https://github.com/haki36  
LinkedIn: https://linkedin.com/in/hakan-yildirim-tech
