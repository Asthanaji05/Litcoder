package Java;

public class lab 14 {
    
}
// lab 14
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Read input strings
        String start = input.nextLine();
        String end = input.nextLine();

        // Call the function to check if transformation is possible
        System.out.println(canTransform(start, end));
    }

    public static boolean canTransform(String start, String end) {
        // First, both strings must have the same length to be transformable
        if (start.length() != end.length()) {
            return false;
        }

        // Filter out all 'X' characters from both strings, only keeping 'L' and 'R'
        String filteredStart = start.replace("X", "");
        String filteredEnd = end.replace("X", "");

        // After removing 'X', both strings must be identical
        if (!filteredStart.equals(filteredEnd)) {
            return false;
        }

        // Now check the positions of 'L' and 'R'
        // 'L' can only move left, and 'R' can only move right
        int p1 = 0, p2 = 0;
        int n = start.length();

        // Loop through the strings and check valid movements
        while (p1 < n && p2 < n) {
            // Skip 'X' in both strings
            while (p1 < n && start.charAt(p1) == 'X') p1++;
            while (p2 < n && end.charAt(p2) == 'X') p2++;

            // If either pointer exceeds the length of the string, stop the loop
            if (p1 == n || p2 == n) break;

            // Check if characters at p1 and p2 are the same
            if (start.charAt(p1) != end.charAt(p2)) {
                return false;
            }

            // Validate 'L' movement: 'L' in start cannot move to the right (p1 must be >= p2)
            if (start.charAt(p1) == 'L' && p1 < p2) {
                return false;
            }

            // Validate 'R' movement: 'R' in start cannot move to the left (p1 must be <= p2)
            if (start.charAt(p1) == 'R' && p1 > p2) {
                return false;
            }

            // Move both pointers forward
            p1++;
            p2++;
        }

        // After the loop, both pointers should have traversed the whole string
        return true;
    }
}