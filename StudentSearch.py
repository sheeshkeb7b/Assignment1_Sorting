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

    def ChocolateSort(self, chocolates, key):
        if len(chocolates) <= 1:
            return chocolates


        pivot = chocolates[len(chocolates) // 2]

        left = [choco for choco in chocolates if getattr(choco, key) < getattr(pivot, key)]
        middle = [choco for choco in chocolates if getattr(choco, key) == getattr(pivot, key)]
        right = [choco for choco in chocolates if getattr(choco, key) > getattr(pivot, key)]

        return self.ChocolateSort(left, key) + middle + self.ChocolateSort(right, key)

    def StudentSearchPrice(self, chocolates, students, attributeValue, attributeKey = "price"):
        """
        This function, when called, will first distribute all the students a distinct chocolate, then uses a for loop to
        linearly search each student's weight with the specified price. If found, the chocolate and student is returned.
        Otherwise, it will return nothing.
        """
        sorted_chocolates_price = Chocolate().ChocolateSort(chocolates, attributeKey)
        iterative_results = Chocolate().ChocolateDistribution_Iterative(chocolates, students)

        for student, chocolate in iterative_results.items():
            current_choco_value = getattr(chocolate, attributeKey)

            if current_choco_value == attributeValue:
                #If Chocolate with the specified price was not found
                return chocolate, student

        #If Chocolate with the specified price was not found
        return None

    def StudentSearchWeight(self, chocolates, students, attributeValue=0, attributeKey="weight"):
        """
        This function, when called, will first distribute all the students a distinct chocolate, then uses a for loop to
        linearly search each student's weight with the specified weight. If found, the chocolate and student is returned.
        Otherwise, it will return nothing.
        """
        sorted_chocolates_weight = Chocolate().ChocolateSort(chocolates, attributeKey)
        iterative_results = Chocolate().ChocolateDistribution_Iterative(chocolates, students)

        for student, chocolate in iterative_results.items():
            current_choco_value = getattr(chocolate, attributeKey)

            if current_choco_value == attributeValue:
                #If Chocolate with the specified weight was Found
                return chocolate, student

        #If Chocolate with the specified weight was not found
        return None

# Creating the two lists, chocolates and students. Each student will receive a unique chocolate.
chocolates = [Chocolate(4, 3, "Milk", 1),
                  Chocolate(5, 2, "Almond", 2),
                  Chocolate(3, 6, "Dark", 3),
                  Chocolate(4, 2, "White", 4),
                  Chocolate(7, 4, "Peanut Butter", 5)]

students = ["Rashed", "Khalifa", "Tom", "Jerry", "Matthew"]


#Searching for the student with the candy's price or weight
chocolate_price_result = Chocolate().StudentSearchPrice(chocolates, students, 6, "price")
chocolate_weight_result = Chocolate().StudentSearchWeight(chocolates, students, 4, "weight")
chocolate_weight_result2 = Chocolate().StudentSearchWeight(chocolates, students, 10, "weight")

if chocolate_price_result:
    print(f"The student with a chocolate that costs {chocolate_price_result[0].price} AED is {chocolate_price_result[1]} with {chocolate_price_result[0].chocoType} chocolate")
else:
    print("No student found with the specified chocolate price")

if chocolate_weight_result:
    print(f"The student with a chocolate that weighs {chocolate_weight_result[0].weight} grams is {chocolate_weight_result[1]} with {chocolate_weight_result[0].chocoType} chocolate")
else:
    print("No student found with the specified chocolate weight")

if chocolate_weight_result2:
    print(f"The student with a chocolate that weighs {chocolate_weight_result[0].weight} grams is {chocolate_weight_result[1]} with {chocolate_weight_result[0].chocoType} chocolate")
else:
    print("No student found with the specified chocolate weight")

