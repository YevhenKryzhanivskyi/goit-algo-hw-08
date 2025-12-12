import heapq
from typing import List


def min_merge_cost(lengths: List[int]) -> int:
    """
    Обчислює мінімальні можливі загальні витрати на об'єднання кабелів.

    Вартість кожного об'єднання дорівнює сумі довжин двох кабелів.
    Щоб мінімізувати загальну вартість, завжди об'єднуються два
    найкоротші кабелі (жадібний алгоритм).

    """
    if len(lengths) <= 1:
        return 0

    heap = lengths[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        merged = first + second
        total_cost += merged
        heapq.heappush(heap, merged)

    return total_cost


if __name__ == "__main__":
    print(min_merge_cost([8, 4, 6, 12]))  # 58
    print(min_merge_cost([20, 4, 8, 2]))  # 54
