# import math
# num=[3,5,7]
# for i in num:
#     print(f"factorial of {i} is: {math.factorial(i)}")

# lst=[1,2,2,3,4,4,5,]
# new_list=[]
# for x in lst:
#     if x  not in new_list:
#         new_list.append(x)
# print(new_list)

# def second_largest(list):
#     if len(list)<2:
#         return None
#     first = second = float('_inf')
#     for x in list:
#         if x > first:
#             second = first
#             first = x
#         elif x > second and x != first:
#             second = x
#     return None if second == float('-inf')else second
# print(second_largest([5, 2, 9, 7, 9]))

# lst= [10,5,20,8,15]
# largest = second= float('-inf')
# for n in lst:
#     if n > largest:
#         second = largest
#         largest= n
#     elif n > second and n != largest:
#         second= n
# print(second)

# lst = [1,2,2,3,3,3]
# freq = {}

# for x in lst:
#     if x in freq:
#         freq[x] += 1
#     else:
#         freq[x] = 1

# print(freq)


# A = [1,3,5]
# B = [2,4,6,8]

# result = []
# i = 0

# while i < len(A) or i < len(B):
#     if i < len(A):
#         result.append(A[i])
#     if i < len(B):
#         result.append(B[i])
#     i += 1

# print(result)

# A = [1,2,2,3,4]
# B = [2,3,5]
# common = []
# for x in A:
#     if x in B and x not in common:
#         common.append(x)
# print(common)

# lst = [1,2,3,4]
# squared = [x*x for x in lst]
# print(squared)


# lst = [1,2,3,4,5,6]
# even = []
# odd = []
# for x in lst:
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
# print("Even:", even)
# print("Odd:", odd)

# lst = [1,2,3,4,5]
# N = 2
# N = N % len(lst)
# rotated = lst[-N:] + lst[:-N]
# print(rotated)
