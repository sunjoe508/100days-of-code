print("=== 100 Days of Code : Day 2 ===")

day = input("Which day is it? ")
learned = input("What did you learn today? ")
built = input("What did you build today? ")
reflection = input("One short reflection for today: ")

log_entry = f"""
Day {day}
Learned: {learned}
Built: {built}
Reflection: {reflection}
-----------------------------
"""

with open("100_days_log.txt", "a") as file:
    file.write(log_entry)

print("\n✅ Progress saved. Keep going. God is with you.")
