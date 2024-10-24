import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int ret = doSomething(a);        
        System.out.println(ret);
    }
    
    public static int doSomething(int x) {
        int ans = 0;
        for(int i = x; i>1; i--){
            if(isPrime(i) && chkDigits(i)){
                ans = i;
                break;
            }
        }
        return ans;
    }
    public static boolean chkDigits(int x){
        Set<Integer> mySet = new HashSet<>();
        mySet.add(2);
        mySet.add(3);
        mySet.add(5);
        mySet.add(7);
        mySet.add(9);
        int a = x;
        int lastdigit = 11;
        while(a>0){
            int digit = a%10;
            if(mySet.contains(digit) == false || digit > lastdigit) return false;
            a /= 10;
            lastdigit = digit;
        }
        return true;
    }
    public static boolean isPrime(int x){
        if(x<2) return false;
        int a = x;
        for(int i = 2; i<x/2; i++){
            if(a%i == 0) return false;
        }
        return true;
    }
}