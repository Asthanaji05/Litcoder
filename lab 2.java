import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt(); // HOURS
        int b = input.nextInt(); // DEVICES
        if(a>4){
            int res1 = Math.floorDiv(a,4);
            int res2;
            if(res1 < b){
                res2 = b - res1;
            }
            else{
                res1 = b;
                res2 = 0;
            }
        
            System.out.println(res1);
            System.out.println(res2);
        }
        else{
            System.out.println("Invalid Input");
        }
    }
    
    
}