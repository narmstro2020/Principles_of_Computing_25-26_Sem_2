"""
POC_U1B2 - Unit 01 - Functions - Block 02
Pair Programming Lab: Function Builder Pack
Names: ______________________  ______________________  (______________________)

Instructions:
- Complete each TODO.
- Run after each function to test.
- Use parameters + return whenever possible.
- Avoid global variables.
- Prefer small, single-purpose functions.

Roles (switch halfway)
Driver: types, runs the code, shares screen/keyboard
Navigator: reads instructions, watches for mistakes, explains “why”

Suggested Timing (40 minutes)
0–5 min: Setup + run once (expect failures)
5–20 min: Parts A–B
20 min: Switch Driver/Navigator
20–35 min: Parts C–D
35–40 min: Part E + cleanup (all tests pass)

Each person will turn in a complete copy. Make sure all work is present for both students.
When finished turn this in on GitHub and Canvas.
This portion is worth 15 points.
"""

print("\n=== POC_U1B2 PAIR LAB: Function Builder Pack ===\n")


# ============================================================
# PART A: Warm-up (return values, not prints)
# ============================================================

def is_even(n):
    """TODO: Return True if n is even, otherwise False."""
    raise NotImplementedError


def average(a, b):
    """TODO: Return the average of a and b."""
    raise NotImplementedError


def seconds_to_minutes(seconds):
    """
    TODO:
    Return minutes as a float.
    Example: 90 seconds -> 1.5 minutes
    """
    raise NotImplementedError


# ============================================================
# PART B: Positional vs Keyword + Defaults
# ============================================================

def greet(name, punctuation="!"):
    """
    TODO:
    Return a greeting string.
    greet("Ada") -> "Hello, Ada!"
    greet("Ada", "?") -> "Hello, Ada?"
    """
    raise NotImplementedError


def percent_of(part, whole, digits=1):
    """
    TODO:
    Return a percentage string rounded to 'digits' decimals.
    percent_of(1, 4) -> "25.0%"
    percent_of(1, 4, digits=0) -> "25%"
    """
    raise NotImplementedError


# ============================================================
# PART C: Return vs Print (build strings)
# ============================================================

def line_total(quantity, price_each):
    """TODO: Return quantity * price_each."""
    raise NotImplementedError


def receipt_line(item, quantity, price_each):
    """
    TODO:
    Return a formatted receipt line string.
    Example: receipt_line("Soda", 2, 1.5) -> "Soda x2 = $3.00"
    (Tip: use line_total and format to 2 decimals)
    """
    raise NotImplementedError


# ============================================================
# PART D: Scope + Side Effects (mutating vs non-mutating)
# ============================================================

def add_item_mutating(items, new_item):
    """
    TODO:
    Add new_item to the existing list 'items' (mutates it).
    Return None.
    """
    raise NotImplementedError


def add_item_copy(items, new_item):
    """
    TODO:
    Return a NEW list that contains all items plus new_item.
    Do NOT mutate the original list.
    """
    raise NotImplementedError


# ============================================================
# PART E: Mini-Challenge (combine your functions)
# ============================================================

def build_receipt(items):
    """
    items is a list of tuples: (name, quantity, price_each)

    TODO:
    Return a multi-line receipt string that includes:
    - One receipt_line per item
    - A final TOTAL line formatted like: "TOTAL = $X.XX"

    Example return:

    Soda x2 = $3.00
    Chips x1 = $2.25
    TOTAL = $5.25
    """
    raise NotImplementedError


# ============================================================
# TESTS (Run often. Start by doing Part A and uncommenting.)
# ============================================================

print("=== TESTS (Uncomment as you finish each part) ===\n")

# --- Part A ---
# assert is_even(2) is True
# assert is_even(7) is False
# assert average(10, 20) == 15
# assert seconds_to_minutes(90) == 1.5

# --- Part B ---
# assert greet("Ada") == "Hello, Ada!"
# assert greet("Ada", "?") == "Hello, Ada?"
# assert percent_of(1, 4) == "25.0%"
# assert percent_of(1, 4, digits=0) == "25%"

# --- Part C ---
# assert line_total(3, 2.0) == 6.0
# assert receipt_line("Soda", 2, 1.5) == "Soda x2 = $3.00"

# --- Part D ---
# original = ["apple"]
# add_item_mutating(original, "banana")
# assert original == ["apple", "banana"]
# original2 = ["apple"]
# copy_list = add_item_copy(original2, "banana")
# assert original2 == ["apple"]            # original unchanged
# assert copy_list == ["apple", "banana"]  # new list returned

# --- Part E ---
# cart = [("Soda", 2, 1.5), ("Chips", 1, 2.25)]
# expected = "Soda x2 = $3.00\nChips x1 = $2.25\nTOTAL = $5.25"
# assert build_receipt(cart) == expected

print("When all asserts pass: push to GitHub, submit to Canvas. ✅")
