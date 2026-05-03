public class ms5 {
    public double findMaxAverage(int[] nums, int k) {
        double sum=0,maxavg=Double.NEGATIVE_INFINITY;
        for(int i=0;i<k;i++){
           sum+=nums[i];
        }
        maxavg=sum/k;
        for(int i=0;i<nums.length-k;i++){
            sum=sum-nums[i]+nums[i+k];
            maxavg = Math.max(maxavg, sum/k);
        }
        return maxavg;
            }

    
}
