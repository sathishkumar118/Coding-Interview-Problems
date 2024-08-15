def bestSeat(seats):
    streak = 0
    idx = -1
    print(seats)
    for i in range(len(seats)):
        currStreak = int(seats[i] == 0)
        currIdx = i
        while i < len(seats) and sum(seats[i : i+2]) == 0:
            currStreak += 1
            i += 1
        if streak < currStreak:
            streak = currStreak
            idx = currIdx + (currStreak + 1)//2 - 1
    return idx