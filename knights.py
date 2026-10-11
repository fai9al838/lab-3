from logic import *

AKnight, AKnave = Symbol("A is a Knight"), Symbol("A is a Knave")
BKnight, BKnave = Symbol("B is a Knight"), Symbol("B is a Knave")
CKnight, CKnave = Symbol("C is a Knight"), Symbol("C is a Knave")


def person(knight, knave):
    """Every person is a knight or a knave, never both."""
    return And(Or(knight, knave), Not(And(knight, knave)))


def says(knight, knave, statement):
    """A knight's statement is true; a knave's statement is false."""
    return And(Implication(knight, statement),
               Implication(knave, Not(statement)))


# Puzzle 0: A says "I am both a knight and a knave."
knowledge0 = And(
    person(AKnight, AKnave),
    says(AKnight, AKnave, And(AKnight, AKnave))
)

# Puzzle 1: A says "We are both knaves." B says nothing.
knowledge1 = And(
    person(AKnight, AKnave),
    person(BKnight, BKnave),
    says(AKnight, AKnave, And(AKnave, BKnave))
)

# Puzzle 2: A says "We are the same kind." B says "We are of different kinds."
same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
knowledge2 = And(
    person(AKnight, AKnave),
    person(BKnight, BKnave),
    says(AKnight, AKnave, same),
    says(BKnight, BKnave, Not(same))
)

# Bonus Puzzle 3
a_said_knave = says(AKnight, AKnave, AKnave)
a_said_knight = says(AKnight, AKnave, AKnight)
knowledge3 = And(
    person(AKnight, AKnave),
    person(BKnight, BKnave),
    person(CKnight, CKnave),
    Or(a_said_knight, a_said_knave),
    says(BKnight, BKnave, a_said_knave),
    says(BKnight, BKnave, CKnave),
    says(CKnight, CKnave, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for name, knowledge in puzzles:
        print(name)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()