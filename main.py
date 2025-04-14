#ok so you need to run this on the terminal, do something likee python main.py --file sample.txt --capacity 15
# I have a file mode and a random mode here as well dont know if the random one is necessary for project just made it because i hate the sample thing



import argparse
from pathlib import Path
from typing import List, Tuple

from dp_algorithm import dp_algorithm, KnapsackResult
import experimental_analysis as ea


def read_instance_from_file(path: Path, capacity: int | None = None) -> Tuple[List[int], List[int], int]:
    with path.open() as f:
        weights = list(map(int, f.readline().strip().split(',')))
        values = list(map(int, f.readline().strip().split(',')))
    if capacity is None:
        capacity = int(sum(weights) * 0.5)
    return values, weights, capacity


def pretty_print(result: KnapsackResult) -> None:
    print("Optimal value :", result.max_value)
    print("Total weight  :", result.total_weight)
    print("Items chosen  :", result.chosen_items)


def main() -> None:
    parser = argparse.ArgumentParser(description="0/1 Knapsack DP Project — no external libs required")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=Path, help="Path to input file (two comma‑separated lines)")
    group.add_argument("--random", action="store_true", help="Benchmark on random instances and print results")

    parser.add_argument("--capacity", type=int, help="Knapsack capacity (used with --file)")
    parser.add_argument("--max_n", type=int, default=200, help="Largest n for random benchmark")
    parser.add_argument("--step", type=int, default=20, help="Step size for n in random benchmark")

    args = parser.parse_args()

    if args.file:
        values, weights, cap = read_instance_from_file(args.file, args.capacity)
        result = dp_algorithm(values, weights, cap)
        pretty_print(result)
    else:
        sizes = list(range(args.step, args.max_n + 1, args.step))
        times = ea.time_algorithm(dp_algorithm, sizes)
        mem = ea.memory_algorithm(dp_algorithm, sizes)
        ea.output_results(sizes, times, mem)


if __name__ == "__main__":
    main()
