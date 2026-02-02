"""
============================================
Python Sets - Guided Notes
============================================
Follow along as we explore Python sets!
Run each section to see the output.

Press F5 or Run to execute the entire file,
or run sections individually in your IDE.
"""

# ============================================
# DEMO 1: Creating Sets
# ============================================
# Sets are unordered collections of UNIQUE elements.
# Think of them like a bag where duplicates disappear!

print("=" * 50)
print("DEMO 1: Creating Sets")
print("=" * 50)

# Method 1: Using curly braces {}
fruits = {'apple', 'banana', 'cherry'}
print(f"fruits = {fruits}")

# Method 2: Using set() constructor - great for converting!
numbers_list = [1, 2, 3, 2, 1, 4, 3, 5]
numbers_set = set(numbers_list)
print(f"\nOriginal list: {numbers_list}")
print(f"Converted to set: {numbers_set}")
print("Notice the duplicates are gone!")

# Converting a string to a set
word = "mississippi"
letters = set(word)
print(f"\nLetters in '{word}': {letters}")

# IMPORTANT: Empty set vs empty dict!
empty_dict = {}          # This is a DICTIONARY
empty_set = set()        # This is a SET
print(f"\ntype({{}}) = {type(empty_dict)}")
print(f"type(set()) = {type(empty_set)}")

input("\n[Press Enter to continue to Demo 2...]\n")


# ============================================
# DEMO 2: Set Characteristics
# ============================================
print("=" * 50)
print("DEMO 2: Set Characteristics")
print("=" * 50)

my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
print(f"Created: {{3, 1, 4, 1, 5, 9, 2, 6, 5, 3}}")
print(f"Result:  {my_set}")
print("↳ Duplicates removed, order not guaranteed!")

# Cannot index a set!
print("\n⚠️ Sets don't support indexing:")
print("   my_set[0] would raise TypeError!")
# Uncomment to see the error:
# print(my_set[0])

# But you CAN iterate!
print("\nIterating through the set:")
for num in my_set:
    print(f"  → {num}")

# Fast membership testing - O(1)!
print("\n⚡ Membership testing (super fast!):")
print(f"  5 in my_set → {5 in my_set}")
print(f"  99 in my_set → {99 in my_set}")

input("\n[Press Enter to continue to Demo 3...]\n")


# ============================================
# DEMO 3: Adding & Removing Elements
# ============================================
print("=" * 50)
print("DEMO 3: Adding & Removing Elements")
print("=" * 50)

# Adding elements
colors = {'red', 'blue'}
print(f"Starting set: {colors}")

colors.add('green')
print(f"After add('green'): {colors}")

colors.add('red')  # Adding duplicate - no effect!
print(f"After add('red'): {colors} ← No change!")

colors.update(['yellow', 'purple', 'orange'])
print(f"After update([...]): {colors}")

# Removing elements
print("\n--- Removing Elements ---")
colors.discard('yellow')  # Safe - no error if missing
print(f"After discard('yellow'): {colors}")

colors.discard('pink')  # No error even though 'pink' isn't there!
print(f"After discard('pink'): {colors} ← No error!")

colors.remove('purple')  # Will error if not found!
print(f"After remove('purple'): {colors}")

# Uncomment to see the KeyError:
# colors.remove('pink')  # KeyError!

# pop() - removes arbitrary element
removed = colors.pop()
print(f"\npop() removed: '{removed}'")
print(f"Set is now: {colors}")

input("\n[Press Enter to continue to Demo 4...]\n")


# ============================================
# DEMO 4: Set Operations (The Good Stuff!)
# ============================================
print("=" * 50)
print("DEMO 4: Set Operations")
print("=" * 50)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")
print()

# Union - everything from both
print("UNION (A | B) - All elements from both sets:")
print(f"  A | B = {A | B}")
print(f"  A.union(B) = {A.union(B)}")
print()

# Intersection - only shared elements
print("INTERSECTION (A & B) - Only elements in BOTH:")
print(f"  A & B = {A & B}")
print(f"  A.intersection(B) = {A.intersection(B)}")
print()

# Difference - in one but not the other
print("DIFFERENCE (A - B) - In A but NOT in B:")
print(f"  A - B = {A - B}")
print(f"  B - A = {B - A}  ← Order matters!")
print()

# Symmetric Difference - in one OR other, not both
print("SYMMETRIC DIFFERENCE (A ^ B) - In A or B, NOT both:")
print(f"  A ^ B = {A ^ B}")
print()

# Quick visual:
print("Visual Summary:")
print("  A:     {1, 2, 3, 4}")
print("  B:         {3, 4, 5, 6}")
print("  ─────────────────────")
print("  A | B: {1, 2, 3, 4, 5, 6}  ← Union")
print("  A & B:     {3, 4}          ← Intersection")
print("  A - B: {1, 2}              ← Difference")
print("  A ^ B: {1, 2, 5, 6}        ← Symmetric Diff")

input("\n[Press Enter to continue to Demo 5...]\n")


# ============================================
# DEMO 5: Set Comparisons
# ============================================
print("=" * 50)
print("DEMO 5: Set Comparisons")
print("=" * 50)

small = {1, 2}
big = {1, 2, 3, 4, 5}
same = {2, 1}  # Same as small, different order
other = {7, 8, 9}

print(f"small = {small}")
print(f"big = {big}")
print(f"same = {same}")
print(f"other = {other}")
print()

