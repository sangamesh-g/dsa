class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum,avg,maxavg=Double.NEGATIVE_INFINITY;
        for(int i=0;i<=nums.length-k;i++){
            sum=0;
            for(int j=0;j<k;j++){
                sum+=nums[i+j];
            }
            avg=sum/k;
            if(maxavg<(avg)){
                maxavg=avg;
            }
        }
        return maxavg;
    }
}
