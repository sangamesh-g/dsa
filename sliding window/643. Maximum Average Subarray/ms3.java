public class ms3 {
        public double findMaxAverage(int[] nums, int k) {
        int windowSum = 0;
        int n = nums.length;

        for(int i = 0; i <k; i++){
            windowSum += nums[i];
        }
         int maxSum = windowSum;
        
        // Step 2: Slide the window
        for (int i = k; i < n; i++) {
            windowSum += nums[i] - nums[i - k]; // add new, remove old
            maxSum = Math.max(maxSum, windowSum);
        }
        
        // Step 3: Return maximum average
        return (double) maxSum / k;

    }
}
