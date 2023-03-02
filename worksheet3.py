# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-09-07
# DESCRIPTION: An assignment that gives us an introduction to conditionals

def earlier_name(name1: str, name2: str) -> str:
    names = [name1, name2]
    sortedNames = sorted(names)
    return sortedNames[0]


def ticket_price(age: int) -> float:
    if age >= 65:
        return 4.75
    elif age <= 12:
        return 4.25
    else:
        return 7.50


def format_name(first: str, last: str) -> str:
    if len(last) > 0:
        return last + ", " + first
    else:
        return first

def main():
    print(earlier_name("Jen","Paul"))
    print(earlier_name("Colin", "Colin"))
    print(ticket_price(7))
    print(ticket_price(21))
    print(ticket_price(101))
    print(format_name("Cherilyn", "Sarkisian"))
    print(format_name("Cher", ""))


if __name__ == "__main__":
    main()
