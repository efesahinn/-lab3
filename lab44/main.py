n=int(input("enter task number"))
tasks = {}
initial_task=[]
inital_task_number=0

for i in range (n):
    dependcy=[]
    task_name=(input("enter task name"))
    depend=int(input("enter dependncy"))

    if depend==0:
        initial_task.append(task_name)
        inital_task_number+=1

    for i in range(depend):
     dep_name=(input("dependency names"))
     dependcy.append(dep_name)

    tasks[task_name] =dependcy

print("TASK STRUCTURE")
print(tasks)

print("initial tasks")
print(initial_task)

print("exe order")

execution_order = []
completed = set()

while len(execution_order) < n:

    count = len(execution_order)

    for key in tasks:
        if key not in completed:

            ok = 1   # 1 = yapılabilir, 0 = yapılamaz

            for dep in tasks[key]:
                if dep not in completed:
                    ok = 0

            if ok == 1:
                execution_order.append(key)
                completed.add(key)

    if len(execution_order) == count:
        print("Error: Circular dependency detected!")
        break

if len(execution_order) == n:
    print("Execution order:", execution_order)












