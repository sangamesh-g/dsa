
public class mysolution {
     public int maxVowels(String s, int k) {
        int v=0,maxv=0;
        int l=0;
        for(int r=0;r<k;r++){
            if(checkvowel(s.charAt(r))){
                v++;
            }
        }
        maxv=v;
        for(int r=k;r<s.length();r++){
            if(checkvowel(s.charAt(l))){
                v--;
            }
            l++;
            if(checkvowel(s.charAt(r))){
                v++;
            }
            maxv=Math.max(v,maxv);
        }
        return maxv;
    }
    public boolean checkvowel(char ch){
        return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';
    }
}
