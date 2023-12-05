import sys
from typing import List

def n_queens(n: int) -> List[List[str]]:
    def can_place(pos: int, occupied_columns: List[int]) -> bool:
        for i in range(len(occupied_columns)):
            if occupied_columns[i] == pos or \
               occupied_columns[i] - i == pos - occupied_columns[i] or \
               occupied_columns[i] + i == pos + occupied_columns[i]:
                return False
        return True

    def backtrack(solution: List[int]) -> List[List[str]]:
        if len(solution) == n:
            return [["."] * i + ["Q"] + ["."] * (n - i - 1) for i in solution]
        result = []
        for pos in range(n):
            if can_place(pos, solution):
                solution.append(pos)
                result.extend(backtrack(solution))
                solution.pop()
        return result

    return backtrack([])

print(n_queens(8))
