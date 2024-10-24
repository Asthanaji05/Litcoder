import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Step 1: Taking the divisor as input
        int divisor = sc.nextInt();
        sc.nextLine();  // Consume the newline

        // Step 2: Taking space-separated integers as input and storing in an array
        String[] inputArr = sc.nextLine().split(" ");
        int[] arr = new int[inputArr.length];
        
        // Convert string array to integer array
        for (int i = 0; i < inputArr.length; i++) {
            arr[i] = Integer.parseInt(inputArr[i]);
        }

        // Step 3: Array to store remainder frequencies
        int[] remainderFreq = new int[divisor];
        
        // Step 4: Count remainders when divided by divisor
        for (int num : arr) {
            remainderFreq[num % divisor]++;
        }

        // Step 5: Calculate pairs whose sum is divisible by divisor
        int count = 0;

        // Case 1: Pairs with remainder 0 (evenly divisible by divisor)
        count += (remainderFreq[0] * (remainderFreq[0] - 1)) / 2;

        // Case 2: Pairs where remainder i and divisor-i add up to divisor
        for (int i = 1; i <= divisor / 2; i++) {
            if (i != divisor - i) {
                count += remainderFreq[i] * remainderFreq[divisor - i];
            }
        }

        // Case 3: If divisor is even, count pairs where remainder is exactly divisor/2
        if (divisor % 2 == 0) {
            count += (remainderFreq[divisor / 2] * (remainderFreq[divisor / 2] - 1)) / 2;
        }

        // Output the result
        System.out.println(count);
        sc.close();
    }
}