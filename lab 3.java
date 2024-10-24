import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
public class Main{
    public static boolean constraint(int[] arr){
        if(arr.length > 10 || arr.length <1){
            System.out.println("Array size must be between 1 and 10");
            return false;
        }
        for(int num : arr){
            if(num >10 || num < -10){
                System.out.println( "Array elements must be from -10 to 10");
                return false;
            }
        }
        return true;
    }
    public static boolean zero(int[] arr){
        int curr = 0;
        Set<Integer> sumSet = new HashSet<>();
        for(int num : arr){
            curr += num;
            if(curr == 0 || sumSet.contains(curr)){
                return true;
            }
            sumSet.add(curr);
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String[] input = scan.nextLine().split(" ");
        int[] arr = new int[input.length];
        try{
            for(int i = 0; i<input.length; i++){
                arr[i] = Integer.parseInt(input[i]);
            }
        }catch(NumberFormatException e){
            System.out.println("Array elements must be integers");
            return;
        }
        if(constraint(arr)){
            if(zero(arr)){
                System.out.println(true);
            }else{
                System.out.println(false);
            }
            System.out.println(arr.length);
        }
        scan.close();
    }
}