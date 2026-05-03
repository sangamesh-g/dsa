class Solution {
    public int maxVowels(String s, int k) {
        int left = 0; int countVowel = 0; int maxCount = 0;
        for(int right = 0; right<s.length(); right++){
            char ch = s.charAt(right);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                countVowel++;
            }
            while(right-left+1 > k){
                char leftch = s.charAt(left);
                if(leftch=='a'||leftch=='e'||leftch=='i'||leftch=='o'||leftch=='u'){
                    countVowel--;
                }
                    left++;    
            }
            maxCount = Math.max(maxCount,countVowel);
         
        }
        return maxCount;
    }
}
