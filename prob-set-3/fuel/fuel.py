def main():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int, fraction.split("/"))
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            fuel = numerator / denominator
            if fuel > 1:
                print("Fraction must be less than or equal to 1. Try again.")
                continue
            if fuel >= 0.99:
                print("F")
            elif fuel <= 0.01:
                print("E")
            else:
                print(f"{round(fuel * 100)}%")
            break  
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
if __name__ == "__main__":
    main()
