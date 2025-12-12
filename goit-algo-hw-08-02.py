import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
   #  Об'єднує k відсортованих списків в один відсортований список.
    heap = []
    result = []

    # Заповнюємо купу першими елементами кожного списку
    for list_idx, lst in enumerate(lists):
        if lst:  # перевірка, що список не порожній
            heapq.heappush(heap, (lst[0], list_idx, 0))

    # Дістаємо найменший елемент та додаємо наступний з того ж списку
    while heap:
        value, list_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            next_value = lists[list_idx][next_idx]
            heapq.heappush(heap, (next_value, list_idx, next_idx))

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
