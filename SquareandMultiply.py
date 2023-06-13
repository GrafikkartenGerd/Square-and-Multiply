def square_and_multiply(base, exponent, modulus):
    res = 1
    binary_exponent = bin(exponent)[2:]

    for bit in binary_exponent:
        res = (res ** 2) % modulus
        if bit == '1':
            res = (res * base) % modulus

    return res

result = square_and_multiply(base, exponent, modulus)
print(result)
