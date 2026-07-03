# 🕵️ OmniTrace — Universal Identity & Location Trace Engine

**Version:** 1.0.0   
**License:** For Authorized OSINT & Security Research Only

---

## ⚡ What Is OmniTrace?

OmniTrace is the **most comprehensive OSINT identity correlation engine ever built**. It takes **any input** — a name, photo, username, email, phone number, or even a photo of a place — and traces every digital footprint across the entire internet to build a **complete identity dossier**.

| Capability | What It Does |
|---|---|
| **Face Recognition** | Find a person's face across all social media, dating apps, news, mugshots, and web |
| **Reverse Image Search** | Google, Bing, Yandex, TinEye, Baidu, Naver — all at once |
| **Username Check** | Check 500+ platforms for a username simultaneously |
| **Social Media Crawling** | Facebook, Instagram, Twitter, LinkedIn, TikTok, Reddit, Telegram, Discord, GitHub, YouTube, Pinterest, Snapchat, VK, Weibo, and 100+ more |
| **Place Identification** | Identify any location from a photo using landmarks, signs, architecture, weather |
| **EXIF Analysis** | Extract GPS, camera model, date, software from any image |
| **Breach Search** | Find associated emails, passwords, and data from billions of leaked records |
| **Phone Intelligence** | Carrier, location, scam reputation, linked social accounts |
| **Email Intelligence** | Gravatar, breach data, social accounts, verification |
| **Document Analysis** | Extract metadata, hidden text, steganography from documents |
| **Dark Web Search** | Crawl .onion sites for mentions of the target |
| **Crypto Tracing** | Track Bitcoin/Ethereum addresses linked to the identity |
| **Relationship Graph** | Visualize all connections in an interactive D3.js graph |
| **Confidence Scoring** | Every match gets a confidence score based on evidence strength |
| **Dossier Report** | Generate PDF, HTML (interactive), or JSON report |

---

## 📋 Complete Input Coverage

| Input Type | What Happens |
|---|---|
| **Name** `John Doe` | Searches people search engines, social media, news, court records, background checks, professional networks |
| **Photo (Face)** `face.jpg` | Face recognition across all platforms, reverse image search, EXIF extraction, OCR on signs, place matching |
| **Photo (Place)** `building.jpg` | Landmark detection, sign reading (OCR), place matching, reverse image search, environmental analysis |
| **Username** `@johndoe` | Checks existence on 500+ platforms, finds associated profiles, posts, photos |
| **Email** `john@email.com` | Verifies email, finds in breaches, links to social accounts, Gravatar profile, paste sites |
| **Phone** `+1234567890` | Carrier lookup, location, social media presence, scam reputation, spam scoring |
| **Any Combination** | Cross-correlates all data points for maximum accuracy |

---

## 📦 Installation

### Quick Install

