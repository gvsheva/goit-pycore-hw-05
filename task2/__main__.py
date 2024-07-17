if __name__ == "__main__":
    import argparse

    from task2 import find_numbers, sum_numbers

    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=argparse.FileType(), help="Path to the file")
    args = ap.parse_args()
    s = sum_numbers(args.path.read(), find_numbers)
    print(f"Sum of numbers in the file: {s}")
