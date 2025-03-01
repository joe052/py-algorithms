def typing_time(digits, num):
    time = 0
    current_index = 0
    for digit in num:
        target_index = digits.index(digit)
        time += abs(target_index - current_index)
        current_index = target_index
    return time


