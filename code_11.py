'''QUESTION - 11'''

'''Write a Python program that asks the user to enter: (1) number of developers initially working, (2) total days required to complete the project, (3) number of days already worked, and (4) number of additional developers joining later. Calculate and display the total number of days required to complete the project.'''


developers = int(input()) # 3
total_days = int(input()) #10
already_worked = int(input()) # 4
additional_developers = int(input()) #2

total_work = developers * total_days # 3*10=30

work_done = developers * already_worked # 3*4=12

remaining_work = total_work - work_done # 30-12=18

new_developers = developers + additional_developers # 3+2=5

days_needed_now = remaining_work / new_developers #18/5 = 3.6

total_project_days = already_worked + days_needed_now # 4+3.6=7.6

print( total_project_days)

