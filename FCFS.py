from car import Car

def FCFS(tasks: list[Car]) -> list[Car]:
  """
  This function implements the First-Come, First-Served (FCFS) scheduling algorithm.

  Parameters:
  tasks (list): A list of tasks where each task is represented as a dictionary with two keys: 'arrival_time' and 'burst_time'.

  Returns:
  schedule (list): A list of tasks in the order they will be scheduled, with an additional 'waiting_time' key for each task.
  """

  # Sort tasks by arrival time (`arrival_time` can be the ID of each object in a array)
  tasks.sort(key=lambda task: task.id)

  # Initialize an empty list to store the scheduling order
  schedules = []

  # Initialize total waiting time
  cumulative_time = 0

  # For each task in the sorted list, calculate its waiting time, append it to the schedule, and update current time
  for task in tasks:
    burst_time = 100 / task.speed

    #waiting_time = cumulative_time
    cumulative_time += burst_time

    schedules.append(task)

  print(f"Average Waiting Time: {format(cumulative_time / len(schedules), ".2f")} Units of Time")
  print(f"Total Waiting Time: {format(cumulative_time, ".2f")} Units of Time\n\n")

  return schedules