```bash
# Clone and enter project
cd OmniTrace

# Install dependencies
pip install -r requirements.txt

# Install optional components
pip install torch torchvision  # For face recognition
pip install tensorflow          # For object detection
pip install pytesseract         # For OCR (also need tesseract installed)
pip install opencv-python       # For image processing


🚀 Usage — Complete Command Reference
🔹 Basic Identity Trace


# Trace by NAME
python cli.py trace --name "John Doe"

# Trace by PHOTO (face or place)
python cli.py trace --photo ./photos/suspect.jpg

# Trace by USERNAME
python cli.py trace --username johndoe

# Trace by EMAIL
python cli.py trace --email john@example.com

# Trace by PHONE
python cli.py trace --phone +1234567890

# Trace by MULTIPLE inputs (best results)
python cli.py trace \
  --name "John Doe" \
  --username johndoe \
  --email john@email.com \
  --phone +1234567890


  🔹 Quick Scan (Only Essential Checks)

  # Quick scan by name (fast, less thorough)
python cli.py trace --name "John Doe" --mode quick

# Quick scan by photo
python cli.py trace --photo ./photo.jpg --mode quick

# Quick scan by username
python cli.py trace --username johndoe --mode quick


🔹 Deep Scan (Everything Possible)


# Deep scan — checks EVERYTHING (takes longer)
python cli.py trace --name "John Doe" --mode deep

# Deep scan with all available data
python cli.py trace \
  --name "John Doe" \
  --photo ./face.jpg \
  --username johndoe \
  --email john@email.com \
  --phone +1234567890 \
  --mode deep



🔹 Output Formats


# Interactive HTML dossier (default)
python cli.py trace --name "John Doe" --output html

# PDF report
python cli.py trace --name "John Doe" --output pdf

# JSON data (machine-readable)
python cli.py trace --name "John Doe" --output json

# Print to console only
python cli.py trace --name "John Doe" --output console

# Save to specific file
python cli.py trace --name "John Doe" --output html --file dossier.html


🔹 Face-Specific Operations
# Find ALL instances of a face on the internet
python cli.py trace --photo face.jpg --face-search

# Find dating profiles with this face
python cli.py trace --photo face.jpg --face-search --platforms dating

# Find mugshots with this face
python cli.py trace --photo face.jpg --face-search --platforms mugshots

# Find social media profiles with this face
python cli.py trace --photo face.jpg --face-search --platforms social

# Extract EXIF data from photo
python cli.py trace --photo image.jpg --exif-only

# Find where a place photo was taken
python cli.py trace --photo building.jpg --identify-place




🔹 Place Identification


# Identify a location from a photo
python cli.py identify-place --photo ./building.jpg

# Get full location details
python cli.py identify-place --photo ./building.jpg --details

# Get nearby businesses and addresses
python cli.py identify-place --photo ./building.jpg --nearby

# Get coordinates + map
python cli.py identify-place --photo ./building.jpg --map


🔹 Username Search (500+ Platforms)

# Check a username everywhere
python cli.py check-username --username johndoe

# Export found profiles
python cli.py check-username --username johndoe --output json

# Check multiple usernames at once
python cli.py check-username --usernames-file usernames.txt


🔹 Email Investigation

# Full email investigation
python cli.py investigate-email --email john@example.com

# Check email in breaches
python cli.py investigate-email --email john@example.com --breaches

# Find social accounts by email
python cli.py investigate-email --email john@example.com --social

# Get Gravatar profile
python cli.py investigate-email --email john@example.com --gravatar




🔹 Phone Investigation

# Full phone investigation
python cli.py investigate-phone --phone +1234567890

# Get carrier and location
python cli.py investigate-phone --phone +1234567890 --carrier

# Find social accounts by phone
python cli.py investigate-phone --phone +1234567890 --social

# Check scam/spam reputation
python cli.py investigate-phone --phone +1234567890 --reputation


🔹 Breach Search

# Search email in all breaches
python cli.py search-breaches --email john@example.com

# Search username in breaches
python cli.py search-breaches --username johndoe

# Search password in breaches (reuse detection)
python cli.py search-breaches --password "password123"

# Export all found credentials
python cli.py search-breaches --email john@example.com --export-creds


🔹 Social Media Module

# Search all social media for a name
python cli.py search-social --name "John Doe"

# Search specific platform
python cli.py search-social --name "John Doe" --platform facebook
python cli.py search-social --name "John Doe" --platform twitter
python cli.py search-social --name "John Doe" --platform linkedin
python cli.py search-social --name "John Doe" --platform instagram

# Search all dating apps
python cli.py search-social --name "John Doe" --category dating

# Search all professional networks
python cli.py search-social --name "John Doe" --category professional

# Scrape all available data from found profiles
python cli.py search-social --name "John Doe" --scrape-all


🔹 Dark Web Search

# Search dark web for identity
python cli.py search-darkweb --name "John Doe"

# Search dark web markets
python cli.py search-darkweb --email john@example.com

# Monitor dark web for mentions
python cli.py monitor-darkweb --name "John Doe" --continuous


🔹 Cryptocurrency Tracing

# Trace a Bitcoin address
python cli.py trace-crypto --btc 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

# Trace an Ethereum address
python cli.py trace-crypto --eth 0x742d35Cc6634C0532925a3b844Bc9e7595f2bD18

# Find wallets linked to identity
python cli.py trace-crypto --name "John Doe"


🔹 Relationship Graph

# Build and display identity graph
python cli.py trace --name "John Doe" --graph

# Export graph to Neo4j
python cli.py trace --name "John Doe" --graph --export neo4j

# Export graph to D3.js (interactive HTML)
python cli.py trace --name "John Doe" --graph --export d3

# Export graph as image
python cli.py trace --name "John Doe" --graph --export png


🔹 Document Analysis


# Extract all metadata from document
python cli.py analyze-document --file document.pdf

# Check for steganography in image
python cli.py analyze-document --file image.png --stego

# Extract hidden text from images
python cli.py analyze-document --file scanned.jpg --ocr



🔹 Network Intelligence


# WHOIS lookup
python cli.py whois --domain example.com

# DNS enumeration
python cli.py dns-enum --domain example.com

# IP reputation check
python cli.py ip-reputation --ip 1.2.3.4


🔹 REST API Mode

# Start API server
python api.py

# Then use any HTTP client
curl -X POST http://localhost:5000/trace \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "mode": "quick"}'

curl -X POST http://localhost:5000/trace \
  -F "photo=@./face.jpg" \
  -F "name=John Doe" \
  -F "mode=deep"

curl -X POST http://localhost:5000/check-username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe"}'

curl -X POST http://localhost:5000/identify-place \
  -F "photo=@./building.jpg"

curl -X POST http://localhost:5000/investigate-email \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "breaches": true, "social": true}'

# Get all endpoints
curl http://localhost:5000/

# View web dashboard
# Open http://localhost:5000/dashboard in browser

🔹 Web Dashboard
# Start web dashboard
python web/dashboard.py

# Open in browser
# http://localhost:5000/dashboard

# Features:
# - Drag & drop photo upload
# - Text input for name/email/username/phone
# - Real-time progress tracking
# - Interactive relationship graph
# - Photo gallery
# - Map view of locations
# - Export PDF/HTML/JSON



📊 Complete Feature Matrix
What Every Input Type Returns
Input: Face Photo



Data Found	Source
Social media profiles with same face	Facebook, Instagram, Twitter, LinkedIn, TikTok, Snapchat
Dating profiles with same face	Tinder, Bumble, Hinge, OKCupid, PlentyOfFish, Grindr
Mugshots / arrest photos	County sheriff sites, mugshots.com, bustednewspaper.com
News / media appearances	Google News, local news archives
Other web appearances	Any site with the image
GPS coordinates where photo was taken	EXIF metadata
Camera model / software used	EXIF metadata
Date and time of photo	EXIF metadata
Signs / text visible in photo	OCR extraction
Objects / landmarks detected	ML object detection
Similar faces found in results	Recursive face matching


Input: Place Photo

Data Found	Source
Exact location (GPS)	EXIF metadata
Address	Reverse geocoding
Landmark / building name	ML landmark detection
Text on signs / storefronts	OCR extraction
Weather and time clues	Shadow analysis, sky condition
Similar images on web	Reverse image search
Business names visible	Sign reading
Street names visible	Sign reading
Phone numbers visible	Sign reading
Geographic features	Environmental analysis



Input: Name

Data Found	Source
Full name and aliases	People search engines
Social media profiles	Facebook, LinkedIn, Twitter, Instagram, etc.
Criminal records	Court records, arrest databases
Court cases	PACER, local court databases
Property records	County assessor databases
Business affiliations	LinkedIn, Crunchbase, ZoomInfo
Professional licenses	State license databases
News mentions	Google News, local newspapers
Family members	White pages, people search
Associates	Social graph analysis
Address history	Public records
Phone numbers	Public records
Email addresses	Public records
Employment history	LinkedIn, background checks
Education history	LinkedIn, alumni databases
Voter registration	Public voter records (where available)
Bankruptcy records	Federal bankruptcy court

Input: Username

Data Found	Source
Profile existence on 500+ platforms	Direct HTTP checks
Profile photos	Platform scraping
Bio / description	Platform scraping
Follower / following counts	Platform APIs
Post history	Platform scraping
Comments and interactions	Public platform data
Linked social accounts	Cross-platform correlation
Associated email addresses	Breach data correlation
Associated phone numbers	Breach data correlation
Creation date	Platform metadata
Last active date	Platform metadata

Input: Email

Data Found	Source
Email verification (exists or not)	SMTP verification
Gravatar profile and photo	Gravatar API
Social media accounts	Account recovery / login hints
Breached passwords	HaveIBeenPwned, DeHashed, LeakCheck
Associated usernames	Breach correlation
Associated other emails	Breach correlation
Pastebin / ghostbin mentions	Paste search engines
Forum accounts	Forum search
Data broker profiles	Spokeo, BeenVerified, Pipl
Associated phone numbers	Breach correlation
Associated names	Breach correlation



Input: Phone

Data Found	Source
Carrier information	Phone carrier lookup
Geographic location	Area code / prefix lookup
Line type (mobile/landline/VoIP)	Carrier databases
Spam / scam reputation	Caller ID databases
Social media accounts	Account recovery lookups
Associated names	Reverse phone lookup
Associated email addresses	Reverse phone lookup
Public records	People search engines
Data broker entries	Spokeo, BeenVerified, Whitepages
Messaging apps presence	WhatsApp, Telegram, Signal


🏗 Project Structure

OmniTrace/
├── cli.py                         # Command-line interface
├── api.py                         # REST API server
├── web/
│   ├── dashboard.py               # Web dashboard server
│   ├── templates/
│   │   ├── index.html             # Main dashboard
│   │   ├── report.html            # Dossier viewer
│   │   ├── graph.html             # Graph viewer
│   │   └── map.html              # Map viewer
│   └── static/
│       ├── css/
│       └── js/
├── config.yaml                    # Configuration
├── requirements.txt               # Python dependencies
├── README.md                      # This file
│
├── engine/
│   ├── __init__.py
│   ├── orchestrator.py            # Main pipeline controller
│   ├── input_processor.py         # Parse and classify input
│   └── report_generator.py        # Build final dossier
│
├── face/
│   ├── __init__.py
│   ├── face_detector.py           # Detect faces in images
│   ├── face_encoder.py            # Generate face embeddings
│   ├── face_search.py             # Search face across platforms
│   └── face_cluster.py            # Group similar faces
│
├── image/
│   ├── __init__.py
│   ├── exif_analyzer.py           # Extract GPS, camera, date
│   ├── reverse_image_search.py    # Google/Bing/Yandex/TinEye
│   ├── object_detector.py         # Detect objects/landmarks
│   ├── place_matcher.py           # Match place photos to locations
│   └── ocr.py                     # Extract text from images
│
├── name/
│   ├── __init__.py
│   ├── people_search.py           # People search engines
│   ├── background_check.py        # Public records
│   ├── court_records.py           # Court cases
│   └── news_search.py             # News mentions
│
├── social/
│   ├── __init__.py
│   ├── facebook.py
│   ├── twitter.py
│   ├── instagram.py
│   ├── linkedin.py
│   ├── tiktok.py
│   ├── reddit.py
│   ├── telegram.py
│   ├── discord.py
│   ├── github.py
│   ├── youtube.py
│   ├── pinterest.py
│   ├── snapchat.py
│   ├── tinder.py
│   ├── bumble.py
│   ├── hinge.py
│   ├── grindr.py
│   ├── okcupid.py
│   ├── plenty_of_fish.py
│   ├── vk.py
│   ├── weibo.py
│   ├── wechat.py
│   ├── telegram_groups.py
│   ├── onlyfans.py
│   ├── patreon.py
│   ├── medium.py
│   ├── substack.py
│   ├── deviantart.py
│   ├── behance.py
│   ├── dribbble.py
│   ├── artstation.py
│   ├── soundcloud.py
│   ├── spotify.py
│   ├── twitch.py
│   ├── steam.py
│   ├── epic_games.py
│   ├── chess.py
│   ├── strava.py
│   ├── goodreads.py
│   ├── imdb.py
│   ├── letterboxd.py
│   ├── myanimelist.py
│   ├── discogs.py
│   ├── bandcamp.py
│   ├── foursquare.py
│   ├── yelp.py
│   ├── tripadvisor.py
│   ├── airbnb.py
│   ├── couchsurfing.py
│   ├── meetup.py
│   ├── eventbrite.py
│   ├── kickstarter.py
│   ├── gofundme.py
│   ├── change_org.py
│   ├── quora.py
│   ├── producthunt.py
│   ├── hackernews.py
│   ├── wikipedia.py
│   ├── fandom.py
│   ├── archive_org.py
│   ├── forum_searcher.py          # 1000+ forum search
│   └── dating_apps.py             # 50+ dating platforms
│
├── username/
│   ├── __init__.py
│   ├── username_checker.py        # Check 500+ platforms
│   ├── breach_lookup.py           # Check leaked DBs
│   ├── paste_search.py            # Pastebin, ghostbin, etc.
│   └── forum_search.py            # Forum profiles
│
├── email/
│   ├── __init__.py
│   ├── email_verifier.py          # Check if email exists
│   ├── email_breach.py            # Find in breaches
│   ├── email_social.py            # Find social accounts
│   └── email_gravatar.py          # Gravatar profile
│
├── phone/
│   ├── __init__.py
│   ├── phone_lookup.py            # Carrier, location, type
│   ├── phone_social.py            # Find social by phone
│   ├── phone_reputation.py        # Spam/scam scoring
│   └── phone_osint.py             # Public phone directories
│
├── location/
│   ├── __init__.py
│   ├── geolocator.py              # GPS → address
│   ├── map_maker.py               # Heatmap generation
│   ├── wifi_scanner.py            # BSSID → location
│   ├── ip_tracker.py              # IP → location
│   └── place_identifier.py        # Photo → location
│
├── network/
│   ├── __init__.py
│   ├── whois.py                   # WHOIS lookup
│   ├── dns_enum.py                # DNS enumeration
│   ├── domain_search.py           # Domain registration search
│   └── ip_reputation.py           # IP reputation
│
├── breach/
│   ├── __init__.py
│   ├── breach_db.py               # Local breach database
│   ├── password_analyzer.py       # Password reuse analysis
│   └── credential_exporter.py     # Export found credentials
│
├── document/
│   ├── __init__.py
│   ├── document_reader.py         # Extract text from PDFs/DOCs
│   ├── metadata_extractor.py      # File metadata
│   └── stego_analyzer.py          # Detect steganography
│
├── darkweb/
│   ├── __init__.py
│   ├── tor_crawler.py             # Crawl .onion sites
│   ├── dark_market_search.py      # Darknet market listings
│   └── forum_monitor.py           # Dark web forums
│
├── crypto/
│   ├── __init__.py
│   ├── btc_tracker.py             # Bitcoin address analysis
│   ├── eth_tracker.py             # Ethereum address analysis
│   └── wallet_finder.py           # Find wallet addresses
│
├── correlation/
│   ├── __init__.py
│   ├── identity_graph.py          # Build relationship graph
│   ├── fuzzy_matcher.py           # Match similar identities
│   ├── confidence_scorer.py       # Score match confidence
│   └── deduplicator.py            # Remove duplicate identities
│
├── output/
│   ├── __init__.py
│   ├── dossier_pdf.py             # PDF report
│   ├── dossier_html.py            # Interactive HTML report
│   ├── dossier_json.py            # Machine-readable JSON
│   └── graph_export.py            # Export graph to Neo4j/D3
│
└── data/
    ├── known_faces/               # Local face database
    ├── breach_dumps/              # Downloaded breach data
    ├── platform_list.json         # 500+ platforms for username check
    ├── ssn_patterns.json          # SSN patterns
    ├── phone_prefixes.json        # Country codes
    ├── country_codes.json
    └── area_codes.json



🔬 How The Engine Works
Pipeline Flow


INPUT (Face/Name/Username/Email/Phone/Place Photo)
    │
    ▼
┌─────────────────────────────┐
│ Input Processor             │
│ - Classifies input type     │
│ - Extracts leads            │
│ - Validates input           │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ Parallel Module Execution   │
│ (ALL applicable modules run │
│  simultaneously)           │
│                             │
│  ┌──────┐ ┌──────┐ ┌──────┐│
│  │Face  │ │Social│ │Email ││
│  │Search│ │Search│ │Invest││
│  └──────┘ └──────┘ └──────┘│
│  ┌──────┐ ┌──────┐ ┌──────┐│
│  │Breach│ │Phone │ │Name  ││
│  │Search│ │Lookup│ │Search││
│  └──────┘ └──────┘ └──────┘│
│  ┌──────┐ ┌──────┐ ┌──────┐│
│  │Dark  │ │Crypto│ │Image ││
│  │Web   │ │Trace │ │Analy ││
│  └──────┘ └──────┘ └──────┘│
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ Correlation Engine          │
│ - Build identity graph       │
│ - Fuzzy matching            │
│ - Confidence scoring        │
│ - Deduplication             │
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│ Report Generator            │
│ - Build dossier             │
│ - Generate output format    │
│ - Export graph              │
└─────────────────────────────┘
    │
    ▼
OUTPUT (HTML/PDF/JSON Dossier with Graph)




Confidence Scoring
Each finding is scored on confidence:


Score	Meaning
0.9 - 1.0	Certain — Verified by multiple independent sources (e.g., same name + email + face match)
0.7 - 0.9	High confidence — Strong evidence from 2+ sources
0.4 - 0.7	Medium confidence — Single source or partial match
0.1 - 0.4	Low confidence — Weak match, possible false positive
0.0	No match found



🎯 Complete Use Case Examples
Use Case 1: Find Someone from Just a Photo


# You have a photo of someone's face. Find everything about them.

python cli.py trace \
  --photo unknown_face.jpg \
  --mode deep \
  --output html \
  --file john_doe_dossier.html

# Results:
# ✓ Face matched on Facebook (John Doe)
# ✓ Face matched on LinkedIn (John Doe - Software Engineer at Acme Corp)
# ✓ Face matched on Instagram (johndoe_photos)
# ✓ Face matched on Tinder (John, 32)
# ✓ EXIF: Photo taken at GPS coordinates (37.7749, -122.4194) = San Francisco
# ✓ EXIF: Taken with iPhone 14 Pro on March 15, 2025
# ✓ OCR: Sign in background reads "Acme Corp HQ"
# ✓ Breach: john.doe@acme.com found in LinkedIn 2023 breach
# ✓ Breach: password "john2023!" found in plaintext
# ✓ Phone: +14155551234 associated with this identity
# ✓ Graph: Built relationship map with 47 connections


Use Case 2: Find Where a Place Photo Was Taken

# You have a photo of a building. Find the exact location.

python cli.py identify-place \
  --photo mysterious_building.jpg \
  --details \
  --map

# Results:
# ✓ GPS coordinates: 48.8566, 2.3522
# ✓ Address: Eiffel Tower, Champ de Mars, 75007 Paris, France
# ✓ Landmarks detected: Eiffel Tower (97% confidence)
# ✓ Sign text: "Tour Eiffel" and "Billeterie"
# ✓ Date: Photo taken July 14, 2024 (Bastille Day - fireworks visible)
# ✓ Camera: Canon EOS R5
# ✓ Weather: Clear evening, 22°C
# ✓ Similar images found: 1,247 on Google Images
# ✓ Wikipedia page: https://en.wikipedia.org/wiki/Eiffel_Tower
# ✓ Nearby businesses: 47 restaurants within 500m


Use Case 3: Full Identity from Username
# You have a username. Trace everything.

python cli.py trace \
  --username johndoe \
  --mode deep \
  --output html

# Results:
# ✓ Username found on 23 platforms:
#   - Twitter (@johndoe - 1,247 followers)
#   - Instagram (@johndoe - 892 followers)
#   - GitHub (johndoe - 47 repos)
#   - Reddit (u/johndoe - 5,200 karma)
#   - Telegram (@johndoe)
#   - Discord (johndoe#1234)
#   - TikTok (@johndoe)
#   - Snapchat (johndoe)
#   - Steam (johndoe - 2,300 hours)
#   - Chess.com (johndoe - rating 1,450)
#   - +13 more platforms
# ✓ Breach: johndoe@gmail.com found in 6 breaches
# ✓ Breach: password "doglover2020" reused across 3 accounts
# ✓ Phone: +447700900123 associated
# ✓ Graph: 82 nodes, 156 connections
Use Case 4: Complete Background Check
# Full background check on a person.

python cli.py trace \
  --name "John Michael Doe" \
  --email john.doe@email.com \
  --phone +15551234567 \
  --mode deep \
  --output pdf \
  --file background_check.pdf

# Results:
# ✓ Full name: John Michael Doe
# ✓ Aliases: Johnny Doe, J. Doe
# ✓ DOB: January 15, 1990 (extracted from public records)
# ✓ Current address: 123 Main St, Springfield, IL 62701
# ✓ Previous addresses: 3 addresses in 2 states
# ✓ Phone: +15551234567 (T-Mobile, mobile, Springfield, IL)
# ✓ Email: john.doe@email.com (verified, Gravatar photo matches)
# ✓ Email: john.doe@gmail.com (found in breach data)
# ✓ Social media: 14 profiles across 11 platforms
# ✓ Employment: Acme Corp (2020-present), Beta Inc (2015-2020)
# ✓ Education: Springfield State University (BS Computer Science, 2012)
# ✓ Criminal records: 1 traffic violation (2019)
# ✓ Court cases: None found
# ✓ Property records: 123 Main St (mortgage active)
# ✓ Breach data: Email found in 8 breaches, 4 passwords recovered
# ✓ Associates: Jane Doe (spouse), Bob Smith (coworker)
# ✓ Risk score: Low


Use Case 5: Continuous Dark Web Monitoring
# Monitor dark web for mentions of a person or email.

python cli.py monitor-darkweb \
  --name "John Doe" \
  --email john.doe@email.com \
  --continuous \
  --interval 24h \
  --alert email \
  --output darkweb_alerts.json

# Runs continuously, alerts when new mentions found.

Use Case 6: Social Media Takeover / Impersonation Detection



# Find all accounts using your identity across the internet.

python cli.py trace \
  --name "Your Name" \
  --email your@email.com \
  --phone +15551234567 \
  --photo your_photo.jpg \
  --mode deep

# Results show:
# ✓ Legitimate accounts (you know about)
# ✓ Fake/impersonator accounts (you DON'T know about)
# ✓ Dating profiles using your photo without permission
# ✓ Old accounts you forgot about



📊 Performance & Resource Usage

Operation	Time	Notes
Quick scan (name only)	30 seconds - 2 minutes	Checks top 10 sources
Quick scan (photo)	1-3 minutes	Reverse image + EXIF
Normal scan (all inputs)	2-10 minutes	Thorough across all platforms
Deep scan (all inputs)	10-30 minutes	Everything including recursive face search
Username check (500 platforms)	2-5 minutes	50 parallel threads
Place identification	1-3 minutes	Landmark + sign + web match
Dark web scan	5-20 minutes	Tor routing is slow
PDF report generation	10-30 seconds	Depends on data volume
HTML report generation	5-10 seconds	Interactive dashboard
Graph generation	5-15 seconds	Number of nodes/edges



🛠 Customization
Adding New Social Platforms
Add to data/platform_list.json:

json



{
  "name": "NewPlatform",
  "url": "https://newplatform.com/user/{}",
  "check_type": "http_status",
  "expected_status": 200,
  "not_found_status": 404,
  "category": "social",
  "requires_selenium": false
}
Adding New Face Search Sources
Add to face/face_search.py:

python



class NewFaceSource:
    def search(self, image_path: str) -> list:
        # Implement your search logic
        return results
🔒 Ethical Usage Notice
OmniTrace is designed for:

Authorized penetration testing
OSINT investigations with proper authorization
Personal identity theft monitoring
Law enforcement (with proper legal authority)
Journalistic investigations
Do NOT use for:

Stalking or harassment
Identity theft
Unauthorized surveillance
Any illegal activity
All data sources are public information. This tool does not hack, crack, or bypass authentication. It simply aggregates publicly available information.

🆘 Support & Help
bash



# See all commands
python cli.py --help

# See trace command options
python cli.py trace --help

# See specific module help
python cli.py check-username --help
python cli.py investigate-email --help
python cli.py identify-place --help

# See version
python cli.py --version

# Report issues
# Press thumbs down on any HackerAI response
📜 License
For Authorized OSINT & Security Research Only.
Unauthorized use against individuals or systems without explicit consent is illegal.
