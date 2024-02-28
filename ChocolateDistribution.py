class Chocolate:
   """ A class that represents a chocolate


     Attributes:
     weight - The weight of the chocolate measured in grams
     price - The price of the chocolate measured in AED
     chocoType - The type of chocolate
     ID - The number given to a chocolate in the bag.


   """
   def __init__(self, weight = 0, price = 0, chocoType = "", ID = 0):
       self.weight = weight
       self.price = price
       self.chocoType = chocoType
       self.ID = ID


   def ChocolateDistribution_Iterative(chocolates, students):
       """
          When called, this function distributes chocolates to students through a loop that iterates depending on
          the number of students. When the for loop starts, it assigns a chocolate from the list
          to a student and puts them in overallDistribution dictionary. After all students have been assigned a
          chocolate, the loop ends and returns the dictionary.
       """
       overallDistribution = {}
       for i in range(len(students)):
           overallDistribution[students[i]] = chocolates[i]


       return overallDistribution


   def ChocolateDistribution_Recursive(chocolates, students, index=0, overallDistribution={}):
       """
           This method, when called, distributes a list of chocolates by their weight to students by
           calling itself recursively until the index becomes greater than or equal to the number of students.
           Each recursive call increases the index by +1, allowing each student to get a chocolate.
       """
       if index < len(students):
           overallDistribution[students[index]] = chocolates[index]
           Chocolate.ChocolateDistribution_Recursive(chocolates, students, index + 1, overallDistribution)

       return overallDistribution




#Creating the two lists, chocolates and students. Each student will receive a unique chocolate.
chocolates = [Chocolate(4, 3, "Milk", 1),
             Chocolate(5, 2, "Almond", 2),
             Chocolate(3, 6, "Dark", 3),
             Chocolate(4, 2, "White", 4),
             Chocolate(7, 4, "Peanut Butter", 5)]


students = ["Rashed", "Khalifa", "Tom", "Jerry", "Matthew"]


#Calling both methods and assigning the results to a new variable.
iterativeResults = Chocolate.ChocolateDistribution_Iterative(chocolates, students)
recursiveResults = Chocolate.ChocolateDistribution_Recursive(chocolates, students)


#Displaying the results of the distribution, stating the type, price, weight, and unique ID of a chocolate that a student received.
print("Iterative Result:")
for student, chocolate in iterativeResults.items():
   print(f"{student} got number {chocolate.ID}, which is {chocolate.chocoType} chocolate. It weighs {chocolate.weight} grams and is valued at {chocolate.price} AED.")


print("\nRecursive Result:")
for student, chocolate in recursiveResults.items():
   print(f"{student} got number {chocolate.ID}, which is {chocolate.chocoType} chocolate. It weighs {chocolate.weight} grams and is valued at {chocolate.price} AED.")


