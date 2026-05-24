"""
MindMate - Mental Wellness Web Application
A supportive emotional check-in tool for daily mental wellness.

Author: Muhammad Taqui (iTaqiZ)
Project: Stanford Code in Place 2026 Final Project
GitHub: github.com/itaqit
"""

import random
import json
import os
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
app.secret_key = "mindmate-secret-key-2026"  # Change in production

# ─────────────────────────────────────────────
# In-memory mood history (persists per session)
# For production: replace with SQLite or JSON file
# ─────────────────────────────────────────────
mood_history = []

# ─────────────────────────────────────────────
# MOOD RESPONSE DATA
# ─────────────────────────────────────────────

MOOD_DATA = {
    "sad": {
        "label": "Sad",
        "emoji": "🌧️",
        "color": "blue",
        "quotes": [
            "Even the darkest night will end, and the sun will rise. — Victor Hugo",
            "You don't have to be positive all the time. It's perfectly okay to feel sad, angry, annoyed, frustrated, scared or anxious. — Lori Deschene",
            "Every day may not be good, but there is something good in every day. — Alice Morse Earle",
            "Stars can't shine without darkness.",
            "This too shall pass. Whatever you are feeling right now has a beginning, a middle, and an end.",
            "Be gentle with yourself. You are a child of the universe. — Max Ehrmann",
            "Tough times never last, but tough people do. — Robert H. Schuller",
        ],
        "support_message": "It's okay to feel sad. Your feelings are valid, and acknowledging them is the first step toward healing.",
        "tip": "Try journaling your thoughts, listening to calming music, or reaching out to someone you trust.",
    },

    "anxious": {
        "label": "Anxious",
        "emoji": "🌀",
        "color": "purple",
        "breathing_steps": [
            {"step": 1, "action": "Breathe In", "duration": 4, "instruction": "Slowly inhale through your nose for 4 counts. Let your belly expand fully."},
            {"step": 2, "action": "Hold", "duration": 4, "instruction": "Hold your breath gently for 4 counts. Stay still. You are safe."},
            {"step": 3, "action": "Breathe Out", "duration": 6, "instruction": "Slowly exhale through your mouth for 6 counts. Let all tension go."},
            {"step": 4, "action": "Hold", "duration": 2, "instruction": "Rest for 2 counts before the next breath. Relax your shoulders."},
        ],
        "support_message": "Anxiety is your mind trying to protect you — but right now, you are safe. Let's slow down together.",
        "tip": "The 4-4-6-2 breathing pattern activates your parasympathetic nervous system and naturally reduces anxiety.",
    },

    "stressed": {
        "label": "Stressed",
        "emoji": "⚡",
        "color": "amber",
        "relaxation_scene": {
            "title": "A Quiet Forest Morning",
            "paragraphs": [
                "Close your eyes and take one slow, deep breath. You are stepping into a quiet forest at dawn.",
                "The air is cool and carries the faint scent of pine and damp earth. Soft morning light filters through the tall trees, casting golden patches on the mossy ground beneath your feet.",
                "You hear only the gentle rustling of leaves and the distant, steady rhythm of a small stream. Birds begin their morning calls — soft, unhurried, peaceful.",
                "With each breath, you feel the weight of the week lift slightly from your shoulders. Your jaw softens. Your hands unclench. Your breath deepens.",
                "You are not behind. You are not failing. You are a human being taking one moment to just breathe. That is enough.",
                "Stay here as long as you need. The forest holds no deadlines. When you open your eyes, you carry this stillness back with you.",
            ],
        },
        "support_message": "Stress is a signal, not a verdict. You are doing more than you realize — take a moment to reset.",
        "tip": "After this visualization, try writing down just ONE thing you can complete today. Small wins break the stress cycle.",
    },

    "happy": {
        "label": "Happy",
        "emoji": "✨",
        "color": "green",
        "quotes": [
            "Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
            "Count your age by friends, not years. Count your life by smiles, not tears. — John Lennon",
            "The purpose of our lives is to be happy. — Dalai Lama",
            "Joy is not in things; it is in us. — Richard Wagner",
            "Happiness is a warm cup of tea, a good book, and the quiet knowledge that you're growing. ☕",
            "Keep going. Whatever you did today to arrive here — do more of that.",
        ],
        "support_message": "You're in a great headspace today! Channel this energy into something meaningful.",
        "tip": "Happy moments are worth anchoring. Write down 3 things that contributed to this feeling — it trains your brain to notice more of them.",
    },
}

VALID_MOODS = list(MOOD_DATA.keys())

# ─────────────────────────────────────────────
# UTILITY FUNCTIONS
# ─────────────────────────────────────────────

def get_mood_response(mood: str) -> dict:
    """Return full mood data dict for a given mood key."""
    return MOOD_DATA.get(mood, {})


def get_random_quote(mood: str) -> str:
    """Return a random quote for moods that have quote lists."""
    data = MOOD_DATA.get(mood, {})
    quotes = data.get("quotes", [])
    return random.choice(quotes) if quotes else ""


def log_mood(mood: str):
    """Append a mood entry to the in-memory history list."""
    entry = {
        "mood": mood,
        "label": MOOD_DATA[mood]["label"],
        "emoji": MOOD_DATA[mood]["emoji"],
        "timestamp": datetime.now().strftime("%B %d, %Y — %I:%M %p"),
    }
    mood_history.append(entry)
    # Keep only last 20 entries (prevents unbounded growth)
    if len(mood_history) > 20:
        mood_history.pop(0)


def save_history_to_file():
    """Persist mood history to a JSON file (optional extension)."""
    try:
        with open("mood_history.json", "w") as f:
            json.dump(mood_history[-20:], f, indent=2)
    except Exception:
        pass  # Silent fail — not critical

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Home page — shows intro and last check-in mood from session."""
    last_mood = session.get("last_mood", None)
    last_mood_data = MOOD_DATA.get(last_mood, {}) if last_mood else {}
    recent_history = mood_history[-5:][::-1]  # Last 5, newest first
    return render_template(
        "index.html",
        last_mood=last_mood,
        last_mood_data=last_mood_data,
        recent_history=recent_history,
    )


@app.route("/checkin", methods=["GET", "POST"])
def checkin():
    """Mood check-in page — GET renders form, POST processes selection."""
    if request.method == "POST":
        mood = request.form.get("mood", "").strip().lower()

        # Validate input
        if mood not in VALID_MOODS:
            flash("Please select a valid mood option.", "error")
            return redirect(url_for("checkin"))

        # Store in session and global history
        session["last_mood"] = mood
        log_mood(mood)
        save_history_to_file()

        return redirect(url_for("result", mood=mood))

    return render_template("checkin.html", moods=MOOD_DATA)


@app.route("/result/<mood>")
def result(mood):
    """Results page — shows personalized response based on mood."""
    if mood not in VALID_MOODS:
        flash("Invalid mood. Please try again.", "error")
        return redirect(url_for("checkin"))

    mood_data = MOOD_DATA[mood]
    random_quote = get_random_quote(mood)

    return render_template(
        "result.html",
        mood=mood,
        mood_data=mood_data,
        random_quote=random_quote,
    )


@app.route("/history")
def history():
    """View full mood history log."""
    full_history = mood_history[::-1]  # Newest first
    return render_template("history.html", history=full_history)


@app.route("/about")
def about():
    """About MindMate page."""
    return render_template("about.html")


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# // iTaqiZ - PK
