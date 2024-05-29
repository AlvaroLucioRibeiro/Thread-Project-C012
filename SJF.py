from car import Car

def SJF(cars: list[Car]) -> list[Car]:
    """
    This function implements the Shortest Job First (SJF) scheduling algorithm.

    Parameters:
    tasks (list): A list of Task objects.

    Returns:
    schedule (list): A list of tasks in the order they will be scheduled.
    """

    # Initialize an empty list to store the scheduling order
    schedule = []

    # Sort tasks by speed (Speed represents the size of proccess)
    cars.sort(key=lambda car: car.speed)

    # Initialize total waiting time
    cumulative_time = 0

    for car in cars:
        # Calculates burst time based on speed and total running distancea
        burst_time = 100 / car.speed

        # Calculates waiting time based on accumulated displacement
        #car.waiting_time = cumulative_time
        cumulative_time += burst_time

        schedule.append(car)

    print(f"Average Waiting Time: {format(cumulative_time / len(schedule), ".2f")} Units of Time")
    print(f"Total Waiting Time: {format(cumulative_time, ".2f")} Units of Time\n\n")

    return schedule