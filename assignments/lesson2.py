import numpy as np

print("Question 1")

a = np.arange(25).reshape((5, 5))
print(a)

# sum of diag
sum_diag = np.diag(a).sum()
print("sum of diag: ", sum_diag)

# three functions applying to a
sum_a = np.sum(a)
mean_a = np.mean(a)
sqrt_a = np.sqrt(a)


print("sum: ", sum_a)
print("mean: ", mean_a)
print("sqrt:\n", sqrt_a)


print("\nQuestion 2")

x = np.random.randint(0, 1000, size=(10, 10))
even_x = x % 2 == 0
count_event = np.count_nonzero(even_x)

print("count of even number in x: ", count_event)

random_n = np.random.randn(100)

std_n = np.std(random_n)
mean_n = np.mean(random_n)
print("std: ", std_n)
print("mean: ", mean_n)

