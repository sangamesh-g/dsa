class Solution {
    public int subarraySum(int[] nums, int k) {
        int cnt=0;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==k){
                cnt++;
            }if(nums[i]+nums[i+1]==k){
                cnt++;
            }
        }
        if(nums[nums.length-1]==k){
            cnt++;
        }
        return cnt;
    }
}
