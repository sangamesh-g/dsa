public class sort {
    public static void main(String[] ar){
        int[] a={1,3,65,34,76,32};int temp,sm;
        int[] insertion=a,selection=a,bubble=a;
        //insertion sort
        for(int i=1;i<insertion.length;i++){
            int curr=insertion[i];
            int j=i-1;
            while(j>=0 && curr<insertion[j]){
                insertion[j+1]=insertion[j];
                j--;
            }
            insertion[j+1]=curr;
        }
        //bubble sort
        for(int i=0;i<bubble.length-1;i++){
            for(int j=0;j<bubble.length-i-1;j++){
                if(bubble[j]>bubble[j+1]){
                    temp=bubble[j];
                    bubble[j]=bubble[j+1];
                    bubble[j+1]=temp;
                }
            }
        }
        //selection sort
        for(int i=0;i<selection.length-1;i++){
            sm=i;
            for(int j=i+1;j<=selection.length-1;j++){
                if(selection[sm]>selection[j]){
                    sm=j;
                }
            }
            if(sm!=i){
                temp=selection[sm];
                selection[sm]=selection[i];
                selection[i]=temp;
            }
        }
        System.out.println("Insertion sort:"+java.util.Arrays.toString(insertion));
        System.out.println("Selection sort:"+java.util.Arrays.toString(selection));
        System.out.println("Bubble sort:"+java.util.Arrays.toString(bubble));
    }
}
