"""When someone wants to make a change in python, they write a Python Enhancement Proposal (PEP)."""
"""Oldest PEP is PEP 8 -- Style Guide for Python Code."""


""" PEP recommends the following formatting guidelines:"""
# 1. Use 4 spaces per indentation level.
# 2. Limit all lines to a maximum of 79 characters.
# 3. Use blank lines to separate functions and classes, and larger blocks of code inside functions.
# 4. When possible, put comments on a separate line.
# 5. Use docstrings to describe all public classes and functions.
# 6. Use spaces around operators and after commas, but not directly inside parentheses, brackets
# 7. Name your classes and functions consistently (use CamelCase for classes and lowercase_with_underscores for functions and methods).
# 8. Use a consistent coding style throughout your project.
def greet_user(username):
    """Display a simple greeting to the user."""
    print(f"Hello, {username.title()}!")