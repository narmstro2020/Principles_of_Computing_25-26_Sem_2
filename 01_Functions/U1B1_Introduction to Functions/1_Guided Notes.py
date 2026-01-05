"""
Unit 01 - Functions - Block 01 - Introduction to Functions
Guided Note
Students: fill in the blanks by writing answers in COMMENTS and completing the TODO code.
Run this file often to see what happens.

When finished turn this in via Github and Canvas.

This portion is worth 5 points.
"""


# ============================================================
# 0–3 min — Warm-Up: “Code déjà vu”
# Notice the repeated parts. What’s annoying about this?
# Functions help because they let us:
# ✅ ________________________________________________
# ✅ ________________________________________________
# ============================================================

print("Welcome!")
print("Here are the rules...")
print("Be kind.")
print("Welcome!")
print("Here are the rules...")
print("Be kind.")

print("\n" + "-" * 60 + "\n")


# ============================================================
# 3–7 min — What is a function?
# A function is a(n) ____________________________ of code
# that runs when it is ____________________________.
#
# Why we use functions (2 big reasons):
# 1) Organization: ____________________________________________
# 2) Reuse (DRY): DRY means “__________________________________”
# ============================================================


# ============================================================
# 7–12 min — Function vocabulary
# - Define a function = write it using the keyword __________
# - Call a function = _______________________________________
# - Parameter = a variable in the function ___________________
# - Argument = the actual value you __________________________
# ============================================================

def greet(name):  # name is a _____________
    print("Hello", name)

greet("Ada")      # "Ada" is an _____________

print("\n" + "-" * 60 + "\n")


# ============================================================
# 12–18 min — Anatomy of a function (the “shape”)
#
# Template:
# def function_name(parameters):
#     # function body (indented!)
#     statements
#     return value
#
# Label the parts of this:
# def add(a, b):
#     total = a + b
#     return total
#
# - function name: ____________________________
# - parameters: _______________________________
# - function body: ____________________________
# - return statement: _________________________
#
# Indentation rule:
# Everything inside the function must be ______________________.
# ============================================================

def add(a, b):
    total = a + b
    return total

print("add(3, 4) =", add(3, 4))

print("\n" + "-" * 60 + "\n")


# ============================================================
# 18–22 min — `print` vs `return` (super important)
# `print` shows something to the ____________________________.
# `return` sends a value back to the ________________________.
#
# Predict what happens BEFORE running:
# What prints to the screen?
# 1) _______________________________________
# 2) _______________________________________
#
# What is `result` equal to? ________________________________
#
# Key idea: If a function has no `return`, it returns _________.
# ============================================================

def double_print(x):
    print(x * 2)

result = double_print(5)
print("result =", result)

print("\n" + "-" * 60 + "\n")


# ============================================================
# 22–26 min — Function Scope (Local vs Global)
# Scope means: where a variable _____________________________
# (and can be used).
#
# Big rule:
# Variables created inside a function are __________ variables.
# - They exist only _________________________________________
# - They cannot be used _____________________________________
#
# Variables created outside a function are __________ variables.
# - They can be used ________________________________________
# - But functions usually should not depend on globals too much.
# ============================================================

# --- Example: Local variables stay in the function ---
def demo():
    x = 10  # local variable
    print("inside:", x)

demo()

# Predict:
# If we try to use x out here (outside demo), what happens?
# Does it work? YES / NO
# If NO, what error do you expect? ___________________________
#
# IMPORTANT: We are NOT running the "outside x" line yet because it will stop the program.
# You'll test it later in the OPTIONAL section at the bottom.

print()

# --- Example: Using a global variable (reading is allowed) ---
score = 0

def show_score():
    print("score =", score)

show_score()

# This works because the function is only _____________________ the global variable.

print()

# --- Example: Changing a global variable (tricky!) ---
# Predict: Does this run? YES / NO
# If NO, why? ________________________________________________

# This code is shown for learning; DON'T run it unless your teacher tells you to.
# def add_point_broken():
#     score = score + 1   # <-- what happens?

# Fix option 1 (recommended): Use parameters + return instead of globals
def add_point(score):
    return score + 1

score = add_point(score)
print("score after add_point(score) =", score)

# Fix option 2 (use carefully): global keyword
score2 = 0

def add_point_global():
    global score2
    score2 = score2 + 1

add_point_global()
print("score2 after add_point_global() =", score2)

# When should you use `global`?
# ➡️ Almost never. Prefer ________________________________.

print()

# Quick check:
# In this code, identify the local variables and the global variab
