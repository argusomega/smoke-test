def greeting(name="World", greeting="Hello"):
    return f"{greeting}, {name}!"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="A simple greeting CLI.")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument("--greeting", default="Hello", help="Greeting to use")
    args = parser.parse_args()
    print(greeting(args.name, args.greeting))


if __name__ == "__main__":
    main()
