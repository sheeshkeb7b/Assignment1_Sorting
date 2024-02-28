class Chocolate:
    "A class that represents a chocolate"
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

    def ChocolateDistribution_Recursive(self, chocolates, students, index=0, overallDistribution={}):
        if index < len(students):
            overallDistribution[students[index]] = chocolates[index]
            self.ChocolateDistribution_Recursive(chocolates, students, index + 1, overallDistribution)

        return overallDistribution

    def ChocolateSort(self, chocolates, key):
        """
        This function, when called, will use quicksort to sort the chocolates depending on the specified key (weight,
        price, ID).
        """
        if len(chocolates) <= 1: #Checks if the list of chocolates has 0 or 1 elements, if true then it is already sorted.
            return chocolates

        #Assigning the pivot as the middle element, which is ID 1 Milk Chocolate
        pivot = chocolates[len(chocolates) // 2] #


        # Divide the list of chocolates into three different groups, left is < pivot, middle is = pivot, right is > pivot
        left = [choco for choco in chocolates if getattr(choco, key) < getattr(pivot, key)]
        middle = [choco for choco in chocolates if getattr(choco, key) == getattr(pivot, key)]
        right = [choco for choco in chocolates if getattr(choco, key) > getattr(pivot, key)]

        #Recursively applies quicksort to left and right groups, the results will be merged into one sorted list and returned.
        return self.ChocolateSort(left, key) + middle + self.ChocolateSort(right, key)


# Creating the two lists, chocolates and students. Each student will receive a unique chocolate.
chocolates = [Chocolate(4, 3, "Milk", 1),
              Chocolate(5, 2, "Almond", 2),
              Chocolate(3, 6, "Dark", 3),
              Chocolate(4, 2, "White", 4),
              Chocolate(7, 4, "Peanut Butter", 5)]

students = ["Rashed", "Khalifa", "Tom", "Jerry", "Matthew"]

# Creating two lists of chocolate, one that is sorted by their weight and the other is sorted by their price.
sorted_chocolates_by_weight = Chocolate().ChocolateSort(chocolates, 'weight')
sorted_chocolates_by_price = Chocolate().ChocolateSort(chocolates, 'price')

# Displaying the results of ChocolateSort, stating the ID, Type, Weight, and price of each chocolate in the sorted list.
print("\nSorted Chocolates by Weight:")
for chocolate in sorted_chocolates_by_weight:
    print(f"ID {chocolate.ID}: {chocolate.chocoType} chocolate, Weight: {chocolate.weight} grams, Price: {chocolate.price} AED")

print("\nSorted Chocolates by Price:")
for chocolate in sorted_chocolates_by_price:
    print(f"ID {chocolate.ID}: {chocolate.chocoType} chocolate, Weight: {chocolate.weight} grams, Price: {chocolate.price} AED")
