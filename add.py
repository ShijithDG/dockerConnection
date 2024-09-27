# addition.py

def add_positive_integers(a: int, b: int) -> int:
    """Add two positive integers.

    Args:
        a (int): First positive integer.
        b (int): Second positive integer.

    Returns:
        int: The sum of a and b.

    Raises:
        ValueError: If a or b is not a positive integer.
    """
    if a <= 0 or b <= 0:  # Change < 0 to <= 0
        raise ValueError("Both numbers must be positive integers.")
    return a + b
