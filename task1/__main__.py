if __name__ == "__main__":
    import argparse

    from task1 import caching_fibonacci

    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int, help="Number to calculate fibonacci")
    args = ap.parse_args()

    fib = caching_fibonacci()
    print(fib(args.n))
