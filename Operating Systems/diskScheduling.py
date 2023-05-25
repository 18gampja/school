import sys
import random

# Constants
CYLINDERS = 5000
REQUESTS = 1000

# Functions
def fcfs(initial, requests):
    head = initial
    total_movement = 0
    for request in requests:
        distance = abs(head - request)
        head = request
        total_movement += distance
    return total_movement

def scan(initial, requests):
    head = initial
    total_movement = 0
    sorted_requests = sorted(requests)
    lower_requests = [r for r in sorted_requests if r < head]
    higher_requests = [r for r in sorted_requests if r >= head]
    for direction in [higher_requests, reversed(lower_requests)]:
        for request in direction:
            distance = abs(head - request)
            head = request
            total_movement += distance
    return total_movement

def cscan(initial, requests):
    head = initial
    total_movement = 0
    sorted_requests = sorted(requests)
    lower_requests = [r for r in sorted_requests if r < head]
    higher_requests = [r for r in sorted_requests if r >= head]
    for direction in [higher_requests, [CYLINDERS - 1] + lower_requests]:
        for request in direction:
            distance = abs(head - request)
            head = request
            total_movement += distance
    return total_movement

# Main program
if __name__ == '__main__':

    initial = 1000

    # Generate random requests
    requests = [random.randint(0, CYLINDERS - 1) for _ in range(REQUESTS)]

    # Define a dictionary mapping algorithm names to functions
    algorithms = {
        'FCFS': fcfs,
        'SCAN': scan,
        'C-SCAN': cscan
    }

    # Calculate head movement for each algorithm
    for name, function in algorithms.items():
        movement = function(initial, requests)
        print(f"{name}: {movement}")
