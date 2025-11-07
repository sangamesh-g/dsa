import java.util.*;

public class SearchingMethod {

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++)
            if (arr[i] == target) return i;
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 8, 10, 12, 14};
        int target = 10;

        System.out.println(linearSearch(arr, target));
        System.out.println(linearSearch(arr, target));
        System.out.println(linearSearch(arr, 0, arr.length - 1, target));
    }
}
