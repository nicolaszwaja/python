# Napisz funkcję:
# def fun(N), która dla podanej liczby naturalnej N (uwaga: liczby w systemie dziesiętnym) 
# zwraca długość jej najdłuższej 
# binarnej przerwy, albo 0, jeśli nie ma ani jednej przerwy. 

def fun(N):
    N = bin(N)[2:]
    max_gap = 0
    curr_gap = 0

    for digit in N:
        if digit == '0':
            curr_gap += 1
        elif digit == '1':
            max_gap = max(max_gap, curr_gap)
            curr_gap = 0
    return max_gap

print(fun(1041))
print(fun(529))