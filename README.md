<h1 align="center">🕵️ OmniTrace</h1>
<p align="center"><b>Universal Identity &amp; Location Trace Engine</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version">
  <img src="https://img.shields.io/badge/python-3.9%2B-green" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-orange" alt="license">
  <img src="https://img.shields.io/badge/OSINT-toolkit-red" alt="osint">
</p>

<p align="center"><b>Developed by JOJIN JOHN</b></p>

---

> ⚠️ **Ethical use only.** OmniTrace is for **authorized** OSINT, security research, and educational use. It aggregates *publicly available* information and does not hack, crack, or bypass authentication. See the [Ethical Usage Notice](#-ethical-usage-notice).

> ℹ️ **About the data:** OmniTrace ships as a fully-working pipeline that returns realistic **demo/mock data** out of the box, so every command runs with zero setup. To get **live** results, add your API keys in `config/keys.yaml` (see `config/keys.example.yaml`) — modules such as breach lookup (HaveIBeenPwned), email intel (Clearbit), and Gravatar automatically switch to real data when keys are present.

---

## ⚡ What Is OmniTrace?

OmniTrace is a modular OSINT correlation engine. Give it **any input** — a name, username, email, phone number, or a photo — and it runs every applicable module, correlates the results into an identity graph, scores confidence, and produces a dossier (Console / JSON / HTML / PDF).

| Capability | What It Does |
|---|---|
| **Username Check** | Check a username across many platforms at once |
| **Social Search** | Facebook, Instagram, Twitter, LinkedIn, TikTok, Reddit, GitHub, YouTube, Pinterest, Snapchat |
| **Email Intel** | Format validation, Gravatar, breach lookup, linked accounts |
| **Phone Intel** | Carrier, line type, location, messaging-app presence, spam score |
| **Breach Search** | Look up emails / usernames / password reuse in breach data |
| **Face Search** | Match a face across platforms (demo) + reverse image search |
| **Image / EXIF** | GPS, camera, date, OCR on signs, object detection |
| **Place ID** | Identify a location from a photo (landmarks, signs) |
| **Dark Web** | Search dark-web mentions of a target |
| **Crypto Tracing** | Trace Bitcoin / Ethereum addresses and find linked wallets |
| **Network Intel** | WHOIS, DNS enumeration, IP reputation |
| **Document Analysis** | Metadata extraction and steganography checks |
| **Correlation Graph** | Build a relationship graph + confidence score |
| **Dossier Report** | Export Console, JSON, HTML, or PDF |

---

## 📦 Installation

```bash
# 1. Clone
git clone https://github.com/jojin1709/OmniTrace.git
cd OmniTrace

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Add API keys for live data
cp config/keys.example.yaml config/keys.yaml
#   ...then edit config/keys.yaml
```

Requires **Python 3.9+**. All commands work immediately with demo data — no keys needed.

---

## 🚀 Command Reference

Every command below works out of the box. Use `python cli.py <command> --help` for full options.

### Identity Trace

```bash
# Trace by a single input
python cli.py trace --name "John Doe"
python cli.py trace --username johndoe
python cli.py trace --email john@example.com
python cli.py trace --phone +1234567890
python cli.py trace --photo ./photo.jpg

# Trace by MULTIPLE inputs (best correlation)
python cli.py trace --name "John Doe" --username johndoe --email john@example.com --phone +1234567890

# Scan depth
python cli.py trace --name "John Doe" --mode quick    # fast
python cli.py trace --name "John Doe" --mode normal
python cli.py trace --name "John Doe" --mode deep     # everything

# Build the relationship graph
python cli.py trace --name "John Doe" --graph
```

> Tip: `python cli.py --name "John Doe"` (without the `trace` word) also works — it defaults to `trace`.

### Output Formats

```bash
python cli.py trace --name "John Doe" --output console        # pretty console (default)
python cli.py trace --name "John Doe" --output json           # machine-readable
python cli.py trace --name "John Doe" --output html --file dossier.html
python cli.py trace --name "John Doe" --output pdf
```

### Username Search

```bash
python cli.py check-username --username johndoe
python cli.py check-username --username johndoe --output json
python cli.py check-username --usernames-file usernames.txt
```

### Email Investigation

```bash
python cli.py investigate-email --email john@example.com
python cli.py investigate-email --email john@example.com --breaches --social --gravatar
```

### Phone Investigation

```bash
python cli.py investigate-phone --phone +1234567890
python cli.py investigate-phone --phone +1234567890 --carrier --social --reputation
```

### Breach Search

```bash
python cli.py search-breaches --email john@example.com
python cli.py search-breaches --username johndoe
python cli.py search-breaches --password "password123"      # reuse detection
```

### Social Media

```bash
python cli.py search-social --name "John Doe"
python cli.py search-social --name "John Doe" --platform linkedin
python cli.py search-social --name "John Doe" --category dating
```

### Place Identification

```bash
python cli.py identify-place --photo ./building.jpg
python cli.py identify-place --photo ./building.jpg --details --map --nearby
```

### Dark Web

```bash
python cli.py search-darkweb --name "John Doe"
python cli.py search-darkweb --email john@example.com
python cli.py monitor-darkweb --name "John Doe" --continuous --interval 24h
```

### Cryptocurrency

```bash
python cli.py trace-crypto --btc 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
python cli.py trace-crypto --eth 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18
python cli.py trace-crypto --name "John Doe"
```

### Document Analysis

```bash
python cli.py analyze-document --file document.pdf
python cli.py analyze-document --file image.png --stego
```

### Network Intelligence

```bash
python cli.py whois --domain example.com
python cli.py dns-enum --domain example.com
python cli.py ip-reputation --ip 1.2.3.4
```

### Help & Version

```bash
python cli.py --help
python cli.py trace --help
python cli.py --version
```

---

## 🌐 REST API & Web Dashboard

Start the server:

```bash
python api.py
#   or the equivalent launcher:
python web/dashboard.py
```

Then open the dashboard at **http://localhost:5000/dashboard** or call the API:

```bash
# JSON trace
curl -X POST http://localhost:5000/trace \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Photo upload trace
curl -X POST http://localhost:5000/trace \
  -F "photo=@./face.jpg" -F "name=John Doe"
```

| Endpoint | Method | Description |
|---|---|---|
| `/` and `/dashboard` | GET | Web dashboard |
| `/trace` | POST | Run a full trace (JSON body or multipart photo) |
| `/check-username` | POST | Username check |
| `/identify-place` | POST | Place identification |
| `/investigate-email` | POST | Email investigation |

---

## 🏗 Project Structure

```
OmniTrace/
├── cli.py                     # Command-line interface (all subcommands)
├── api.py                     # Flask REST API + dashboard server
├── config.yaml                # Global configuration
├── config/keys.example.yaml   # API-key template (copy to keys.yaml)
├── requirements.txt
│
├── engine/                    # Core pipeline
│   ├── orchestrator.py        # Runs applicable modules for the input
│   ├── input_processor.py     # Classify input & extract leads
│   ├── report_generator.py    # Build the dossier object
│   ├── config_loader.py       # Config / key loader
│   └── correlation/           # Identity graph + confidence scoring
│
├── face/                      # Face search
├── image/                     # EXIF, OCR, reverse image, object detection
├── name/                      # People search
├── social/                    # Social-media search
├── username/                  # Username checker (+ breach lookup)
├── email_intel/               # Email investigation
├── phone/                     # Phone lookup
├── location/                  # Place identification
├── network/                   # WHOIS / DNS / IP reputation
├── breach/                    # Breach database search
├── document/                  # Document metadata & steganography
├── darkweb/                   # Dark-web search
├── crypto/                    # BTC / ETH tracing
├── output/                    # Dossier renderers (HTML/JSON/PDF)
└── web/                       # Dashboard (dashboard.html + launcher)
```

---

## 🔬 How The Engine Works

```
INPUT (name / username / email / phone / photo)
        │
        ▼
┌───────────────────────────┐
│ Input Processor           │  classify type, extract leads, build target
└───────────────────────────┘
        │
        ▼
┌───────────────────────────┐
│ Module Execution          │  runs every applicable module:
│  face · image · name      │  social · username · email · phone
│  breach · darkweb · crypto│  location · network · document
└───────────────────────────┘
        │
        ▼
┌───────────────────────────┐
│ Correlation Engine        │  build identity graph + confidence score
└───────────────────────────┘
        │
        ▼
┌───────────────────────────┐
│ Report Generator          │  Console / JSON / HTML / PDF dossier
└───────────────────────────┘
```

### Confidence Scoring

| Score | Meaning |
|---|---|
| 0.9 – 1.0 | Certain — verified by multiple independent sources |
| 0.7 – 0.9 | High confidence — strong evidence from 2+ sources |
| 0.4 – 0.7 | Medium confidence — single source or partial match |
| 0.1 – 0.4 | Low confidence — weak match, possible false positive |
| 0.0 | No match found |

---

## 🔑 Enabling Live Data

Copy the template and add keys for any services you have:

```bash
cp config/keys.example.yaml config/keys.yaml
```

```yaml
services:
  haveibeenpwned:
    enabled: true
    api_key: "YOUR_KEY"
  clearbit:
    enabled: true
    api_key: "YOUR_KEY"
```

`config/keys.yaml` is git-ignored so your secrets are never committed. Modules automatically use live data when their key is enabled, and fall back to demo data otherwise.

---

## 📖 Documentation Website

A full documentation site lives in [`docs/`](docs/) and is ready for **GitHub Pages**:

1. Push the repo to GitHub.
2. Go to **Settings → Pages**.
3. Set **Source** to *Deploy from a branch*, branch **main**, folder **/docs**.
4. Your site goes live at `https://jojin1709.github.io/OmniTrace/`.

---

## 🔒 Ethical Usage Notice

OmniTrace is designed for:

- ✅ Authorized penetration testing & OSINT investigations
- ✅ Personal identity-theft monitoring
- ✅ Journalistic and academic research
- ✅ Law enforcement with proper legal authority

**Do NOT** use it for stalking, harassment, identity theft, unauthorized surveillance, or any illegal activity. All data sources are public information — this tool does not hack, crack, or bypass authentication. **You are responsible for how you use it.**

---

## 📜 License

Released under the **MIT License** — see [LICENSE](LICENSE).

© 2026 **JOJIN JOHN**
