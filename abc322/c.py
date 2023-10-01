N, M = map(int, input().split(" "))
event_days = list(map(int, input().split(" ")))

i = 1
while len(event_days) > 0:
    next_event_day = event_days.pop(0)
    for day in range(i, next_event_day + 1):
        print(next_event_day - day)

    i = next_event_day + 1
