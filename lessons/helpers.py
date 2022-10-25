"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


#Idiom for making a module able to run as a program
#or have its global definitions imported elsewhere.
if __name__ == "__main___":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helpers.py was imported: {__name__}")