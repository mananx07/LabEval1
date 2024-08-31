task = {1: ["task1","false"],
        2: ["task2","false"],
        3: ["task5","false"],
        4: ["task6","true"],
        5: ["module6","false"],
        6: ["assigment5","true"],
        7: ["group6","false"],
        8: ["finishes6","true"] 
    }

def addtask(name,id,done):
    task[id] = [name,done]


def modify(id,newname, newdone):
    task[id] = [newname,newdone]

def deletetask(name):
    k = list(task.keys())
    for i in range(len(k)):
        arr = task[k[i]]
        if arr[0] == name:
            task.pop(k[i])
            return

    print("no such task exists")

def findtask(n):
    if type(n) == int:
        print("task found based on id: ")
        k = list(task.keys())
        if n in k:
             print(f"{n}: {task[n]}")
        else:
            print("Id not found")
    else:
        k = list(task.keys())
        for i in range(len(k)):
            arr = task[k[i]]
            if arr[0] == n:
                print("task found based on name: ")
                print(f"{k[i]}: [{n},{arr[1]}]")
                return 
        print("taskname not found")   

def findAllTasksEndsWith(c):
    k = list(task.keys())
    ans = {}
    for i in range(len(k)):
        arr = task[k[i]]
        st = arr[0]
        if (st[len(st)-1] == c):
            ans[k[i]] = task[k[i]] 
        
        
    print(f"Tasks whose name end with {c} are: ")
    print(ans)
    

#print(task)
addtask("task9", 9, "false") #adding tasks 
#print(task)
modify(3,"newtask","false")
print(task)
deletetask("newtask")
#print(task)
findtask("task6")
findtask(7)
findAllTasksEndsWith("6")
findAllTasksEndsWith("7")

