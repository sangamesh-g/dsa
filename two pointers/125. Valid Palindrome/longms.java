class longms {
    public boolean isPalindrome(String s) {
         String str="";
        for(char ch:s.toCharArray()){
            if (Character.isLetterOrDigit(ch)){
                str+=Character.toLowerCase(ch);
            }
        }
        if(str.length()<=1){
            return true;
        }
        for(int i=0;i<str.length()/2;i++){
            if(str.charAt(i)!=str.charAt(str.length()-1-i)){
                return false;
            }
        }
        return true;
    }
}