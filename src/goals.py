from typing import List, Tuple


def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    if k <= 0:
        raise ValueError("k must be greater than 0")
    if k > len(values):
        return None

    max_sum = sum(values[:k])
    max_index = 0
    current_sum = max_sum

    for i in range(1, len(values) - k + 1):
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i

    return (max_index, max_sum)


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    if k <= 0:
        raise ValueError("k must be greater than 0")
    if k > len(values):
        return 0

    count = 0
    current_sum = sum(values[:k])
    if current_sum / k >= target_avg:
        count += 1

    for i in range(1, len(values) - k + 1):
        current_sum = current_sum - values[i - 1] + values[i + k - 1]
        if current_sum / k >= target_avg:
            count += 1

    return count


def longest_rising_streak(values: List[int]) -> int:
    if not values:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
