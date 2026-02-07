
import random
import json
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import quote
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

# -----------------------------
# Curated themes
# -----------------------------
THEMES = {
    "fear": {
        "hooks": [
            "Fear is not the enemy.",
            "That fear you feel?",
            "Most people are trapped by fear."
        ],
        "insights": [
            "It signals growth is near.",
            "It shows you’re stepping outside comfort.",
            "It only survives when you stop moving."
        ],
        "closings": [
            "Move anyway.",
            "Do it afraid.",
            "Action kills fear."
        ]
    },
    "consistency": {
        "hooks": [
            "Consistency beats motivation.",
            "Winning is boring.",
            "Success is quiet."
        ],
        "insights": [
            "Small actions daily change everything.",
            "Repetition builds results.",
            "Showing up matters more than talent."
        ],
        "closings": [
            "Show up again tomorrow.",
            "Repeat this daily.",
            "Stay consistent."
        ]
    },
    "leadership": {
        "hooks": [
            "Leadership is service.",
            "True leaders inspire.",
            "Leaders show the way."
        ],
        "insights": [
            "Influence is more important than authority.",
            "Leading is about enabling others.",
            "Your vision drives your team."
        ],
        "closings": [
            "Lead with integrity.",
            "Inspire others daily.",
            "Empower those around you."
        ]
    },
    "faith": {
        "hooks": [
            "Faith moves mountains.",
            "Belief shapes reality.",
            "Faith sustains us in hard times."
        ],
        "insights": [
            "Trust even when you cannot see.",
            "Faith grows through action.",
            "Hope and faith go hand in hand."
        ],
        "closings": [
            "Hold on to your faith.",
            "Believe and move forward.",
            "Let faith guide your actions."
        ]
    }
}

