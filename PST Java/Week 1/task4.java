import java.util.Arrays;
import java.util.Scanner;

public class KthSmallest {
    public static void main(String[] args) {
        int[] arr = {12, 3, 5, 7, 19};

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter value of K: ");
        int k = sc.nextInt();

        if (k <= 0 || k > arr.length) {
            System.out.println("Invalid K");
            return;
        }

        Arrays.sort(arr);  // Sorting

        System.out.println(k + "th smallest element is: " + arr[k - 1]);

        sc.close();
    }
}
