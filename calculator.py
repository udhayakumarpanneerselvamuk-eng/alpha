def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError(f"Unsupported operator: {operator}")


def main():
    print("Simple Calculator (+, -, *, /). Enter q to quit.")

    while True:
        expression = input("Expression (e.g. 2 + 3): ").strip()
        if expression.lower() == "q":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Please enter an expression in the form: number operator number")
            continue

        try:
            first = float(parts[0])
            second = float(parts[2])
            result = calculate(first, parts[1], second)
            print(f"Result: {result:g}")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
