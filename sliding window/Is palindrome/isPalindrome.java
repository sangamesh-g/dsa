class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)return false;
        if(x%10==0 && x!=0) return false;

        int n=0;
        while(x>n){
            n=n*10+x%10;
            x/=10;
        }
        return n==x || n/10==x;
    }
}
