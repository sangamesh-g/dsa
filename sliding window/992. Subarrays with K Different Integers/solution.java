class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
    public int atMost(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        int l=0,cnt=0;
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            while(map.size()>k){
               map.put(nums[l],map.getOrDefault(nums[l],0)-1);
               if(map.get(nums[l])==0){
                map.remove(nums[l]);
               }
               l++;
            }
            cnt+=(i-l+1);
        }
        return cnt;
    }
}