"""
Testing and Debugging in Python - Starter Code

This starter file provides examples and a foundation for learning
testing and debugging practices. Complete the tasks by writing tests,
debugging code, and handling exceptions.
"""

import unittest
from typing import List

# ============================================================================
# TASK 1: Write Simple Unit Tests
# ============================================================================

# TODO: Define simple functions to test
# Example function (you can modify or replace these):
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def divide(a: int, b: int) -> float:
    """Divide a by b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def find_max(numbers: List[int]) -> int:
    """Find the maximum number in a list."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


# TODO: Create a test class that inherits from unittest.TestCase
# Write test methods for the functions above
class TestMathFunctions(unittest.TestCase):
    """Test cases for math functions."""
    
    # TODO: Write test_add with multiple test cases
    # Test normal case: add(2, 3) should equal 5
    # Test negative numbers: add(-1, 5) should equal 4
    # Test zero: add(0, 0) should equal 0
    
    # TODO: Write test_divide with multiple test cases
    # Test normal case: divide(10, 2) should equal 5.0
    # Test that divide by zero raises ValueError
    
    # TODO: Write test_find_max with multiple test cases
    # Test normal case: find_max([3, 1, 4, 1, 5]) should equal 5
    # Test that empty list raises ValueError


# ============================================================================
# TASK 2: Use the Python Debugger
# ============================================================================

def buggy_function(numbers: List[int]) -> int:
    """
    TODO: This function has a bug. Use pdb to debug it.
    
    Instructions:
    1. Add: import pdb; pdb.set_trace()
    2. Run: python starter-code.py
    3. Use 'n' to step, 'p variable' to inspect, 'c' to continue
    4. Find the bug and fix it
    """
    total = 0
    for i in range(len(numbers)):
        total = numbers[i]  # BUG: This should be += not =
    return total


# TODO: Document the bug you found:
# Bug description: ___________________________________________
# How you fixed it: __________________________________________


# ============================================================================
# TASK 3: Handle Exceptions with Try/Except
# ============================================================================

def safe_divide(a: int, b: int) -> str:
    """
    TODO: Implement exception handling for division.
    Use try/except to catch exceptions and return helpful messages.
    """
    try:
        # TODO: Perform division
        pass
    except ZeroDivisionError:
        # TODO: Handle division by zero
        pass
    except TypeError:
        # TODO: Handle invalid input types
        pass


def read_file_safely(filename: str) -> str:
    """
    TODO: Implement exception handling for file operations.
    """
    try:
        # TODO: Open and read file
        pass
    except FileNotFoundError:
        # TODO: Handle missing file
        pass
    except Exception as e:
        # TODO: Handle other unexpected errors
        pass


def parse_integer(value: str) -> int:
    """
    TODO: Implement exception handling for type conversion.
    """
    try:
        # TODO: Convert string to integer
        pass
    except ValueError:
        # TODO: Handle invalid number format
        pass


# ============================================================================
# TASK 4 (Stretch): Intentional Errors for Learning
# ============================================================================

def demonstrate_errors():
    """
    TODO: Create intentional errors to understand error messages.
    Uncomment one at a time, run it, read the error, then fix it.
    
    Common error types to practice:
    - TypeError: Wrong data type
    - ValueError: Invalid value
    - KeyError: Missing dictionary key
    - IndexError: List index out of range
    """
    
    # TypeError example:
    # result = "5" + 3  # Can't add string and int
    
    # ValueError example:
    # number = int("not a number")
    
    # KeyError example:
    # data = {"name": "Alice"}
    # print(data["age"])
    
    # IndexError example:
    # numbers = [1, 2, 3]
    # print(numbers[10])


# ============================================================================
# Main: Run Tests
# ============================================================================

if __name__ == "__main__":
    # Run the test suite
    print("Running unit tests...\n")
    unittest.main(argv=[''], exit=False)
    
    # TODO: Once tests pass, uncomment to debug:
    # print("\nTesting buggy function...")
    # result = buggy_function([1, 2, 3, 4, 5])
    # print(f"Result: {result}")
