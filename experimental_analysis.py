from __future__ import annotations
import csv
import random
import time
import tracemalloc
from typing import Callable, List, Tuple

from knapsack import knapsack

#Generates random instances of varying n, it Times the algorithm with time.perf_counter.
# it Measures peak memory with tracemalloc.
# it prints a neat table and writes times.csv, memory.csv so we can make graphs for the paper?


def generate_instance(n: int, *, max_weight: int = 100, max_value: int = 100,
                      capacity_ratio: float = 0.5) -> Tuple[List[int], List[int], int]:
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values = [random.randint(1, max_value) for _ in range(n)]
    capacity = int(sum(weights) * capacity_ratio)
    return values, weights, capacity

def time_algorithm(algorithm: Callable[[List[int], List[int], int], KnapsackResult],
                   sizes: List[int]) -> List[float]:
    times: List[float] = []
    for n in sizes:
        values, weights, cap = generate_instance(n)
        start = time.perf_counter()
        algorithm(values, weights, cap)
        times.append(time.perf_counter() - start)
    return times


def memory_algorithm(algorithm: Callable[[List[int], List[int], int], KnapsackResult],
                     sizes: List[int]) -> List[int]:
    peaks: List[int] = []
    for n in sizes:
        values, weights, cap = generate_instance(n)
        tracemalloc.start()
        algorithm(values, weights, cap)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peaks.append(peak // 1024)  # KiB
    return peaks


def write_csv(filename: str, header: List[str], rows: List[Tuple]) -> None:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def output_results(sizes: List[int], times: List[float], mem: List[int], *,
                   save_csv: bool = True) -> None:
    print("\nEmpirical Results (0/1 Knapsack)\n" + "-" * 40)
    print(f"{'n':>6} | {'time (s)':>10} | {'memory (KiB)':>14}")
    print("-" * 40)
    for n, t, m in zip(sizes, times, mem):
        print(f"{n:6d} | {t:10.6f} | {m:14d}")
    if save_csv:
        write_csv("times.csv", ["n", "time_s"], list(zip(sizes, times)))
        write_csv("memory.csv", ["n", "memory_kib"], list(zip(sizes, mem)))
        print("\nCSV files 'times.csv' and 'memory.csv' written — import them into Excel, Google Sheets, or any plotting tool you like.")


if __name__ == "__main__": # activites file as input
    import argparse
# builds random list of inputs, runtime / memory algo using the knapsack() and prints the table
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_n", type=int, default=200)   # basically just defaults if you dont specify in the terminal
    parser.add_argument("--step",  type=int, default=20)
    parser.add_argument("--no_csv", action="store_true")
    args = parser.parse_args()
# write times.csv and memory if we need to use that for the graph, if not we can just take it out.
    sizes = list(range(args.step, args.max_n + 1, args.step))
    times = time_algorithm(knapsack, sizes)
    mem   = memory_algorithm(knapsack, sizes)
    output_results(sizes, times, mem, save_csv=not args.no_csv)
