//lab 16
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the target sweetness level
        // System.out.print("Enter the target sweetness level: ");
        int targetSweetness = scanner.nextInt();

        // Read the sweetness levels of the candies
        // System.out.println("Enter the sweetness levels of the candies separated by space:");
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        // Continue reading integers from input until no more input is given
        while (scanner.hasNextInt()) {
            minHeap.add(scanner.nextInt());
        }

        int steps = calculateStepsToReachSweetness(minHeap, targetSweetness);
        System.out.println(steps);
    }

    public static int calculateStepsToReachSweetness(PriorityQueue<Integer> minHeap, int targetSweetness) {
        int steps = 0;

        // Continue combining candies until the least sweet candy meets the target sweetness
        while (minHeap.size() > 1 && minHeap.peek() < targetSweetness) {
            int leastSweet = minHeap.poll();
            int secondLeastSweet = minHeap.poll();

            // Combine the two candies to create a new candy
            int newSweetness = leastSweet + 2 * secondLeastSweet;
            minHeap.add(newSweetness);
            steps++;
        }

        // Check if the target sweetness is reached
        if (minHeap.peek() < targetSweetness) {
            return -1; // Impossible to reach target sweetness
        }

        return steps;
    }
}