def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def divide2(a: int, b: int) -> tuple[int, int]:
    """returns multiple and reminder of a divided by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    multiple = a // b
    reminder = a % b
    return multiple, reminder
