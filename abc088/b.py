card_count = int(input())
cards = map(int, input().split())

sorted_cards = sorted(cards, reverse=True)

score_of_alice = sum(sorted_cards[::2])
score_of_bob = sum(sorted_cards[1::2])

print(score_of_alice - score_of_bob)
