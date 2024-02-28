from matplotlib import pyplot as plt
import timeit

class Chocolate:
    def __init__(self, weight=0, price=0, chocoType="", ID=0):
        self.weight = weight
        self.price = price
        self.chocoType = chocoType
        self.ID = ID

    def ChocolateSort(self, chocolates, key):
        if len(chocolates) <= 1:
            return chocolates

        pivot = chocolates[len(chocolates) // 2]

        left = [choco for choco in chocolates if getattr(choco, key) < getattr(pivot, key)]
        middle = [choco for choco in chocolates if getattr(choco, key) == getattr(pivot, key)]
        right = [choco for choco in chocolates if getattr(choco, key) > getattr(pivot, key)]

        return self.ChocolateSort(left, key) + middle + self.ChocolateSort(right, key)

def measure_time_complexity_chocolate_sort(n, key):
    chocolates = [Chocolate(weight=i, price=i, chocoType=f"Type{i}", ID=i) for i in range(n)]

    start_time = timeit.default_timer()
    chocolates[0].ChocolateSort(chocolates, key)
    end_time = timeit.default_timer()

    return end_time - start_time

# Varying the number of chocolates (n) and measuring time complexity for sorting by weight
n_values = list(range(1, 100, 1))
time_complexity_values_weight = [measure_time_complexity_chocolate_sort(n, 'weight') for n in n_values]

# Varying the number of chocolates (n) and measuring time complexity for sorting by price
time_complexity_values_price = [measure_time_complexity_chocolate_sort(n, 'price') for n in n_values]

# Varying the number of chocolates (n) and measuring time complexity for sorting by ID
# Plotting the graphs
plt.plot(n_values, time_complexity_values_weight, label='Weight', marker='o')
plt.plot(n_values, time_complexity_values_price, label='Price', marker='o')

plt.title('T(n) of ChocolateSort at n = 1000')
plt.xlabel('Number of Chocolates')
plt.ylabel('T(n) (seconds)')
plt.legend()
plt.grid(True)
plt.show()
