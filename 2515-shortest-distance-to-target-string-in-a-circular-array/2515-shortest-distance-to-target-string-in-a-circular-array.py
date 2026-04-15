class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        answer=float('inf')
        total=len(words)
        for ind, word in enumerate(words):
            if word==target:
                #we found a ind match
                dist = abs(startIndex-ind) #direct movement towards left or right
                answer= min(answer, dist, total-dist) #going towards the left and coming from the other end
        if answer==float('inf'):
            return -1
        