class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ans=new ArrayList<>();
        Arrays.sort(nums);
        int l,r;
        for(int i=0;i<nums.length-3;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            for(int j=i+1;j<nums.length-2;j++){
                if(j>i+1 && nums[j]==nums[j-1]){
                    continue;
                }
                l=j+1;
                r=nums.length-1;
                while(l<r){
                    long sum=(long)nums[l]+nums[j]+nums[r]+nums[i];
                    if(sum==target){
                        ans.add(Arrays.asList(nums[i],nums[j],nums[l],nums[r]));
                        l++;
                        r--;
                        while(l<r && nums[l]==nums[l-1]){
                            l++;
                        }
                        while(l<r && nums[r]==nums[r+1]){
                            r--;
                        }
                    }
                    else if(sum<target){
                        l++;
                    }
                    else{
                        r--;
                    }
                }
            }
        }
        return ans;
    }
}