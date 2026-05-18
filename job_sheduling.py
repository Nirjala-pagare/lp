def job_scheduling(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = 0

    for job in jobs:
        if job[1] > max_deadline:
            max_deadline = job[1]

    slots = [False] * max_deadline
    result = [""] * max_deadline

    total_profit = 0

    for job in jobs:

        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        for j in range(deadline - 1, -1, -1):

            if slots[j] == False:

                slots[j] = True
                result[j] = job_id
                total_profit = total_profit + profit

                break

    print("\nSelected Jobs:", result)
    print("Maximum Profit:", total_profit)


n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):

    print("\nEnter Job", i + 1)

    job_id = input("Enter Job ID: ")

    deadline = int(input("Enter Deadline: "))

    profit = int(input("Enter Profit: "))

    jobs.append((job_id, deadline, profit))


job_scheduling(jobs)