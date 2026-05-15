class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> map=new HashMap<>();
        long max=0,sum=0;
        int l=0;
        for(int r=0;r<nums.length;r++){
            sum+=nums[r];
            map.put(nums[r],map.getOrDefault(nums[r],0)+1);
            if(r-l+1>k){
                sum-=nums[l];
                map.put(nums[l],map.getOrDefault(nums[l],0)-1);
                if(map.get(nums[l])<=0){
                    map.remove(nums[l]);
                }
                l++;
            }
            if(r-l+1==k && map.size()==k){
                max=Math.max(max,sum);
            }
        }
        return max;
    }
}



class Solution11 {
    public long maximumSubarraySum(int[] nums, int k) {
        long sum = 0, maxSum = 0;
        int j = 0;
        Set<Integer> st = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            while(st.contains(nums[i]) || i - j >= k){
                st.remove(nums[j]);
                sum -= nums[j];
                j++;
            }
            st.add(nums[i]);
            if(i - j + 1 == k)
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum;
    }
}
