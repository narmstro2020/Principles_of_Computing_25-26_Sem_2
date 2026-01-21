"""
POC_U1B3 - Pair Programming Lab: Lambda Launchpad (40 minutes)
Names: ______________________  ______________________  (______________________)

Instructions:
- Complete each TODO.
- Run after each section to test.
- Use lambda where requested (don’t replace with def unless it says you may).

Roles (switch halfway)

Driver: types, runs the code, shares screen/keyboard
Navigator: reads instructions, watches for mistakes, explains “why”
(Optional 3rd) Coach: tests edge cases, keeps time

0–3 min: Assign roles, create file, run it once (expect failures).
3–18 min: Complete Parts A–C + run tests after each part.
18 min: Switch Driver/Navigator.
18–38 min: Complete Parts D–E.
38–40 min: Clean up: confirm all tests run, add names, push to GitHub

Each person will turn in a complete copy. So make sure all work is present for both students.
When finished turn this in on Github and Canvas.

This portion is worth 15 points.
"""

print("\n=== PART A: Lambda Basics ===\n")

# A1) TODO: Create a lambda named triple that multiplies a number by 3
triple = lambda x: 3 * x

# A2) TODO: Create a lambda named shout that takes a string and returns it uppercase with "!" at the end
shout = lambda s: s.upper() + "!"

# Tests
assert triple(4) == 12
assert shout("hello") == "HELLO!"
print("Part A passed!")

print("\n=== PART B: sorted(..., key=...) ===\n")

students = [
    {"name": "Ava", "grade": 91},
    {"name": "Ben", "grade": 84},
    {"name": "Cam", "grade": 98},
    {"name": "Dee", "grade": 91},
]

# B1) TODO: Sort students by grade (ascending). Use lambda in key=
by_grade = sorted(students, key=lambda x: x["grade"])

# B2) TODO: Sort students by name (alphabetical). Use lambda in key=
by_name = sorted(students, key=lambda x: x["name"])

# B3) TODO: Sort students by grade DESCENDING (highest first). Use sorted(..., reverse=True)
by_grade_desc = sorted(students, key=lambda x: x["grade"], reverse=True)

# Tests
assert [s["grade"] for s in by_grade] == [84, 91, 91, 98]
assert [s["name"] for s in by_name] == ["Ava", "Ben", "Cam", "Dee"]
assert [s["grade"] for s in by_grade_desc] == [98, 91, 91, 84]
print("Part B passed!")

print("\n=== PART C: min/max with key= ===\n")

# C1) TODO: Find the student with the highest grade using max(..., key=lambda ...)
top_student = max(students, key=lambda s: s["grade"])

# C2) TODO: Find the student with the lowest grade using min(..., key=lambda ...)
low_student = min(students, key=lambda s: s["grade"])  # TODO

# C3) TODO: Find the student whose NAME is longest (max by len(name))
longest_name_student = max(students, key=lambda s: len(s["name"]))  # TODO

# Tests
assert top_student["name"] == "Cam"
assert low_student["name"] == "Ben"
assert longest_name_student["name"] in ["Ava", "Ben", "Cam", "Dee"]  # all 3 letters; accept any
print("Part C passed!")

print("\n=== PART D: map() and filter() ===\n")

nums = [1, 2, 3, 4, 5, 6]

# D1) TODO: Use map + lambda to square each number
squares = list(map(lambda num: num * 2, nums))

# D2) TODO: Use filter + lambda to keep only numbers divisible by 3
div_by_3 = list(filter(lambda num: num % 3 == 0, nums))

# D3) TODO: Use filter + lambda to keep only odd numbers
odds = list(filter(lambda num: num % 2 != 0))

# Tests
assert squares == [1, 4, 9, 16, 25, 36]
assert div_by_3 == [3, 6]
assert odds == [1, 3, 5]
print("Part D passed!")

print("\n=== PART E: Real-ish Challenge (Key + Transform) ===\n")

products = [
    {"name": "Keyboard", "price": 49.99, "rating": 4.2},
    {"name": "Mouse", "price": 19.99, "rating": 4.5},
    {"name": "Monitor", "price": 199.99, "rating": 4.7},
    {"name": "USB Cable", "price": 7.99, "rating": 4.0},
]

# E1) TODO: Sort products by price (cheapest first)
by_price = None  # TODO

# E2) TODO: Sort products by rating (highest first)
by_rating_desc = None  # TODO

# E3) TODO: Use map + lambda to create a list of product names only
names = None  # TODO

# E4) TODO: Use filter + lambda to keep only products with rating >= 4.5
top_rated = None  # TODO

# E5) TODO: Combine ideas: get the NAME of the highest-rated product
best_name = None  # TODO

# Tests
assert [p["name"] for p in by_price] == ["USB Cable", "Mouse", "Keyboard", "Monitor"]
assert [p["name"] for p in by_rating_desc] == ["Monitor", "Mouse", "Keyboard", "USB Cable"]
assert names == ["Keyboard", "Mouse", "Monitor", "USB Cable"]
assert [p["name"] for p in top_rated] == ["Mouse", "Monitor"]
assert best_name == "Monitor"
print("Part E passed!")

print("\n✅ All parts passed. Nice work. Lambdas: tiny, sharp, and slightly dangerous.\n")
