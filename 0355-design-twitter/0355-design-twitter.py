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
        max_heap = []
        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            total = len(self.posts[followee])
            if total>=1:
                time, tweetid = self.posts[followee][total-1]    
                heapq.heappush(max_heap, (-time, tweetid, total-1, followee))
                if len(max_heap)>10:
                    heapq.heappop(max_heap)
        
        answer = []
        while max_heap and len(answer)<10:

            _, tweet, index, followee = heapq.heappop(max_heap)
            answer.append(tweet)
            index-=1
            if index>=0:
                timer, id = self.posts[followee][index]
                heapq.heappush(max_heap, (-timer, id, index, followee))
        self.followers[userId].remove(userId)
        return answer


        

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