# Subset checks
print("SUBSET (<=) - Is every element of A also in B?")
print(f"  small <= big → {small <= big}")
print(f"  small.issubset(big) → {small.issubset(big)}")
print(f"  small <= same → {small <= same}  ← Equal sets are subsets!")
print()

# Proper subset (must be strictly smaller)
print("PROPER SUBSET (<) - Subset AND smaller?")
print(f"  small < big → {small < big}")
print(f"  small < same → {small < same}  ← Equal, so False!")
print()

# Superset checks
print("SUPERSET (>=) - Does A contain all elements of B?")
print(f"  big >= small → {big >= small}")
print(f"  big.issuperset(small) → {big.issuperset(small)}")
print()

# Disjoint - no shared elements
print("DISJOINT - Do they share ANY elements?")
print(f"  small.isdisjoint(other) → {small.isdisjoint(other)}  ← No overlap")
print(f"  small.isdisjoint(big) → {small.isdisjoint(big)}  ← They share 1,2")

input("\n[Press Enter to continue to Demo 6...]\n")


# ============================================
# DEMO 6: Practical Examples
# ============================================
print("=" * 50)
print("DEMO 6: Practical Examples")
print("=" * 50)

# Example 1: Remove duplicates from a list
print("--- Example 1: Removing Duplicates ---")
emails = [
    "alice@email.com",
    "bob@email.com", 
    "alice@email.com",  # duplicate
    "carol@email.com",
    "bob@email.com"     # duplicate
]
unique_emails = list(set(emails))
print(f"Original list ({len(emails)} items): {emails}")
print(f"Unique ({len(unique_emails)} items): {unique_emails}")

# Example 2: Find mutual friends
print("\n--- Example 2: Social Network Analysis ---")
alice_friends = {'Bob', 'Carol', 'Dave', 'Eve', 'Frank'}
bob_friends = {'Alice', 'Carol', 'Eve', 'Grace', 'Henry'}

mutual = alice_friends & bob_friends
only_alice = alice_friends - bob_friends
all_connections = alice_friends | bob_friends

print(f"Alice's friends: {alice_friends}")
print(f"Bob's friends: {bob_friends}")
print(f"Mutual friends: {mutual}")
print(f"Friends only Alice knows: {only_alice}")
print(f"All unique people: {all_connections}")

# Example 3: Fast lookup
print("\n--- Example 3: Fast Membership Checking ---")
valid_commands = {'start', 'stop', 'pause', 'resume', 'quit', 'help'}

def process_command(cmd):
    if cmd.lower() in valid_commands:  # O(1) lookup!
        return f"✅ Executing '{cmd}'"
    else:
        return f"❌ Unknown command: '{cmd}'"

for cmd in ['start', 'HELP', 'dance', 'quit']:
    print(f"  {process_command(cmd)}")

# Example 4: Set comprehension
print("\n--- Example 4: Set Comprehension ---")
# Find unique word lengths
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = {len(word) for word in words}
print(f"Sentence: '{sentence}'")
print(f"Unique word lengths: {word_lengths}")

input("\n[Press Enter to continue to Demo 7...]\n")


# ============================================
# DEMO 7: Frozenset (Immutable Sets)
# ============================================
print("=" * 50)
print("DEMO 7: Frozenset (Immutable Sets)")
print("=" * 50)

# Creating a frozenset
fs = frozenset([1, 2, 3])
print(f"Frozenset: {fs}")
print(f"Type: {type(fs)}")

# Cannot modify!
print("\n⚠️ Cannot modify frozensets:")
print("   fs.add(4) would raise AttributeError!")
# Uncomment to see:
# fs.add(4)

# Why use frozenset?
print("\n✨ Frozensets can be dictionary keys:")
team_scores = {
    frozenset(['Alice', 'Bob']): 100,
    frozenset(['Carol', 'Dave']): 95
}
print(f"  {team_scores}")

print("\n✨ Frozensets can be set elements:")
groups = {frozenset([1, 2]), frozenset([3, 4])}
print(f"  Set of sets: {groups}")

# All read operations still work!
print("\n✨ All read operations work:")
print(f"  3 in fs → {3 in fs}")
print(f"  len(fs) → {len(fs)}")
print(f"  fs | {{4, 5}} → {fs | {4, 5}}")


# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 50)
print("SUMMARY - Key Takeaways")
print("=" * 50)
print("""
📝 SET CHARACTERISTICS:
   • Unordered (no indexing)
   • Unique elements only
   • Mutable (can add/remove)
   • Fast O(1) membership testing

📝 CREATING SETS:
   • {1, 2, 3} - curly braces
   • set([1, 2, 3]) - from iterable
   • set() - empty set (NOT {})

📝 MODIFYING SETS:
   • add(elem) - add one element
   • update(iterable) - add multiple
   • remove(elem) - remove (error if missing)
   • discard(elem) - remove (no error)
   • pop() - remove arbitrary element

📝 SET OPERATIONS:
   • Union: A | B or A.union(B)
   • Intersection: A & B or A.intersection(B)
   • Difference: A - B or A.difference(B)
   • Symmetric Diff: A ^ B or A.symmetric_difference(B)

📝 COMPARISONS:
   • A <= B - subset
   • A < B - proper subset
   • A >= B - superset
   • A.isdisjoint(B) - no overlap

📝 FROZENSET:
   • Immutable version of set
   • Can be dict keys or set elements
   • Created with frozenset([...])
""")

print("\n🎉 Great job! Now try the activity!")
