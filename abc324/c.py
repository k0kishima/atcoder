N, origin_text = input().split()
len_origin_text = len(origin_text)

changed_texts = []
for _ in range(int(N)):
    changed_texts.append(input())


def is_shorter_text_of(origin: str, short: str) -> bool:
    for i in range(len(short) + 1):
        if short[:i] + origin[i] + short[i:] == origin:
            return True
    return False


def is_longer_text_of(origin: str, long: str) -> bool:
    for i in range(len(origin) + 1):
        if long[:i] + long[i + 1 :] == origin:
            return True
    return False


def is_one_letter_different_of(origin: str, changed: str) -> bool:
    diff_count = 0
    for o, c in zip(origin, changed):
        if o != c:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1


may_be_same = []
for i, t in enumerate(changed_texts, 1):
    if t == origin_text:
        may_be_same.append(i)
        continue

    if (len(t) + 1) == len_origin_text:
        if is_shorter_text_of(origin_text, t):
            may_be_same.append(i)
            continue

    if (len(t) - 1) == len_origin_text:
        if is_longer_text_of(origin_text, t):
            may_be_same.append(i)
            continue

    if len(t) == len_origin_text:
        if is_one_letter_different_of(origin_text, t):
            may_be_same.append(i)
            continue

if len(may_be_same) > 0:
    print(len(may_be_same))
    print(*may_be_same)
else:
    print(0)
    print()
