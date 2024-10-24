import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        CustomQueue queue = new CustomQueue();
        String[] commands = input.nextLine().split(",");
        for (String command : commands) {
            String[] parts = command.split(" ");
            int cmd = Integer.parseInt(parts[0]);
            switch (cmd) {
                case 1:
                    int valueToEnqueue = Integer.parseInt(parts[1]);
                    queue.enqueue(valueToEnqueue);
                    break;
                case 2:
                    queue.dequeue();
                    break;
                case 3:
                    System.out.println(queue.front());
                    break;
            }
        }
    }
}

class CustomQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    public CustomQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    public void enqueue(int value) {
        stack1.push(value);
    }
    public void dequeue() {
        moveStack1ToStack2();
        if (!stack2.isEmpty()) {
            stack2.pop();
        }
    }
    public int front() {
        moveStack1ToStack2();
        if (!stack2.isEmpty()) {
            return stack2.peek();
        }
        return -1;
    }
    private void moveStack1ToStack2() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
    }
}