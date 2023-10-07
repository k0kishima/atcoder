from pprint import pprint

N, M = map(int, input().split(" "))

SCORING = list(map(int, input().split(" ")))
scores = {}
not_solved = {}

for i in range(N):
    result = input()
    solved_idxs = [i for i, mark in enumerate(result) if mark == "o"]
    player_num = i + 1
    scores[player_num] = sum([SCORING[idx] for idx in solved_idxs]) + player_num
    not_solved[player_num] = [i for i, mark in enumerate(result) if mark == "x"]

high_score = max(scores.values())

scoring_tuple_sorted_by_desc = sorted(
    list(enumerate(SCORING)), key=lambda x: x[1], reverse=True
)
score_with_index = [(score, index) for index, score in scoring_tuple_sorted_by_desc]

for player_num, current_score in scores.items():
    if current_score == high_score:
        print(0)
    else:
        need_count = 0
        virtual_score = current_score
        for score, idx in score_with_index:
            if idx in not_solved[player_num]:
                virtual_score += score
                need_count += 1
                if virtual_score > high_score:
                    break
        print(need_count)
