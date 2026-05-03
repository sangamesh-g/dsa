930. Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
 
Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

 
Constraints:
1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
 
class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return countAtMost(nums, goal) - countAtMost(nums, goal - 1);
    }
    public int countAtMost(int[] nums, int goal){
        if (goal<0)return 0;
        int l=0,sum=0,count=0;
        for(int r=0;r<nums.length;r++){
            sum+=nums[r];
            while(sum>goal){
                sum-=nums[l];
                l++;
            }
           count += (r - l + 1);
        }
        return count;
    }
}

🔥 Part 1: Why
count += (right - left + 1);

Suppose:
nums = [1,0,1,0,1]
         ↑     ↑
       left   right
Assume:
left = 1
right = 3
Window = [0,1,0] → valid (sum ≤ k)

Question:
👉 How many subarrays END at index = 3?

All possibilities:
[0,1,0]   (start = left = 1)
[1,0]     (start = 2)
[0]       (start = 3)
👉 Total = 3

Formula:
(right - left + 1)
= (3 - 1 + 1)
= 3

🔥 Key Insight
At every right:
👉 You are counting:
“How many valid subarrays END at this index?”

Why this works?
Because:
Entire window [left → right] is valid
Any smaller window inside it is also valid

💀 Wrong Thinking
if (sum == goal) count++;
👉 Counts only 1 subarray
 👉 But actually there are many

🔥 Part 2: Why
atMost(goal) - atMost(goal - 1)

Problem:
We need:
sum == goal

But sliding window gives:
sum ≤ k

So we do:
exact(goal)
= atMost(goal) - atMost(goal - 1)

Example:
nums = [1,0,1]

All subarrays:
[1] → 1
[1,0] → 1
[1,0,1] → 2
[0] → 0
[0,1] → 1
[1] → 1

Buckets:
atMost(2):
👉 includes → 0,1,2
atMost(1):
👉 includes → 0,1

Difference:
👉 Only sum = 2 remains

🧠 Final Mental Model
Think:
atMost(k)     → big bucket
atMost(k - 1) → smaller bucket
👉 Subtract → get exact k

⚡ One more clarity (important)
👉 Why not direct sliding window for exact?
Because:
condition sum == goal is not stable
window keeps changing → you miss cases

🧠 Ultra Short Memory Line
If you forget everything:
1. Count subarrays ending at right → (right - left + 1)
2. Exact = atMost(k) - atMost(k-1)

😏 Quick check (answer mentally)
If:
left = 2
right = 6
👉 How many subarrays end at 6?
If you say instantly:
6 - 2 + 1 = 5
✅ Then you're getting it
 ❌ If not → we grind more 😄

