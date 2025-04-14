from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple


#ok im just putting this up here so i dont forget what im supposed to add:
#  This code file is made to implement the Knapsack in a bottom up way because when i tried top down I got really stuck,we can change it if you want tho
# It has dataclass KnapsackResult and a clean wrapper.
# It has a O( n W) DP table and the back‑trace to recover the chosen items.


@dataclass
class KnapsackResult:
    max_value: int
    total_weight: int
    chosen_items: List[int]
def knapsack(values: List[int], weights: List[int], capacity: int) -> KnapsackResult:
    """Bottom‑up 0/1 knap"""
    if len(values) != len(weights):
        raise ValueError("values and weights must be the same length")
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        v, w = values[i - 1], weights[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    chosen: List[int] = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(i - 1)
            c -= weights[i - 1]
    chosen.reverse()
    total_weight = sum(weights[i] for i in chosen)
    return KnapsackResult(dp[n][capacity], total_weight, chosen)

def dp_algorithm(values: List[int], weights: List[int], capacity: int) -> KnapsackResult:  # noqa: N802
    return knapsack(values, weights, capacity)