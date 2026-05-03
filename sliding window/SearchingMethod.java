import java.util.*;

public class SearchingMethod {

    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++)
            if (arr[i] == target) return i;
        return -1;
    }

     public static int binarySearchIterative(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

     public static int binarySearchRecursive(int[] arr, int low, int high, int target) {
        if (low > high) return -1;
        int mid = (low + high) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) return binarySearchRecursive(arr, mid + 1, high, target);
        return binarySearchRecursive(arr, low, mid - 1, target);
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 8, 10, 12, 14};
        int target = 12;

        System.out.println(binarySearchIterative(arr, target));
        System.out.println(binarySearchIterative(arr, target));
        System.out.println(binarySearchIterative(arr, 0, arr.length - 1, target));
        System.out.println(linearSearch(arr, target));
        System.out.println(linearSearch(arr, target));
        System.out.println(linearSearch(arr, 0, arr.length - 1, target));
        System.out.println(binarySearchRecursive(arr, target));
        System.out.println(binarySearchRecursive(arr, target));
        System.out.println(binarySearchRecursive(arr, 0, arr.length - 1, target));
    }
}
