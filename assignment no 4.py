# =================================================================
# 🚀 PYTHON LIST & MATRIX ASSIGNMENT PROGRAMS (By Waiz Imran) 🚀
# =================================================================

# ---------- QUESTION 1 ----------
print("\n📌 QUESTION 1: Print alternate elements of a list")
print("-"*50)
items = input("👉 Enter elements separated by spaces: ").split()
print("Original List:", items)
print("Alternate Elements:", items[::2])  # slicing with step 2
print("="*50)


# ---------- QUESTION 2 ----------
print("\n📌 QUESTION 2: Reverse a list without using reverse()")
print("-"*50)
items = input("👉 Enter elements separated by spaces: ").split()
reversed_list = items[::-1]  # reverse using slicing
print("Reversed List:", reversed_list)
print("="*50)


# ---------- QUESTION 3 ----------
print("\n📌 QUESTION 3: Find the largest number in a list (without max())")
print("-"*50)
numbers = list(map(int, input("👉 Enter numbers separated by spaces: ").split()))
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("✅ The largest number is:", largest)
print("="*50)


# ---------- QUESTION 4 ----------
print("\n📌 QUESTION 4: Rotate list elements")
print("-"*50)
user_list = input("👉 Enter elements separated by spaces: ").split()
rotated = user_list[-1:] + user_list[:-1]  # rotate last element to first
print("Rotated List:", rotated)
print("="*50)


# ---------- QUESTION 5 ----------
print("\n📌 QUESTION 5: Delete a word from a string")
print("-"*50)
sentence = input("👉 Enter a sentence: ")
word_to_delete = input("👉 Enter the word to delete: ")
new_sentence = sentence.replace(word_to_delete, "")
print("String after deletion:", new_sentence)
print("="*50)


# ---------- QUESTION 6 ----------
print("\n📌 QUESTION 6: Convert date from mm/dd/yyyy to Month dd, yyyy")
print("-"*50)
date = input("👉 Enter date in mm/dd/yyyy format: ")
month, day, year = date.split("/")  # split date into parts

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

month_name = months[int(month) - 1]
print(f"✅ Formatted Date: {month_name} {day}, {year}")
print("="*50)


# ---------- QUESTION 7 ----------
print("\n📌 QUESTION 7: Capitalize each word in a string")
print("-"*50)
text = "hello world"

capitalized = text[0].upper() + text[1:]

print("Result:", capitalized)

print("="*50)


# ---------- QUESTION 8 ----------
print("\n📌 QUESTION 8: Sum of each row in a matrix")
print("-"*50)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    total = 0
    for num in row:
        total += num
    print("Sum of row:", total)

print("="*50)


# ---------- QUESTION 9 ----------
print("\n📌 QUESTION 9: Add two matrices")
print("-"*50)
# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

# result matrix of same size
result = []

for i in range(len(A)):          # loop over rows
    row = []
    for j in range(len(A[0])):   # loop over columns
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Resultant Matrix after Addition:")
for r in result:
    print(r)

print("="*50)


# ---------- QUESTION 10 ----------
print("\n📌 QUESTION 10: Multiply two matrices")
print("-"*50)
# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# result matrix with size (rows of A) x (cols of B)
result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

# matrix multiplication
for i in range(len(A)):                 # loop over rows of A
    for j in range(len(B[0])):          # loop over cols of B
        for k in range(len(B)):         # loop over rows of B
            result[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix after Multiplication:")
for r in result:
    print(r)

print("="*50)
