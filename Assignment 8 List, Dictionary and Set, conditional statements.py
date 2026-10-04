# Python Assignment 2: Data Structures - List, Dictionary, Set
# & Conditional Statements
# Solution prepared according to the assignment questions.

# ============================================================
# LIST (CREATION, MODIFICATION AND ACCESS)
# ============================================================

# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Anu", "Riya", "Meera", "Priya", "Zara"]

print("Initial age_list:", age_list)
print("Initial name_list:", name_list)

# 2. List Operations / Modifications

# a. Append "Yazhini" to name_list
name_list.append("Yazhini")
print("\nAfter appending Yazhini:", name_list)

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print("After inserting 30 at index 2:", age_list)

# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

# d. Pop the last element from age_list
popped_age = age_list.pop()
print("Popped last age:", popped_age)
print("After popping the last element:", age_list)

# e. Extend age_list with [29, 30, 26]
age_list.extend([29, 30, 26])
print("After extending age_list:", age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("age_list in descending order:", age_list)

# g. Find maximum age, minimum age and sum of all ages
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))

# 3. Accessing List Elements

# a. First element
print("\nFirst element of name_list:", name_list[0])

# b. Last element
print("Last element of name_list:", name_list[-1])

# c. Elements from index 2 to index 4
# [2:5] includes indexes 2, 3 and 4.
print("Elements from index 2 to index 4:", name_list[2:5])

# d. Reverse order
print("name_list in reverse order:", name_list[::-1])


# ============================================================
# DICTIONARY (CREATION, MODIFICATION AND ACCESS)
# ============================================================

# a. Dictionary with five students and marks from 0 to 100
student_marks = {
    "Anu": 75,
    "Riya": 88,
    "Meera": 92,
    "Priya": 68,
    "Zara": 95
}

print("\nInitial student_marks:", student_marks)

# b. Access and print the mark of a specific student
print("Mark of Zara:", student_marks["Zara"])

# c. Add Janani with a mark of 80
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update the mark of an older student to 82
student_marks["Anu"] = 82
print("After updating Anu's mark to 82:", student_marks)

# e. Print keys, values and key-value pairs
print("\nAll keys:", student_marks.keys())
print("All values:", student_marks.values())
print("All key-value pairs:", student_marks.items())


# ============================================================
# SETS (OPERATIONS)
# ============================================================

# a. Create my_set with the given values.
# Duplicate values are automatically removed by a set.
my_set = {"a", "e", "i", "o", "u", "a", "a", "i"}

print("\nmy_set:", my_set)
print("Explanation: A set stores only unique elements, so the")
print("duplicate 'a' and 'i' values are automatically removed.")

# b. Attempt to change my_set[4] = 's'.
# Sets do not support index-based assignment, so this raises TypeError.
try:
    my_set[4] = "s"
except TypeError as error:
    print("Error while trying my_set[4] = 's':", error)
    print("Explanation: Sets are unordered and do not support")
    print("item assignment using an index.")

# c. Create set1 and set2
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Union and intersection
print("\nset1:", set1)
print("set2:", set2)
print("Union of set1 and set2:", set1.union(set2))
print("Intersection of set1 and set2:", set1.intersection(set2))


# ============================================================