
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# To understand this problem, check out the graph example on Leetcode.  Essentially, you have to determine the largest area of bar height combinations.  

# Brute force solution with nested loops.
def maxAreaBrute(heights):
    max_area = 0

    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            max_area = max(area, max_area)
    return max_area

print(maxAreaBrute([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49

# Optimized Solution

def maxAreaOpt(heights):
    max_area = 0
    left = 0
    right = len(heights) - 1
    while (left < right):
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)

        if (heights[left] < heights[right]):
            left +=1
        else:
            right -=1
    return max_area

print(maxAreaOpt([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
print(maxAreaOpt([1, 1])) # 1