# -----------------------------
# Wikipedia fallback
# -----------------------------
def fetch_wikipedia_summary(title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
    req = Request(url, headers={"User-Agent": "ContentStudioBot/1.0"})
    try:
        with urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data.get("extract")
    except:
        return None

def research_topic(topic):
    extract = fetch_wikipedia_summary(topic)
    if extract:
        return extract
    extract = fetch_wikipedia_summary(topic.title())
    if extract:
        return extract
    return None

# -----------------------------
# Script Generator
# -----------------------------
def transform_to_script(text, tone="Motivational", length="short"):
    sentences = text.split(". ")
    core = sentences[0] if sentences else text
    if length == "medium" and len(sentences) > 1:
        core = ". ".join(sentences[:2])
    elif length == "long" and len(sentences) > 2:
        core = ". ".join(sentences[:3])

    hooks = [
        f"Let's discuss {tone.lower()} and {core.split()[0]}.",
        f"Here's something about {core.split()[0]}.",
        f"Many overlook this about {core.split()[0]}."
    ]
    closings = [
        "Reflect on this today.",
        "Apply this to your life.",
        "Let this inspire your actions."
    ]
    return f"{random.choice(hooks)} {core}. {random.choice(closings)}"

def generate_script(topic, tone="Motivational", length="short"):
    topic_lower = topic.lower()
    if topic_lower in THEMES:
        data = THEMES[topic_lower]
        return (
            f"{random.choice(data['hooks'])} "
            f"{random.choice(data['insights'])} "
            f"{random.choice(data['closings'])}"
        )
    researched = research_topic(topic)
    if researched:
        return transform_to_script(researched, tone, length)
    return f"Unable to generate content for '{topic}'"

# -----------------------------
# Social Media Caption Generator (Simulated AI)
# -----------------------------
def generate_captions(script):
    captions = [
        f"🔥 {script[:50]}... #motivation #dailyinspiration",
        f"💡 Thought for the day: {script[:60]}... #leadership #growth",
        f"🙏 Remember: {script[:55]}... #faith #hope",
        f"⚡ {script[:60]}... #success #consistency"
    ]
    return random.sample(captions, min(3, len(captions)))

# -----------------------------
# Save Script
# -----------------------------
def save_script(script, topic, idx=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{topic}_script_{timestamp}"
    if idx is not None:
        filename += f"_variation{idx+1}"
    filename += ".txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(script)
    return filename

# -----------------------------
# GUI Functions
# -----------------------------
def on_generate():
    topic = topic_entry.get().strip()
    if not topic:
        return
    tone = tone_var.get()
    length = length_var.get()
    try:
        variations = int(variation_entry.get())
        if variations < 1:
            variations = 1
    except:
        variations = 1

    output_box.delete("0.0", tk.END)
    captions_box.delete("0.0", tk.END)
    history_box.configure(state=tk.NORMAL)
    history_box.insert(tk.END, f"=== Topic: {topic} | Tone: {tone} | Length: {length} ===\n")

    for i in range(variations):
        script = generate_script(topic, tone, length)
        output_box.insert(tk.END, f"Variation {i+1}:\n{script}\n\n")
        history_box.insert(tk.END, f"{script}\n\n")
        # Generate captions
        for cap in generate_captions(script):
            captions_box.insert(tk.END, f"{cap}\n")
        save_script(script, topic, i)

    history_box.configure(state=tk.DISABLED)
    status_label.configure(text=f"Generated {variations} variation(s) for '{topic}'.")

def copy_to_clipboard(box):
    text = box.get("0.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)

# -----------------------------
# GUI Setup
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("🤖 AI-Like Content Studio Dashboard")
root.geometry("1100x850")

# Animated Gradient Background
bg_frame = ctk.CTkFrame(root, fg_color=("gray10", "gray25"))
bg_frame.pack(fill="both", expand=True)

# Title
title_label = ctk.CTkLabel(bg_frame, text="💡 AI-Like Content Studio", font=ctk.CTkFont(size=26, weight="bold"))
title_label.pack(pady=15)

# Input Frame
input_frame = ctk.CTkFrame(bg_frame)
input_frame.pack(pady=10, padx=20, fill="x")

# Topic
ctk.CTkLabel(input_frame, text="Topic:", width=70).grid(row=0,column=0,padx=5,pady=5)
topic_entry = ctk.CTkEntry(input_frame, width=300)
topic_entry.grid(row=0,column=1,padx=5,pady=5)

# Tone
ctk.CTkLabel(input_frame, text="Tone:", width=70).grid(row=0,column=2,padx=5,pady=5)
tone_var = tk.StringVar(value="Motivational")
ctk.CTkOptionMenu(input_frame, variable=tone_var,
                  values=["Motivational","Spiritual","Professional","Casual","Humorous"]).grid(row=0,column=3,padx=5,pady=5)

# Length
ctk.CTkLabel(input_frame, text="Length:", width=70).grid(row=0,column=4,padx=5,pady=5)
length_var = tk.StringVar(value="short")
ctk.CTkOptionMenu(input_frame, variable=length_var, values=["short","medium","long"]).grid(row=0,column=5,padx=5,pady=5)

# Variations
ctk.CTkLabel(input_frame, text="Variations:", width=70).grid(row=0,column=6,padx=5,pady=5)
variation_entry = ctk.CTkEntry(input_frame, width=60)
variation_entry.insert(0,"1")
variation_entry.grid(row=0,column=7,padx=5,pady=5)

# Buttons Frame
button_frame = ctk.CTkFrame(bg_frame)
button_frame.pack(pady=10)

generate_btn = ctk.CTkButton(button_frame, text="Generate", width=150, command=on_generate)
generate_btn.grid(row=0,column=0,padx=10,pady=10)
copy_btn = ctk.CTkButton(button_frame, text="Copy Content", width=150, command=lambda: copy_to_clipboard(output_box))
copy_btn.grid(row=0,column=1,padx=10,pady=10)
copy_cap_btn = ctk.CTkButton(button_frame, text="Copy Captions", width=150, command=lambda: copy_to_clipboard(captions_box))
copy_cap_btn.grid(row=0,column=2,padx=10,pady=10)

# Tabbed Output
tab_view = ctk.CTkTabview(bg_frame)
tab_view.pack(pady=10, padx=20, fill="both", expand=True)
tab_view.add("Content")
tab_view.add("Captions")
tab_view.add("History")

# Output boxes
output_box = ctk.CTkTextbox(tab_view.tab("Content"))
output_box.pack(expand=True, fill="both", padx=10, pady=10)

captions_box = ctk.CTkTextbox(tab_view.tab("Captions"))
captions_box.pack(expand=True, fill="both", padx=10, pady=10)

history_box = ctk.CTkTextbox(tab_view.tab("History"))
history_box.pack(expand=True, fill="both", padx=10, pady=10)
history_box.configure(state="disabled")

# Status
status_label = ctk.CTkLabel(bg_frame, text="", font=ctk.CTkFont(size=12))
status_label.pack(pady=5)

root.mainloop()
