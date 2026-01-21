"""
POC_U1B3 - Lambda Expressions (Anonymous Functions) - Guided Notes (20 minutes)
Name: ________________________________   Date: _______________

Goal:
- Understand what lambda expressions are
- Know when to use lambda vs def
- Use lambda with sorted(), key=, min/max, map, filter

------------------------------------------------------------
0–2 min: Hook — “Functions are values”
------------------------------------------------------------
In Python, functions can be:
- stored in variables
- passed into other functions
- returned from functions

Example:
def add(a, b):
    return a + b

op = add
# op(2, 3) -> 5

------------------------------------------------------------
2–6 min: What is a lambda?
------------------------------------------------------------
A lambda is a(n) _________________________ function.
It is usually used for _____________________________.

Syntax:
lambda <parameters>: <expression>

Key rule:
- A lambda can only contain a single ______________________.
- That expression is automatically _______________________.

Examples:
square = lambda x: x * x
# square(5) -> ________

add = lambda a, b: a + b
# add(2, 3) -> ________

Compare to def:
def square(x):
    return x * x

When to prefer def:
- multi-step logic
- readability
- docstrings / type hints
- debugging

When lambda is great:
- quick one-liners (especially inside another function call)

------------------------------------------------------------
6–11 min: key= with sorted()
------------------------------------------------------------
One of the best uses of lambda is with key=.

Example list:
students = [
    {"name": "Ava", "grade": 91},
    {"name": "Ben", "grade": 84},
    {"name": "Cam", "grade": 98},
]

Sort by grade:
sorted_students = sorted(students, key=lambda s: s["grade"])

Fill in:
- key= expects a function that takes ______ item and returns a ______ to sort by.

Try it:
Sort by name (alphabetical):
sorted_by_name = sorted(students, key=lambda s: s["________"])

------------------------------------------------------------
11–15 min: min(), max(), and key=
------------------------------------------------------------
You can also use key= with min/max.

top_student = max(students, key=lambda s: s["grade"])
lowest_student = min(students, key=lambda s: s["grade"])

What do these return?
- max(...) returns the entire ______________________
- not just the grade number

------------------------------------------------------------
15–18 min: map() and filter() (quick intro)
------------------------------------------------------------
map(function, iterable) -> transforms each item
filter(function, iterable) -> keeps items where function returns True

nums = [1, 2, 3, 4, 5]

doubles = list(map(lambda n: n * 2, nums))
# doubles -> ________________________

evens = list(filter(lambda n: n % 2 == 0, nums))
# evens -> ________________________

Important note:
List comprehensions often read cleaner:
doubles2 = [n * 2 for n in nums]
evens2 = [n for n in nums if n % 2 == 0]

------------------------------------------------------------
18–20 min: Exit Ticket
------------------------------------------------------------
1) Write a lambda that takes x and returns x cubed:
cube = __________________________________________

2) Given words = ["hi", "hello", "yo", "welcome"]
Sort by length (shortest to longest) using lambda + sorted:
sorted_words = __________________________________________

3) True/False: A lambda can contain multiple statements. _______
"""
