# MindMate 🧘

**A minimal mental wellness web app for daily emotional check-ins.**

> Built for Stanford Code in Place 2026 — Final Project  
> Author: Muhammad Taqui · [iTaqiZ | Pakistan](https://github.com/itaqit)

---

## Overview

MindMate is a lightweight Flask web application that provides emotionally intelligent, mood-based support tools. It is not a medical product — it's a thoughtfully designed wellness companion built to give users a calm, judgment-free space to reflect on how they feel each day.

The app responds to four emotional states with tailored experiences:

| Mood | Response |
|------|----------|
| 😔 Sad | Randomized motivational quotes + curated support messages |
| 🌀 Anxious | Interactive 4-4-6-2 guided breathing exercise with live timer |
| ⚡ Stressed | Immersive text-based mindfulness visualization scene |
| ✨ Happy | Positive reinforcement + quote to anchor the feeling |

---

## Features

- **Mood Check-in Form** — Clean card-based UI with radio selection
- **Personalized Response Pages** — Content dynamically matched to selected mood
- **Flask Session** — Remembers last check-in mood across page visits
- **In-Memory Mood History** — Tracks recent check-ins (last 20 entries)
- **Animated Breathing Exercise** — JavaScript-driven 4-step breathing cycle
- **Responsive Design** — Bootstrap 5, mobile-first layout
- **Clean Architecture** — Jinja2 templates, separated logic, type-safe functions

---

## Project Structure

```
mindmate/
├── app.py                  # Flask app — routes, logic, session, data
├── requirements.txt
├── README.md
└── templates/
    ├── base.html           # Shared layout, nav, footer, design system
    ├── index.html          # Landing page with last check-in badge
    ├── checkin.html        # Mood selection form
    ├── result.html         # Personalized response page
    ├── history.html        # Mood history log
    └── about.html          # Project info + tech stack
```

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/itaqit/mindmate.git
cd mindmate
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

---

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page — intro + last check-in badge |
| `/checkin` | GET | Mood selection form |
| `/checkin` | POST | Processes mood, redirects to result |
| `/result/<mood>` | GET | Personalized response page |
| `/history` | GET | Full mood log (newest first) |
| `/about` | GET | Project info + tech stack |

---

## Design System

```
Colors:  Deep Navy (#0B1F3B)  ·  Tech Cyan (#00C2FF)
Fonts:   DM Serif Display (headings)  ·  DM Sans (body)  ·  JetBrains Mono (code)
Stack:   Python · Flask · Jinja2 · Bootstrap 5 · Vanilla JS
```

---

## Technical Implementation

**Python Concepts Used**

- Functions with type annotations for clean modular design
- Dictionaries for structured mood response data
- Lists for randomized quote selection and history tracking
- `random.choice()` for non-repetitive quote delivery
- `datetime` for human-readable timestamps
- Flask `session` for client-side state persistence

**Web Concepts Used**

- Jinja2 template inheritance (`{% extends %}`, `{% block %}`)
- Form POST handling with input validation and flash messages
- CSS custom properties (design tokens) for visual consistency
- Keyframe animations for breathing exercise and fade-in effects
- Vanilla JavaScript async loop for guided breathing timer

---

## Disclaimer

MindMate is a student-built wellness tool and is **not** a substitute for professional mental health care. If you are in crisis, please contact a licensed mental health professional or a crisis helpline in your region.

---

## Stanford Code in Place 2026

This project was submitted as a Final Project for [Stanford Code in Place 2026](https://codeinplace.stanford.edu/).

It demonstrates:
- Real-world Flask web application structure
- Clean separation of concerns (routes vs. data vs. templates)
- User experience design for a sensitive, human-centered domain
- Session management and in-memory state persistence
- Responsive, accessible frontend implementation

---

```
// iTaqiZ - PK
```
