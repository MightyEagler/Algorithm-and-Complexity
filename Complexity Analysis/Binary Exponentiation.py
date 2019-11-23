"""
    Binary Exponenation by two method:
    from left to right and from right to left
"""

def expo_to_list(expo):
    binary = bin(expo)[2:]
    return list(map(int, binary))
def left_right_bin_expo(a, Bin):
    product = a
    for i in range(1, len(Bin)):
        product = product * product
        if Bin[i] == 1:
            product = product * a
    return product
def right_left_bin_expo(a, Bin):
    term = a
    if Bin[-1] == 1:
        product = a
    else:
        product = 1
    for i in range(len(Bin)-2, -1, -1):
        term = term * term
        if Bin[i] == 1:
            product = product * term
    return product
base = 2
expo = 13
Bin = expo_to_list(expo)
print("Compute binary exponentiation from Left to right: ")
print("2 to the power of 13 is: %d" % left_right_bin_expo(base, Bin))
print("Compute binary exponentiation from Right to left: ")
print("2 to the power of 13 is: %d" % right_left_bin_expo(base, Bin))
