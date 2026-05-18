# 📘 Assignment: Testing and Debugging in Python

## 🎯 Objective

Master essential software engineering practices by learning to write unit tests, debug code effectively, and handle errors gracefully. You'll apply these skills to your existing code and future projects to catch bugs early and build more reliable programs.

## 📝 Tasks

### 🛠️ Write Simple Unit Tests with unittest

#### Description
Create your first unit tests using Python's built-in `unittest` module. Write tests for simple functions to verify they work correctly and to prevent future bugs.

#### Requirements
Completed program should:

- Import the `unittest` module
- Define at least 3 test functions using `TestCase` class methods (`test_*`)
- Test a simple function with multiple inputs (normal cases and edge cases)
- Use assertions like `assertEqual()`, `assertNotEqual()`, `assertTrue()`, `assertFalse()`
- Run all tests and verify they pass
- Document what each test is checking with clear comments

### 🛠️ Use the Python Debugger to Step Through Code

#### Description
Learn to use the Python debugger (pdb) to step through your code and understand what's happening at each line. Identify bugs by inspecting variable values and execution flow.

#### Requirements
Completed program should:

- Add `import pdb` and `pdb.set_trace()` breakpoints in a buggy function
- Run the program in debug mode and step through with `n` (next), `s` (step), and `c` (continue)
- Inspect variable values using `p variable_name`
- Identify and fix at least one bug using the debugger
- Document the bug you found and how debugging helped you fix it

### 🛠️ Handle Exceptions with Try/Except Blocks

#### Description
Write robust code that gracefully handles errors instead of crashing. Use try/except blocks to catch common exceptions and provide meaningful error messages.

#### Requirements
Completed program should:

- Identify at least 3 operations that could raise exceptions (e.g., division by zero, file not found, invalid input)
- Wrap each risky operation in a try/except block
- Catch specific exception types (not just generic `Exception`)
- Provide helpful error messages that tell users what went wrong
- Use `else` or `finally` clauses where appropriate
- Test your code with invalid inputs to verify error handling works

### 🛠️ Stretch Goal: Read and Interpret Error Messages

#### Description
Develop the skill to understand Python's error messages and use them to quickly locate and fix problems. Learn common error types and what they mean.

#### Requirements
Completed program should:

- Create a program that intentionally triggers several error types (`TypeError`, `ValueError`, `KeyError`, `IndexError`)
- Read and explain each error message's components: error type, description, and traceback
- Use the traceback to locate the exact line causing the error
- Document what each error type means and common causes
- Fix all intentional errors and verify the program runs without exceptions
