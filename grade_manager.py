def get_grade(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def main():
    print("Welcome to the Student Grade Manager!")
    name = input("What's the student's name? ").strip()
    if not name:
        name = "Student"

    try:
        mark = float(input(f"Hi {name}, enter your mark (0-100): "))
        grade = get_grade(mark)
        print(f"\n{name}, you scored {mark:g}/100 and earned a grade of {grade}.")
        if grade == "A":
            print("Excellent work! Keep it up!")
        elif grade == "B":
            print("Great job! You're doing well.")
        elif grade == "C":
            print("Good effort. Keep practicing and you'll improve.")
        elif grade == "D":
            print("You're making progress. A little more practice can help.")
        else:
            print("Don't give up. Review the material and try again!")
    except ValueError as error:
        print(f"Sorry, that doesn't look like a valid mark. {error}")


if __name__ == "__main__":
    main()
