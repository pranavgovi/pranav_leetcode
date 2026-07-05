from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) #this maps users to posts
        self.timer = 0
        self.followers =  defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.posts[userId].append((self.timer, tweetId))
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            for post in self.posts[followee]:
                time, tweetid = post
                heapq.heappush(min_heap, (time, tweetid))
        
                if len(min_heap)>10:
                    heapq.heappop(min_heap)
        

        self.followers[userId].remove(userId)
        
        min_heap.sort(key= lambda x : x[0], reverse= True)
        return [tweetid for (time, tweetid) in min_heap]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)