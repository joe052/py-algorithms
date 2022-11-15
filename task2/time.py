# test case variable
time = "10:30:00"
# time = "13:34:59"
# time = "00:00:00"

# function to calculate time remaining to midnight
def time2Midnight(time):
    midnight = 86400
    timeArr = time.split(":")
    # convert into seconds
    hSecs = int(timeArr[0]) * 60 * 60
    mSecs = int(timeArr[1]) * 60
    secs = int(timeArr[2])
    totalSecs = hSecs + mSecs + secs
    # check time remaining
    timeRemaining = midnight - totalSecs
    # make midnight exceptional
    if (timeRemaining == 86400):
        timeRemaining = 0

    # convert to desired output
    m, s = divmod(timeRemaining, 60)
    h, m = divmod(m, 60)
    result = '{:d}:{:02d}:{:02d}'.format(h, m, s)
    return result

# run code
print(time2Midnight(time))
