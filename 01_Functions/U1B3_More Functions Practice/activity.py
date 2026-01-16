"""
POC – Unit 01 – Functions Practice Activity #3
Blocks: U1B1 + U1B2 (Functions Basics + Building Stronger Functions)
Pair Programming Lab: Function Forge
Names: ______________________  ______________________  (______________________)

Instructions:
- Complete each TODO.
- Run after each function to test.
- Use parameters + return whenever possible.
- Avoid global variables (unless a TODO explicitly says otherwise).
- Keep functions small: one clear job each.

Roles (switch halfway)
Driver: types, runs the code, shares screen/keyboard
Navigator: reads instructions, watches for mistakes, explains “why”
(Optional 3rd) Coach: tests edge cases, keeps time

Timing (40 minutes total)
0–3 min: Assign roles, create file, run it once (expect failures).
3–18 min: Parts A–C
18 min: Switch Driver/Navigator
18–35 min: Parts D–F
35–40 min: Clean up + final run + push to GitHub

Turn in:
- Each person turns in a complete copy (both students have full work).
- Submit via GitHub + Canvas.

Worth: 15 points
"""

print("\n=== POC U1B1/U1B2: Function Forge ===\n")

# ------------------------------------------------------------
# Helpers for testing (DO NOT EDIT)
# ------------------------------------------------------------
def _assert_equal(actual, expected, msg=""):
    if actual != expected:
        raise AssertionError(f"{msg}\nExpected: {expected}\nActual:   {actual}")
    print(f"✅ {msg}".strip() or "✅ test passed")


# ============================================================
# PART A: Warm-up (Parameters + Return)
# ============================================================

# 1) TODO: write a function named shout(text) that returns the text
#    in ALL CAPS with an exclamation point at the end.
#    Example: shout("hi") -> "HI!"
def shout(text):
    # TODO
    pass


# 2) TODO: write a function named between(x, low, high)
#    Return True if x is between low and high (inclusive). Otherwise False.
def between(x, low, high):
    # TODO
    pass


print("\n--- PART A Tests ---")
_assert_equal(shout("hi"), "HI!", "shout('hi')")
_assert_equal(shout("Python"), "PYTHON!", "shout('Python')")
_assert_equal(between(5, 1, 10), True, "between(5, 1, 10)")
_assert_equal(between(1, 1, 10), True, "between(1, 1, 10)")
_assert_equal(between(11, 1, 10), False, "between(11, 1, 10)")


# ============================================================
# PART B: Input Validation (Defensive Programming)
# ============================================================

# 3) TODO: write a function safe_divide(a, b)
#    - If b == 0, return None
#    - Otherwise return a / b
def safe_divide(a, b):
    # TODO
    pass


# 4) TODO: write a function clamp(n, min_value, max_value)
#    - If n is smaller than min_value, return min_value
#    - If n is larger than max_value, return max_value
#    - Otherwise return n
def clamp(n, min_value, max_value):
    # TODO
    pass


print("\n--- PART B Tests ---")
_assert_equal(safe_divide(10, 2), 5.0, "safe_divide(10, 2)")
_assert_equal(safe_divide(10, 0), None, "safe_divide(10, 0)")
_assert_equal(clamp(5, 1, 10), 5, "clamp(5, 1, 10)")
_assert_equal(clamp(-3, 0, 10), 0, "clamp(-3, 0, 10)")
_assert_equal(clamp(99, 0, 10), 10, "clamp(99, 0, 10)")


# ============================================================
# PART C: Strings (U1B2-ish)
# ============================================================

# 5) TODO: write a function initials(full_name)
#    - full_name contains first and last name separated by spaces
#    - Return the initials in the form "F.L."
#    Example: "Ada Lovelace" -> "A.L."
#    Assume there are at least 2 words.
def initials(full_name):
    # TODO
    pass


print("\n--- PART C Tests ---")
_assert_equal(initials("Ada Lovelace"), "A.L.", "initials('Ada Lovelace')")
_assert_equal(initials("grace hopper"), "G.H.", "initials('grace hopper')")


print("\n🎉 If you reached this line with all ✅ tests, you are FUNCTION-FORGED.\n")
