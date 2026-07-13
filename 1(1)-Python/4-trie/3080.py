from lib import Trie
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