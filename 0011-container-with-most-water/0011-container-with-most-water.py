class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height) -1
        max_container= 0
        while p1 < p2:
            heights = min(height[p1],height[p2])
            weight = p2 - p1 
            container = heights*weight
            max_container = max(max_container,container)
            if height[p1] <= height[p2]:
                p1 +=1
            else:
                p2 -=1
        return max_container