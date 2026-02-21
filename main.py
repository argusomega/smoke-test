def greeting(name="World"):
    return f"Hello, {name}!"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="A simple greeting CLI.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greeting(args.name))


if __name__ == "__main__":
    main()
