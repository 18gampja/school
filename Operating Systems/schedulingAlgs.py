import time

# define process class
class Process:
    def __init__(self, process_id, burst_time, priority):
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority

# initialize ready queue with 3 processes
ready_queue = [Process(1, 10, 3), Process(2, 5, 1), Process(3, 8, 2)]
current_process = None

# print function to display ready queue
def display_ready_queue():
    print("\n")
    print("Ready Queue:")
    print("--------------")
    for p in ready_queue:
        print(f"Process {p.process_id} | Burst Time: {p.burst_time} | Priority: {p.priority}")
    print("\n")

# print function to display CPU status
def display_cpu():
    print("\n")
    print("CPU:")
    print("--------------")
    if current_process is not None:
        print(f"Currently executing Process {current_process.process_id} | Burst Time: {current_process.burst_time} | Priority: {current_process.priority}")
    else:
        print("CPU is idle.")
    print("\n")

# main program loop
while True:
    # display queue and cpu status
    display_ready_queue()
    display_cpu()

    # check for user input
    user_input = input("Press (E) to start executing processes, (A) to add a process to the ready queue, or (X) to exit: ").capitalize()
    
    # execute processes
    if user_input == "E":
        if current_process is not None:
            print("CPU is already executing a process.")
            continue
        if len(ready_queue) == 0:
            print("Ready queue is empty.")
            continue
        # get process with highest priority
        current_process = min(ready_queue, key=lambda p: p.priority)
        # remove process from ready queue
        ready_queue.remove(current_process)
        # execute process
        print(f"CPU executing Process {current_process.process_id}")
        time.sleep(current_process.burst_time)
        print(f"Process {current_process.process_id} finished execution.")
        current_process = None
    
    # add process to ready queue
    elif user_input == "A":
        process_id = len(ready_queue) + 1
        burst_time = int(input("Enter burst time for process: "))
        priority = int(input("Enter priority for process: "))
        new_process = Process(process_id, burst_time, priority)
        ready_queue.append(new_process)
        print(f"Process {new_process.process_id} added to ready queue.")
    
    # exit program
    elif user_input == "X":
        print("Exiting program.")
        break
    
    # invalid input
    else:
        print("Invalid input. Please try again.")
