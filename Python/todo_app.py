"""
name = "I want to learn python by doing Todo APP!"
print(name)

task = input(" Enter the name of the task that you want to do today")
print ("you task will be saved in", task)
"""
# the above are very basic here the next version of the task using while loop concept until we type exit it will keep on add the task.


print("Welcome to TODO app next version")
print( "Type 'exit' to add stop to adding tasks. \n ")
tasks = []

while True:
    task = input(" Enter the task ")
    if task.lower() == "exit":
        break
    tasks.append(task)
    print(" \n  your taks of the day or today ")
    for t in tasks:
        print ("-", t)

# practise for the day.


