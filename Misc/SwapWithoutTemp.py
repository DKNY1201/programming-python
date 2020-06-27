def swap_without_temp(a, b):
    print("Before swap: a = ", a, ". b = ", b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swap: a = ", a, ". b = ", b)
    print("=====================")

swap_without_temp(1, 2)
swap_without_temp(11, 22)
swap_without_temp(111, 222)
