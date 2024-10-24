// lab 11
import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> arr1 = readInputArrayList(input);
        ArrayList<Integer> arr2 = readInputArrayList(input);
        ArrayList<Integer> arr3 = readInputArrayList(input);
        findCommonElements(arr1, arr2, arr3);
    }
    public static ArrayList<Integer> readInputArrayList(Scanner input) {
        ArrayList<Integer> list = new ArrayList<>();
        String line = input.nextLine();
        String[] parts = line.split(" ");
        for (String part : parts) {
            list.add(Integer.parseInt(part));
        }
        return list;
    }
    public static void findCommonElements(ArrayList<Integer> arr1, ArrayList<Integer> arr2, ArrayList<Integer> arr3) {
        int i = 0, j = 0, k = 0;
        boolean found = false;
        while (i < arr1.size() && j < arr2.size() && k < arr3.size()) {
            if (arr1.get(i).equals(arr2.get(j)) && arr2.get(j).equals(arr3.get(k))) {
                System.out.print(arr1.get(i) + " ");
                found = true;
                i++;
                j++;
                k++;
            }
            else if (arr1.get(i) < arr2.get(j)) {
                i++;
            } else if (arr2.get(j) < arr3.get(k)) {
                j++;
            } else {
                k++;
            }
        }
        if (!found) {
            System.out.println("No Elements");
        }
    }
}