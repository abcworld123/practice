class Node:
    def __init__(self, n):
        self.n = n
        self.s_win = set()
        self.s_lose = set()
        self.winner = []
        self.loser = []


def search_win(x):
    if x.s_win: return x.s_win
    x.s_win.add(x.n)
    for w in x.winner: x.s_win |= search_win(w)
    return x.s_win


def search_lose(x):
    if x.s_lose: return x.s_lose
    x.s_lose.add(x.n)
    for l in x.loser: x.s_lose |= search_lose(l)
    return x.s_lose


def solution(n, results):
    graph = [Node(x) for x in range(n)]
    for w, l in results:
        graph[w - 1].winner.append(graph[l - 1])
        graph[l - 1].loser.append(graph[w - 1])

    return [len(search_win(x) | search_lose(x)) for x in graph].count(n)
