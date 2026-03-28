# Quiz Game - Mera Pehla Project

# Questions aur answers ki list
questions = [
    "Pakistan ki capital kya hai? ",
    "2 + 2 kitna hota hai? ",
    "Python ek programming language hai? (haan/nahi) "
]

answers = [
    "islamabad",
    "4",
    "haan"
]

# Score shuru mein zero
score = 0

print("🎮 Quiz Game Mein Khush Amdeed!")
print("=" * 35)

# Har question poochna
for i in range(len(questions)):
    print(f"\nSawal {i+1}: {questions[i]}")
    user_answer = input("Aapka Jawab: ").lower().strip()
    
    if user_answer == answers[i]:
        print("✅ Sahi Jawab!")
        score += 1
    else:
        print(f"❌ Galat! Sahi jawab tha: {answers[i]}")

# Final score dikhana
print("\n" + "=" * 35)
print(f"🏆 Aapka Score: {score} / {len(questions)}")

if score == len(questions):
    print("🌟 Zabardast! Sab sahi!")
elif score >= len(questions) // 2:
    print("👍 Acha kiya! Aur practice karo!")
else:
    print("💪 Koi baat nahi, agli baar better karoge!")
import time
start = time.time()
# ... game code ...
end = time.time()
print(f"⏱️ Aapne {round(end-start)} seconds mein khela!")