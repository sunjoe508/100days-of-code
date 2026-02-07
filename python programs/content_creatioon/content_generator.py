import random
from datetime import datetime

THEMES = {
    "fear": {
        "hooks": [
            "Fear is not the enemy.",
            "That fear you feel?",
            "Most people are trapped by fear.",
            "Fear shows up before growth."
        ],
        "messages": [
            "It’s just a signal that you’re about to grow.",
            "It means you’re standing at the edge of something new.",
            "It survives because you keep listening to it.",
            "It only has power when you stop moving."
        ],
        "closings": [
            "Do it afraid.",
            "Move anyway.",
            "Start before you feel ready.",
            "Fear fades when action begins."
        ]
    },

    "consistency": {
        "hooks": [
            "Consistency beats motivation.",
            "You don’t need motivation.",
            "Small actions matter.",
            "Winning is boring."
        ],
        "messages": [
            "You just need to show up every day.",
            "Doing little things repeatedly changes everything.",
            "Results come from repetition, not hype.",
            "Success is built quietly."
        ],
        "closings": [
            "Show up again tomorrow.",
            "Repeat this daily.",
            "Trust the process.",
            "Stay consistent."
        ]
    }
}


def generate_script(theme):
    data = THEMES.get(theme.lower())
    if not data:
        return None

    hook = random.choice(data["hooks"])
    message = random.choice(data["messages"])
    closing = random.choice(data["closings"])

    script = f"{hook} {message} {closing}"
    return script


def save_script(script, theme):
    filename = f"{theme}_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(script)
    return filename


if __name__ == "__main__":
    print("Available themes: fear, consistency")
    theme = input("Choose a theme: ").strip()

    script = generate_script(theme)

    if script:
        file_saved = save_script(script, theme)
        print("\n🎤 Your Script:")
        print(script)
        print(f"\n✅ Saved as: {file_saved}")
    else:
        print("❌ Theme not found.")
