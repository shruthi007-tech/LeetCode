class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right= len(height)-1
        max_area=0
        while left<right:
            
           width=right-left
           height_value= min(height[left], height[right])
           area= width*height_value
           max_area= max(max_area,area)

           if height[left] < height[right]:
            left+=1
           else:
            right-=1
        return max_area



        