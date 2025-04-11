import argparse


def sort(width: int, height: int, length: int, mass: int) -> str:
    heavy: bool = False
    bulky: bool = False

    if mass >= 20:
        heavy = True

    if (width * height * length) >= 1000000 or any(d >= 150 for d in (width, height, length)):
        bulky = True

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def run_tests():
    passed: int = 0
    failed: int = 0

    test_cases = [
        ((100, 100, 99, 19), "STANDARD"),   # Less than 1.000.000 cm3 and less than 20kg
        ((150, 10, 10, 19), "SPECIAL"),     # Less than 1.000.000 cm3, w = 150 and less than 20kg
        ((10, 150, 10, 19), "SPECIAL"),     # Less than 1.000.000 cm3, h = 150 and less than 20kg
        ((10, 10, 150, 19), "SPECIAL"),     # Less than 1.000.000 cm3, l = 150 and less than 20kg
        ((100, 100, 100, 19), "SPECIAL"),   # 1.000.000 cm3 and less than 20kg
        ((99, 99, 99, 20), "SPECIAL"),      # Less than 1.000.000 cm3 and 20kg
        ((100, 100, 100, 30), "REJECTED"),  # 1.000.000 cm3 and more than 20kg
        ((200, 200, 200, 30), "REJECTED"),  # 8.000.000 cm3 and more than 20kg
    ]

    for ((w, h, l, m), expected) in test_cases:
        result = sort(w, h, l, m)
        try:
            assert result == expected
            print(f"Passed: sort({w}, {h}, {l}, {m}) ==> '{expected}'")
            passed += 1
        except AssertionError:
            print(f"Failed: sort({w}, {h}, {l}, {m}) returned '{result}', expected '{expected}'")
            failed += 1

    print("\n📊 Results:")
    print(f"{passed} Passed")
    print(f"{failed} Failed")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, help="Width in cm")
    parser.add_argument("--height", type=int, help="Height in cm")
    parser.add_argument("--length", type=int, help="Length in cm")
    parser.add_argument("--mass", type=int, help="Mass in kg")
    parser.add_argument("--test", action="store_true", help="Run test cases")

    args = parser.parse_args()

    if args.test:
        run_tests()
    elif None not in (args.width, args.height, args.length, args.mass):
        result = sort(args.width, args.height, args.length, args.mass)
        print(f"Result: {result}")
    else:
        print("Pending parameters, check if width, height, length and mass are valid. Or use --test")

if __name__ == "__main__":
    main()
