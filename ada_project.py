#Pandas for reading the data and matplotlib for plotting
import pandas as pd
import matplotlib.pyplot as plt
import random

#Read data using pandas
iris_data = pd.read_csv("Datasets/Datasets/iris_data.csv")

print("The dataset being used is : ")
print(iris_data)

print("The column(x values) being used !")
print(iris_data.SepalWidth)

#Plot the graph
plt.plot(iris_data.SepalWidth)
plt.title("The graph being used for the algorithm.")
plt.show()

#Create skewed data dict for new data
skewed_data_dict = {}

for i in range(1,11):
    skewed_data_dict[i] = []

print("Initialised dict for skewed data.")
print(skewed_data_dict)    

def random_addition():
    return 0.1 * random.randint(0,4)

def generate_random_graphs():
    for j in range(0,10):
        for i in range(len(iris_data)):
            skewed_data_dict[j+1].append(iris_data.SepalWidth[i] + random_addition())

generate_random_graphs()

#All the graphs 
fig, ax = plt.subplots(nrows=5, ncols=2)

count = 1
for row in ax:
    for col in row:
        col.plot(skewed_data_dict[count])
        count+=1
plt.title("All the graphs used for testing!")
plt.show()

#dictionary to keep track of all the errors
number_of_errors_dict ={}
for i in range(1,11):
    number_of_errors_dict[i] = 0
print(number_of_errors_dict)

#Function to check which are low errors
def check_which_are_low_error():
    for i in range(1,11):
        for j in range(len(iris_data.SepalWidth)):
            if abs(iris_data.SepalWidth[j] - skewed_data_dict[i][j]) >= 0.3:
                number_of_errors_dict[i] += 1

print("The number of errors in dict")
print(number_of_errors_dict)

accepted = []

print()
def which_cases_are_correct_and_which_arent():
    for i in range(1,11):
        if number_of_errors_dict[i] <40:
            accepted.append(i)
            print(f"Case {i} is has less than 40 errors. So this graph is acceptable.")
        else:
            print(f"Case {i} is has more than 40 errors. So this graph is not acceptable.")

which_cases_are_correct_and_which_arent()


fig, (ax1,ax2) = plt.subplots(2,1,figsize=(8,6))
ax1.plot(skewed_data_dict[accepted[0]])
ax2.plot(skewed_data_dict[accepted[1]])
plt.title("The accepted graphs...")
plt.show()
