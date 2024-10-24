import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] inputArr = sc.nextLine().split(" ");
        int[] arr = new int[inputArr.length];
        for (int i = 0; i < inputArr.length; i++) {
            arr[i] = Integer.parseInt(inputArr[i]);
        }
        Map<Integer,Integer> mp = new HashMap<>();
        int max = arr[0];
        int mxc = 0;
        for(int i = 0;i<arr.length; i++){
            mp.put(arr[i], mp.getOrDefault(arr[i],0)+1);
            if(mp.get(arr[i]) > mxc){
                mxc = mp.get(arr[i]);
                max = arr[i];
            }else if(mp.get(arr[i]) == mxc){
                max = Math.min(arr[i], max);
            }else{
                continue;
            }
        }
        System.out.println(max);
        sc.close();
    }
}