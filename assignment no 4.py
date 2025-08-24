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
text = input("👉 Enter a sentence: ")
capitalized = " ".join(word.capitalize() for word in text.split())
print("After Capitalization:", capitalized)
print("="*50)


# ---------- QUESTION 8 ----------
print("\n📌 QUESTION 8: Sum of each row in a matrix")
print("-"*50)
m = int(input("👉 Enter number of rows: "))
n = int(input("👉 Enter number of columns: "))

matrix = []
print("\nEnter matrix elements row by row:")
for i in range(m):
    row = [int(input(f"Element [{i+1},{j+1}]: ")) for j in range(n)]
    matrix.append(row)

print("\nMatrix and Row Sums:")
for i in range(m):
    print(matrix[i], "  Sum =", sum(matrix[i]))
print("="*50)


# ---------- QUESTION 9 ----------
print("\n📌 QUESTION 9: Add two matrices")
print("-"*50)
rows = int(input("👉 Enter number of rows: "))
cols = int(input("👉 Enter number of columns: "))

print("\nEnter elements of First Matrix:")
matrix1 = [[int(input(f"Element [{i+1},{j+1}]: ")) for j in range(cols)] for i in range(rows)]

print("\nEnter elements of Second Matrix:")
matrix2 = [[int(input(f"Element [{i+1},{j+1}]: ")) for j in range(cols)] for i in range(rows)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

print("\n✅ Resultant Matrix (After Addition):")
for row in result:
    print(row)
print("="*50)


# ---------- QUESTION 10 ----------
print("\n📌 QUESTION 10: Multiply two matrices")
print("-"*50)
rows1 = int(input("👉 Enter rows of first matrix: "))
cols1 = int(input("👉 Enter columns of first matrix: "))
rows2 = int(input("👉 Enter rows of second matrix: "))
cols2 = int(input("👉 Enter columns of second matrix: "))

if cols1 != rows2:
    print("❌ Matrix multiplication not possible! Columns of first must equal rows of second.")
else:
    print("\nEnter elements of First Matrix:")
    matrix1 = [[int(input(f"Element [{i+1},{j+1}]: ")) for j in range(cols1)] for i in range(rows1)]

    print("\nEnter elements of Second Matrix:")
    matrix2 = [[int(input(f"Element [{i+1},{j+1}]: ")) for j in range(cols2)] for i in range(rows2)]

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("\n✅ Resultant Matrix (After Multiplication):")
    for row in result:
        print(row)
print("="*50)
