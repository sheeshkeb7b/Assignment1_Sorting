from matplotlib import pyplot as plt
import timeit


def ChocolateDistribution_Iterative(chocolates, students):
    overallDistribution = {}
    for i in range(len(students)):
        overallDistribution[students[i]] = chocolates[i]
    return overallDistribution

def measure_time_complexity(n):
    chocolates = [1] * n  # Assuming each student has 1 chocolate
    students = list(range(n))

    # Measure execution time
    start_time = timeit.default_timer()
    ChocolateDistribution_Iterative(chocolates, students)
    end_time = timeit.default_timer()

    return end_time - start_time


# Varying the number of students (n) and measuring time complexity
n_values = list(range(1, 1001, 50))
time_complexity_values = [measure_time_complexity(n) for n in n_values]

# Plotting the graph
plt.plot(n_values, time_complexity_values, marker='o')
plt.title('T(n) of ChocolateDistribution_Iterative at n = 1000')
plt.xlabel('Number of Students')
plt.ylabel('T(n) (seconds)')
plt.grid(True)
plt.show()