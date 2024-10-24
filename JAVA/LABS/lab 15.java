// lab 15
import java.util.*;

public class Main {

    private static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt(); // Height of the wall
        int m = input.nextInt(); // Width of the wall
        
        // Call the function to calculate the number of ways to build the wall
        System.out.println(legoWall(n, m));
    }

    // Function to calculate the number of ways to build the wall
    public static long legoWall(int n, int m) {
        // Step 1: Calculate the number of possible row combinations for width 'm'
        long[] rowWays = new long[m + 1];
        rowWays[0] = 1; // Base case: 1 way to build a wall of width 0

        // For each width, calculate how many ways we can fill it with the available bricks
        for (int width = 1; width <= m; width++) {
            rowWays[width] = rowWays[width - 1]; // 1x1 brick
            if (width >= 2) rowWays[width] = (rowWays[width] + rowWays[width - 2]) % MOD; // 1x2 brick
            if (width >= 3) rowWays[width] = (rowWays[width] + rowWays[width - 3]) % MOD; // 1x3 brick
            if (width >= 4) rowWays[width] = (rowWays[width] + rowWays[width - 4]) % MOD; // 1x4 brick
        }

        // Step 2: Calculate the total number of ways to fill the entire wall with height 'n' and width 'm'
        long[] totalWays = new long[m + 1];
        for (int width = 0; width <= m; width++) {
            totalWays[width] = modPow(rowWays[width], n, MOD);
        }

        // Step 3: Calculate the number of valid walls (without a vertical break)
        long[] validWalls = new long[m + 1];
        validWalls[0] = 1; // Base case: 1 way to build a wall of width 0

        for (int width = 1; width <= m; width++) {
            long result = totalWays[width];
            for (int i = 1; i < width; i++) {
                result = (result - validWalls[i] * totalWays[width - i] % MOD + MOD) % MOD;
            }
            validWalls[width] = result;
        }

        return validWalls[m];
    }

    // Function to calculate (base^exp) % mod
    public static long modPow(long base, int exp, int mod) {
        long result = 1;
        base = base % mod;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
}
