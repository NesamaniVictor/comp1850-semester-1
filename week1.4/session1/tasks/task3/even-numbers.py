# Find the even numbers up to some limit

# def even_numbers(limit):
#     evens = []
#     for n in range(limit + 1):
#         if n % 2 == 0:
#             evens.append(n)
#     return evens

# print(even_numbers(20))

def even_numbers(limit):
    return [n for n in range(limit+1) if n % 2 == 0]

print(even_numbers(20))