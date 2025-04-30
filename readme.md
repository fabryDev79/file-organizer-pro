#  QuickScan Web

QuickScan Web è un tool open-source in Python per eseguire una **scansione basilare della sicurezza di un sito web**.

Analizza **header HTTP di sicurezza** e **informazioni sul certificato SSL**, permettendo di identificare configurazioni mancanti o deboli in modo semplice e veloce.

---

##  Funzionalità principali

-  Verifica la presenza di header di sicurezza fondamentali:
  - `Strict-Transport-Security`
  - `Content-Security-Policy`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
- 🔐 Estrae e stampa info dal certificato SSL:
  - Autorità che ha emesso il certificato
  - Data di inizio validità
  - Data di scadenza
- 🧠 Semplice da modificare, estendere e integrare
- 🖥️ Output leggibile in console

---

## 🛠️ Requisiti

- Python 3.x
- Libreria `requests`

### Installazione:
```bash
pip install requests

👤 Autore

[Fabry79] – Python Developer & Cybersecurity Enthusiast
🌐 GitHub: https://github.com/fabryDev79

## licenza 

MIT License

Copyright (c) 2025 [Fabry79]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
