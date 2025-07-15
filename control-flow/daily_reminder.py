# This script prompts the user to input a task, its priority, and whether it is time-bound and then generates a reminder message based on the inputs.

task = (input("Enter your task: ")) # Input for the task
priority = (input("Priority (high/medium/low): ")) # Input for the priority of the task
time_bound = (input("Is it time-bound? (yes/no): ")) # Input for whether the task is time-bound

# Determine the reminder message based on the priority
match priority:
    case "high":
        print(f"Reminder: '{task} is a high priority task", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.", end="")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.", end="")
    case _:
        print("Reminder: '{task}' is a task with an unspecified priority.", end="")

# Append whether the task is time-bound or not
if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")
        