from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        pointer = 0

        for element in seq:

            new_index = None

            for child in self[pointer].children:
                if self[child].body == element:
                    new_index = child
                    break

            if new_index is None:
                self.append(TrieNode(body=element))

                new_index = len(self) - 1

                self[pointer].children.append(new_index)

            pointer = new_index

        self[pointer].is_end = True
    # 구현하세요!
    def dfs(self, node: int, factorial: list[int]) -> int:
        result = 1
        child_cnt = 0

        for child in self[node].children:
            result *= self.dfs(child, factorial)
            result %= 1000000007
            child_cnt += 1

        # 단어의 끝도 하나의 선택지로 취급
        if self[node].is_end:
            child_cnt += 1

        result *= factorial[child_cnt]
        result %= 1000000007

        return result


import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
    MOD = 1000000007

    n = int(input())

    trie: Trie[str] = Trie()

    words = []
    for _ in range(n):
        word = input().strip()
        words.append(word)

    words.sort()

    for word in words:
        trie.push(word)

    factorial = [1] * (n + 2)
    for i in range(2, n + 2):
        factorial[i] = factorial[i - 1] * i % MOD

    print(trie.dfs(0, factorial))


if __name__ == "__main__":
    main()