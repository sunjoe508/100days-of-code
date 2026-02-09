from datetime import date

today = date.today().isoformat()

print("=== 100 Days of Code | Day 3 ===")
print(f"Date: {today}\n")

# --- Input with validation ---
learned = input("What did you learn today? ").strip()
built = input("What did you build today? ").strip()
reflection = input("One short reflection: ").strip()

if not learned or not built or not reflection:
    print("\n❌ Empty input detected. Please be intentional.")
    exit()

# --- Handle streak ---
try:
    with open("streak.txt", "r") as f:
        last_date = f.read().strip()
except FileNotFoundError:
    last_date = ""

streak_continues = (last_date != today)

with open("streak.txt", "w") as f:
    f.write(today)

# --- Save log ---
entry = f"""
Date: {today}
Learned: {learned}
Built: {built}
Reflection: {reflection}
---------------------------
"""

with open("log.txt", "a") as f:
    f.write(entry)

# --- Output ---
print("\n✅ Entry saved successfully.")

if streak_continues:
    print("🔥 Streak maintained. Keep going.")
else:
    print("⚠️ You already logged today.")

print("God is with you. One day at a time.")
