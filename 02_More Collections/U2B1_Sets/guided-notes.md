# 🎯 Python Sets

**Guided Notes** - Follow along in your Python environment!

---

## 1️⃣ Creating Sets - The Basics

Sets are **unordered collections of unique elements**. Think of them like a bag where duplicates automatically disappear!

![Python Sets - Creation and Characteristics](python_sets_1_basics.svg)
*📊 Visual Reference: Set Creation & Characteristics*

```python
# ============================================
# Creating Sets
# ============================================

# Method 1: Using curly braces {}
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # {'cherry', 'banana', 'apple'} - order may vary!

# Method 2: Using set() constructor
numbers = set([1, 2, 3, 2, 1])  # From a list
print(numbers)  # {1, 2, 3} - duplicates removed!

# Converting string to set (each character becomes an element)
letters = set('hello')
print(letters)  # {'h', 'e', 'l', 'o'} - only one 'l'!
```

> ⚠️ **Common Mistake: Empty Set**
> 
> `{}` creates an empty **dictionary**, NOT a set!
> Use `set()` to create an empty set.

```python
# Creating an empty set
empty_dict = {}        # This is a DICTIONARY!
empty_set = set()      # This is a SET!

print(type(empty_dict))  # <class 'dict'>
print(type(empty_set))   # <class 'set'>
```

> ✏️ **Try It Yourself!**
> 
> Create a set called `my_hobbies` with at least 3 hobbies. Then try adding a duplicate - what happens?

---

## 2️⃣ Set Characteristics - What Makes Sets Special

Sets have four key characteristics that make them different from lists:

| Characteristic | Sets | Lists |
|----------------|------|-------|
| **Ordered** | ❌ No guaranteed order | ✅ Maintains insertion order |
| **Duplicates** | ❌ Not allowed | ✅ Allowed |
| **Indexing** | ❌ Cannot use `[0]` | ✅ Can use `[0]` |
| **Membership Test** | ⚡ O(1) - Super fast! | 🐌 O(n) - Slower |

```python
# Demonstrating set characteristics
my_set = {3, 1, 4, 1, 5, 9, 2, 6}
print(my_set)  # {1, 2, 3, 4, 5, 6, 9} - sorted? No! Just happens to look that way

# Cannot index into a set
# print(my_set[0])  # TypeError: 'set' object is not subscriptable

# But you CAN iterate through a set
for num in my_set:
    print(num, end=' ')  # Prints each number (order not guaranteed)

# Fast membership testing - this is where sets SHINE!
print(5 in my_set)   # True - checked instantly!
print(10 in my_set)  # False
```

> 💡 **Why is membership testing so fast?**
> 
> Sets use a **hash table** internally. Instead of checking every element (like a list does), it calculates where the element *would be* and checks directly!

---

## 3️⃣ Modifying Sets - Add & Remove

Sets are mutable - you can add and remove elements after creation.

![Python Sets - Methods for Adding and Removing](python_sets_3_methods.svg)
*📊 Visual Reference: Set Methods (add, remove, discard, etc.)*

### Adding Elements

```python
# ============================================
# Adding Elements
# ============================================
colors = {'red', 'blue'}

# add() - Add a single element
colors.add('green')
print(colors)  # {'red', 'blue', 'green'}

# Adding a duplicate does nothing (no error!)
colors.add('red')
print(colors)  # {'red', 'blue', 'green'} - still only one 'red'

# update() - Add multiple elements from any iterable
colors.update(['yellow', 'purple'])
print(colors)  # {'red', 'blue', 'green', 'yellow', 'purple'}

# You can even update from a string (each char is added)
letters = set()
letters.update('abc')
print(letters)  # {'a', 'b', 'c'}
```

### Removing Elements

```python
# ============================================
# Removing Elements
# ============================================
fruits = {'apple', 'banana', 'cherry', 'date'}

# remove() - Remove an element (raises KeyError if not found!)
fruits.remove('banana')
print(fruits)  # {'apple', 'cherry', 'date'}

# fruits.remove('mango')  # KeyError: 'mango'

# discard() - Remove an element (NO error if not found - safer!)
fruits.discard('cherry')  # Removes cherry
fruits.discard('mango')   # Does nothing, no error!
print(fruits)  # {'apple', 'date'}

# pop() - Remove and return an ARBITRARY element
removed = fruits.pop()
print(f"Removed: {removed}")  # Could be 'apple' or 'date'!

# clear() - Remove ALL elements
fruits.clear()
print(fruits)  # set()
```

> ✏️ **Try It Yourself!**
> 
> Create a set of 5 numbers. Practice using `add()`, `remove()`, and `discard()`. What happens when you try to remove something that isn't there?

---

## 4️⃣ Set Operations - The Power of Sets!

This is where sets really shine! Mathematical set operations let you compare and combine sets easily.

![Python Sets - Operations with Venn Diagrams](python_sets_2_operations.svg)
*📊 Visual Reference: Set Operations (Union, Intersection, Difference)*

```python
# Let's work with two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# ============================================
# UNION (|) - All elements from BOTH sets
# ============================================
print(A | B)            # {1, 2, 3, 4, 5, 6}
print(A.union(B))       # {1, 2, 3, 4, 5, 6}

# ============================================
# INTERSECTION (&) - Only elements in BOTH sets
# ============================================
print(A & B)            # {3, 4}
print(A.intersection(B)) # {3, 4}

# ============================================
# DIFFERENCE (-) - Elements in A but NOT in B
# ============================================
print(A - B)            # {1, 2}
print(A.difference(B))   # {1, 2}
print(B - A)            # {5, 6} - Order matters!

# ============================================
# SYMMETRIC DIFFERENCE (^) - Elements in A OR B, but NOT both
# ============================================
print(A ^ B)            # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```

