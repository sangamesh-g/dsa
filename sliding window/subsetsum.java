import java.util.*;

class subsetsum{
    public static void subset(int idx,int[] arr,ArrayList<Integer> curr,ArrayList<ArrayList<Integer>> result,int t){
    if(idx==arr.length){
        if(t==0){
            result.add(new ArrayList<>(curr));
        }
        return;
    }
    curr.add(arr[idx]);
    subset(idx+1,arr,curr,result,t-arr[idx]);
    curr.remove(curr.size()-1);
    subset(idx+1,arr,curr,result,t);


    }
    public static void main(String a[]){
        int[] arr = {2, 4, 6, 8, 10};
        int target = 16;
        ArrayList<ArrayList<Integer>> result=new ArrayList<>();
        subset(0,arr, new ArrayList<>(), result,target);
        System.out.println("Subsets with sum " + target + ": " + result);
    }
}