def karatsuba(num1, num2):
    if num1 < 100 or num2 < 100:
        return num1 * num2

    m = max(len(str(num1)), len(str(num2))) # to handle if two number not same digit
    half = m // 2
    # print(half)
    # 54 32 
    a = str(num1)[:half] # 4
    b = str(num1)[half:] # 50
    c = str(num2)[:half] # 2
    d = str(num2)[half:] # 0

    print(a, b, c, d)
    ac = karatsuba(int(a), int(c)) # c0
    bd = karatsuba(int(b), int(d)) # c2
    ad_bc = karatsuba(int(a)+int(b), int(c)+int(d)) - ac - bd # c1
    # print(ac, bd, ad_bc)
    return (ac * (10 ** (half * 2))) + (ad_bc * (10 ** half)) + bd

if __name__ == "__main__":
    num1 = 5432
    num2 = 1678
    print(karatsuba(num1, num2))

