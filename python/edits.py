# All the code below was taken from https://www.programiz.com/python-programming/examples

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
a += 3
b2 = 5
b2 *= 2
c = 4

c += 3

# calculate the discriminant
d = (b2 ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b2 - cmath.sqrt(d)) / (2 * a)
sol2 = (-b2 + cmath.sqrt(d)) / (2 * a)

print('The solution are {0} and {1}'.format(sol1, sol2))

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))

# Program to add two matrices using nested loop

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


def file_len(file_name, status):
    with open(file_name, status) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print(file_len("my_file.txt", "r"))

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
