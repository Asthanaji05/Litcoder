import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Taking input for Charlie's triplet
        String[] strC = input.nextLine().split(" ");
        int[] c = new int[strC.length];
        for (int i = 0; i <c.length; i++) {
            c[i] = Integer.parseInt(strC[i]);
        }
        // Taking input for Dave's triplet
        String[] strD = input.nextLine().split(" ");
        int[] d = new int[strD.length];
        for (int i = 0; i < d.length; i++) {
            d[i] = Integer.parseInt(strD[i]);
        }
        
        // Compare the triplets and calculate scores
        int charliePoints = 0;
        int davePoints = 0;
        
        for (int i = 0; i < c.length; i++) {
            if (c[i] > d[i]) {
                charliePoints++;
            } else if (c[i] < d[i]) {
                davePoints++;
            }
        }
        
        // Output the scores
        System.out.print(charliePoints + " " + davePoints);
    }
}
