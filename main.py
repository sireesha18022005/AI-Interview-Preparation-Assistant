from interview_question import interview_question
from feedback import evaluate

print("===== AI Interview Assistant =====")

role = input("Enter Role (Data Analyst/Software Engineer): ").strip()

role_map = {k.lower(): k for k in interview_question}

if role.lower() not in role_map:
    print("Role not found")
    exit()

role = role_map[role.lower()]

score = 0

for question in interview_question[role]:
    print("\nQuestion:")
    print(question)

    answer = input("Your Answer: ")

    marks, feedback = evaluate(answer)

    score += marks

    print("Feedback:", feedback)
    print("Marks:", marks)

print("\n===== Result =====")
print("Total Score:", score)

