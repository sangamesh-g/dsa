class mySolution {
    public boolean checkInclusion(String s1, String s2) {
        String sm = s1;
        String sf = s2;
        HashMap<Character, Integer> map = new HashMap<>();
        char a;
        for(int i=0;i<sm.length();i++){
            a=sm.charAt(i);
            map.put(a,map.getOrDefault(a,0)+1);
        }
        // for (char ch : sm.toCharArray()) {
        //     map.put(ch, map.getOrDefault(ch, 0) + 1);
        // }
        HashMap<Character, Integer> window = new HashMap<>();
        int l = 0;
        for(int r=0;r<sf.length();r++){
            a=sf.charAt(r);
            window.put(a,window.getOrDefault(a,0)+1);
            if(r-l+1>sm.length()){
                char leftchar=sf.charAt(l);
                window.put(leftchar,window.get(leftchar)-1);

                if(window.get(leftchar)==0){
                    window.remove(leftchar);
                }
                l++;
            }
            if(window.equals(map)){
                    return true;
                }
        }
    return false;
    }
}