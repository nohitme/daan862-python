print("=== Question 1 ===")

L1 = [1, 4, 1, 5, 1, 3, 3, 1, 5, 1, 1, 1, 2, 4, 3, 3, 4, 2, 3, 2]

# use set() to get unique values
set1 = set(L1)
print("unique values: ", set1)

# number of unique values
print("number of unique values: ", len(set1))

# create a dictionary with counts
dict1 = {}
for val in set1:
    dict1[val] = L1.count(val)

print("result dict: ", dict1)

# find the most frequent number
freq = 0
num = -1
for key, value in dict1.items():
    if value > freq:
        freq = value
        num = key

print("the number with most frequency: ", num)

print("=== Question 2 ===")

L2 = [879, 394, 235, 580, 628, 81, 206, 238, 927, 853, 622,
      603, 110, 143, 824, 324, 343, 506, 634, 325, 258, 900,
      960, 286, 449, 890, 921, 170, 888, 851]

# get sum of L2
sum2 = 0
for val in L2:
    sum2 += val

print("sum of L2: ", sum2)


def my_mean(input_list):
    _sum = 0
    for _val in input_list:
        _sum += _val
    return _sum / len(input_list)


# print mean of L2
print("mean of L2: ", my_mean(L2))

# sum of elements > 500
sum3 = 0
for val in L2:
    if val > 500:
        sum3 += val

print("sum of elements that > 500 in L2: ", sum3)
