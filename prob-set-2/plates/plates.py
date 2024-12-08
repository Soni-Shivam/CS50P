def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    has_seen_digit = False
    for c in s[2:]:
        if c.isdigit():
            if not has_seen_digit and c == "0":
                return False
            has_seen_digit = True
        elif c.isalpha():
            if has_seen_digit:
                return False
        else:
            return False
    return True

main()
