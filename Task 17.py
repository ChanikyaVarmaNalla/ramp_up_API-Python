import collections

def shortestSuperstring(words):
    # Function to find the overlap between two strings
    def overlap(a, b):
        for i in range(min(len(a), len(b)), -1, -1):
            if a.endswith(b[:i]):
                return i
        return 0

    # Create a graph with nodes as words and edges as the overlap between words
    graph = [[overlap(words[i], words[j]) for j in range(len(words))] for i in range(len(words))]
    dp = [[0] * len(words) for _ in range(1 << len(words))]
    parent = [[None] * len(words) for _ in range(1 << len(words))]

    for mask in range(1, 1 << len(words)):
        for bit in range(len(words)):
            if not (mask & (1 << bit)):
                continue
            pmask = mask ^ (1 << bit)
            if pmask == 0:
                continue
            for pbit in range(len(words)):
                if not (pmask & (1 << pbit)):
                    continue
                val = dp[pmask][pbit] + graph[pbit][bit]
                if val > dp[mask][bit]:
                    dp[mask][bit] = val
                    parent[mask][bit] = pbit

    # Find the last word in the superstring
    cur = max(range(len(words)), key=lambda x: dp[-1][x])

    # Build the superstring by backtracking through the parent pointers
    mask = (1 << len(words)) - 1
    path = []
    while cur is not None:
        path.append(cur)
        p = parent[mask][cur]
        mask ^= 1 << cur
        cur = p

    path = path[::-1]
    res = words[path[0]]
    for i in range(1, len(path)):
        overlap_val = graph[path[i - 1]][path[i]]
        res += words[path[i]][overlap_val:]

    return res

# Example usage:
words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
print(shortestSuperstring(words))
