from my_project.calculator import add


def app() -> None:
    result = add(3, 5)
    print(f"The result of adding 3 and 5 is: {result}")


if __name__ == "__main__":
    app()
