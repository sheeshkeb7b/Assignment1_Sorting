from matplotlib import pyplot as plt
import timeit

class Chocolate:
    def __init__(self, weight=0, price=0, chocoType="", ID=0):
        self.weight = weight
        self.price = price
        self.chocoType = chocoType
        self.ID = ID

    def ChocolateDistribution_Iterative(self, chocolates, students):
        overallDistribution = {}
        for i in range(len(students)):
            overallDistribution[students[i]] = chocolates[i]

        return overallDistribution

    def ChocolateSort(self, chocolates, key):
        if len(chocolates) <= 1:
            return chocolates

        pivot = chocolates[len(chocolates) // 2]

        left = [choco for choco in chocolates if getattr(choco, key) < getattr(pivot, key)]
        middle = [choco for choco in chocolates if getattr(choco, key) == getattr(pivot, key)]
        right = [choco for choco in chocolates if getattr(choco, key) > getattr(pivot, key)]

        return self.ChocolateSort(left, key) + middle + self.ChocolateSort(right, key)

    def StudentSearchPrice(self, chocolates, students, attributeValue, attributeKey="price"):
        sorted_chocolates_price = Chocolate().ChocolateSort(chocolates, attributeKey)
        iterative_results = Chocolate().ChocolateDistribution_Iterative(chocolates, students)

        for student, chocolate in iterative_results.items():
            current_choco_value = getattr(chocolate, attributeKey)

            if current_choco_value == attributeValue:
                return chocolate, student

        return None

def measure_time_complexity_search_price(n):
    chocolates = [Chocolate(price=i) for i in range(n)]  # Creating chocolates with different prices
    students = list(range(n))  # Assigning students IDs

    # Measure execution time
    start_time = timeit.default_timer()
    Chocolate().StudentSearchPrice(chocolates, students, 0)  # Searching for chocolate with price 0
    end_time = timeit.default_timer()

    return end_time - start_time

# Varying the number of chocolates (n) and measuring time complexity
n_values = list(range(1, 1001, 50))
time_complexity_values_search_price = [measure_time_complexity_search_price(n) for n in n_values]

# Plotting the graph
plt.plot(n_values, time_complexity_values_search_price, marker='o')
plt.title('T(n) of StudentSearchPrice at n = 1000')
plt.xlabel('Number of Students')
plt.ylabel('T(n) (seconds)')
plt.grid(True)
plt.show()