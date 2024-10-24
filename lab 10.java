// lab 10
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input the array size and the number of operations
        int n = input.nextInt();  // size of the array
        int m = input.nextInt();  // number of operations

        // Create an array to store the differences
        long[] array = new long[n + 1];  // extra element for easier boundary handling

        // Loop through each operation
        for (int i = 0; i < m; i++) {
            int a = input.nextInt();  // start index
            int b = input.nextInt();  // end index
            int k = input.nextInt();  // value to add

            array[a - 1] += k;        // adding at the start of the range
            if (b < n) {
                array[b] -= k;        // subtracting just after the end of the range
            }
        }

        // Now we find the maximum value after calculating the prefix sum
        long maxValue = Long.MIN_VALUE;
        long current = 0;
        for (int i = 0; i < n; i++) {
            current += array[i];
            if (current > maxValue) {
                maxValue = current;
            }
        }

        // Output the maximum value
        System.out.println(maxValue);
    }
}