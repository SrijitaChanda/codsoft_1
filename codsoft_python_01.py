#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


tasks=[]
def addTask():
    task=input("please enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list.")
def listTasks():
    if not tasks:
        print("There are no task currently")
    else:
        print("current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task{index}. {task}")
def deleteTask():
    listTasks()
    try:
        taskToDelete=int(input("Enter the number of task to delete: "))
        if taskToDelete>=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
        
    except:
        print("Invalid input!!")



if __name__=="__main__":
    print("welcome to your to-do list:")
    while True:
        print("\n")
        print("please select your choise:")
        print("----------------------------------")
        print("1. Add a new task:")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        choice=input("Enter your choice of number:")
        
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):  
            break
        else:
            print("invalid choice!!...try again")
    print("Goodbye")     


# In[ ]:




