N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

from itertools import permutations

p_permutations = list(permutations(set(P), N))
q_permutations = list(permutations(set(Q), N))

print(abs(p_permutations.index(P) - q_permutations.index(Q)))
