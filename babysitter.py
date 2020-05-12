def hours_worked(start_time,end_time):
    if start_time < 17:
        start_time = 17
    if end_time not in range(12, 24 + 1):
        end_time += 24

    return end_time - start_time
    