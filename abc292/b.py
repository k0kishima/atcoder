import sys
from enum import IntEnum


class EventType(IntEnum):
    GIVE_A_YELLOW_CARD = 1
    GIVE_A_RED_CARD = 2
    ASK_TO_BE_DISQUALIFIED = 3


if __name__ == "__main__":
    args = []

    for l in sys.stdin:
        if value := l.strip():
            a, b = map(int, value.split())
            args.append((a, b))
        else:
            break

    player_count, event_count = args[0]
    events = args[1:]
    disqualification_points_indexed_by_player_number = [0] * (player_count + 1)
    for event in events:
        event_type, player_number = event
        if event_type == EventType.GIVE_A_YELLOW_CARD:
            disqualification_points_indexed_by_player_number[player_number] += 1
        elif event_type == EventType.GIVE_A_RED_CARD:
            disqualification_points_indexed_by_player_number[player_number] += 2
        elif event_type == EventType.ASK_TO_BE_DISQUALIFIED:
            print("No") if disqualification_points_indexed_by_player_number[
                player_number
            ] < 2 else print("Yes")
