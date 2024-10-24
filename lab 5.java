import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        StringBuilder res = new StringBuilder("");
        int[] arr = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr[i] = Integer.parseInt(input[i]);
            arr[i] = dosomething(arr[i]);
            if (arr[i] % 2 == 0) {
                res.append(arr[i]);
            } else {
                res.append((char) ('a' + arr[i] - 1));
            }
        }
        System.out.println(res.toString());
        scanner.close();
    }
    public static int dosomething(int num) {
        while (num > 9) {
            num = sumofdigits(num);
        }
        return num;
    }
    public static int sumofdigits(int num) {
        int sum = 0;
        if (num < 10) {
            return num;
        } else if (num % 10 == 0) {
            return sumofdigits(num / 10);
        }
        while (num % 10 != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}