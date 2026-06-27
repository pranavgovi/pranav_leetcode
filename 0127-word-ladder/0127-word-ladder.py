class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from queue import deque
        lookup=defaultdict(list)
        #Building the neigbour lookup
        #here bfs will be more efficient as it can find the shortest path
        for word in wordList:
            n=len(word)
            for i in range(n):
                key = word[:i]+ '.'+ word[i+1:]
                lookup[key].append(word)
    
        visited= set()
        
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)
        answer=1
        while queue:
            x =len(queue)
            for i in range(x):
                node = queue.popleft()
                if node==endWord:
                    return answer
                for i in range(len(node)):
                    pat = node[:i] + '.' + node[i+1:]
                    for nei in lookup[pat]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            answer+=1
        return 0