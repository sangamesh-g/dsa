class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int a:arr){
            map.put(a,map.getOrDefault(a,0)+1);
        }
        HashSet<Integer> seen=new HashSet<>();
        for(int a:map.values()){
            if(seen.contains(a))return false;
            seen.add(a);
        }
        return true;
    }
}
