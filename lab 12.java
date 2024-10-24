// lab 12
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        CustomStack textEditor = new CustomStack();

        // Read the input as a single string and split by commas
        String[] commands = input.nextLine().split(",");

        for (String command : commands) {
            String[] parts = command.split(" ");
            int cmd = Integer.parseInt(parts[0]);

            switch (cmd) {
                case 1:
                    // Insert command
                    String valueToInsert = parts[1];
                    textEditor.insert(valueToInsert);
                    break;
                case 2:
                    // Delete command
                    int charsToDelete = Integer.parseInt(parts[1]);
                    textEditor.delete(charsToDelete);
                    break;
                case 3:
                    // Get command
                    int indexToGet = Integer.parseInt(parts[1]);
                    System.out.println(textEditor.get(indexToGet));
                    break;
                case 4:
                    // Undo command
                    textEditor.undo();
                    break;
            }
        }
    }
}

class CustomStack {
    private StringBuilder text;
    private Stack<Command> commandHistory;

    public CustomStack() {
        text = new StringBuilder();
        commandHistory = new Stack<>();
    }
    public void insert(String value) {
        text.append(value);
        commandHistory.push(new Command(1, value));
    }

    // Delete the last value characters from the text
    public void delete(int value) {
        String deleted = text.substring(text.length() - value);
        text.delete(text.length() - value, text.length());
        commandHistory.push(new Command(2, deleted));
    }
    public char get(int index) {
        return text.charAt(index - 1);
    }
    public void undo() {
        if (!commandHistory.isEmpty()) {
            Command lastCommand = commandHistory.pop();
            if (lastCommand.type == 1) {
                text.delete(text.length() - lastCommand.value.length(), text.length());
            } else if (lastCommand.type == 2) {
                text.append(lastCommand.value);
            }
        }
    }
    private static class Command {
        int type;
        String value;
        public Command(int type, String value) {
            this.type = type;
            this.value = value;
        }
    }
}