> 💡 **Operators vs Methods**
> 
> **Operators** (`|`, `&`, `-`, `^`) require both sides to be sets.
> 
> **Methods** (`.union()`, etc.) can accept any iterable (list, tuple, etc.)!

```python
# Method advantage: Works with any iterable!
my_set = {1, 2, 3}
my_list = [3, 4, 5]

print(my_set.union(my_list))  # {1, 2, 3, 4, 5} - Works!
# print(my_set | my_list)  # TypeError! Can't use | with a list
```

---

## 5️⃣ Set Comparisons - Subsets & Supersets

Check relationships between sets - is one contained within another?

![Python Sets - Subset and Superset Comparisons](python_sets_4_comparisons.svg)
*📊 Visual Reference: Set Comparisons (Subset, Superset, Disjoint)*

```python
small = {1, 2}
big = {1, 2, 3, 4}
same = {1, 2}
different = {5, 6}

# issubset() - Is every element of small also in big?
print(small.issubset(big))     # True - {1,2} ⊆ {1,2,3,4}
print(small <= big)            # True - same thing with operator

# issuperset() - Does big contain all elements of small?
print(big.issuperset(small))   # True - {1,2,3,4} ⊇ {1,2}
print(big >= small)            # True - same thing with operator

# Proper subset/superset (must be different sizes)
print(small < big)             # True - proper subset
print(small < same)            # False - same size!
print(small <= same)           # True - subset (can be equal)

# isdisjoint() - Do the sets share ANY elements?
print(small.isdisjoint(different))  # True - no shared elements
print(small.isdisjoint(big))        # False - they share 1 and 2
```

---

## 6️⃣ Practical Examples - Real World Uses

Let's see sets in action with common programming tasks!

```python
# ============================================
# Example 1: Remove Duplicates from a List
# ============================================
names = ['alice', 'bob', 'alice', 'carol', 'bob', 'alice']
unique_names = list(set(names))
print(unique_names)  # ['carol', 'alice', 'bob'] - order may vary!

# ============================================
# Example 2: Find Common Friends
# ============================================
alice_friends = {'bob', 'carol', 'dave', 'eve'}
bob_friends = {'alice', 'carol', 'frank', 'eve'}

mutual_friends = alice_friends & bob_friends
print(f"Mutual friends: {mutual_friends}")  # {'carol', 'eve'}

# ============================================
# Example 3: Fast Membership Checking
# ============================================
valid_users = {'admin', 'moderator', 'user', 'guest'}

def check_role(role):
    if role in valid_users:  # O(1) - instant!
        print(f"✅ '{role}' is a valid role")
    else:
        print(f"❌ '{role}' is NOT valid")

check_role('admin')    # ✅ 'admin' is a valid role
check_role('hacker')   # ❌ 'hacker' is NOT valid

# ============================================
# Example 4: Set Comprehension
# ============================================
# Just like list comprehension, but with {}
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# With condition
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

> ✏️ **Try It Yourself!**
> 
> You have two lists of favorite movies from two friends:
> ```python
> friend1 = ['Inception', 'Avatar', 'Titanic', 'Matrix']
> friend2 = ['Avatar', 'Jaws', 'Matrix', 'Alien']
> ```
> Use sets to find:
> 1. Movies they both like
> 2. All unique movies
> 3. Movies only friend1 likes

---

## 7️⃣ Frozenset - Immutable Sets

Sometimes you need a set that can't be changed. Enter `frozenset`!

![Python Frozensets - Immutable Sets](python_sets_5_frozensets.svg)
*📊 Visual Reference: Frozensets (Immutable Sets)*

```python
# Creating a frozenset
immutable = frozenset([1, 2, 3])
print(immutable)  # frozenset({1, 2, 3})

# Cannot modify!
# immutable.add(4)  # AttributeError: no 'add' method

# Why use frozenset?
# 1. Can be used as dictionary keys
groups = {
    frozenset(['alice', 'bob']): 'Team A',
    frozenset(['carol', 'dave']): 'Team B'
}

# 2. Can be elements in another set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}
```

> 💡 **Remember!**
> 
> Regular sets can't be dictionary keys or set elements because they're mutable (changeable). Frozensets can because they're immutable (unchangeable) and therefore hashable!

---

## 📝 Quick Reference Summary

| Operation | Operator | Method | Result |
|-----------|----------|--------|--------|
| Union | `A \| B` | `A.union(B)` | All elements from both |
| Intersection | `A & B` | `A.intersection(B)` | Only common elements |
| Difference | `A - B` | `A.difference(B)` | In A but not B |
| Symmetric Diff | `A ^ B` | `A.symmetric_difference(B)` | In A or B, not both |
| Subset | `A <= B` | `A.issubset(B)` | True if A ⊆ B |
| Superset | `A >= B` | `A.issuperset(B)` | True if A ⊇ B |

### Common Methods

| Method | Description |
|--------|-------------|
| `add(x)` | Add element x |
| `remove(x)` | Remove x (raises error if not found) |
| `discard(x)` | Remove x (no error if not found) |
| `pop()` | Remove and return arbitrary element |
| `clear()` | Remove all elements |
| `update(iterable)` | Add all elements from iterable |
| `isdisjoint(other)` | True if no common elements |

---

🐍 **Python Sets - Now you're ready for the activity!** 🎯
