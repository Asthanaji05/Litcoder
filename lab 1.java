import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        float[] ret = new float[a];
        for(int i = 0; i<a; i++){
            ret[i] = input.nextInt();
        }
        doSomething(a,ret);
    }
    
    public static void doSomething(int x, float[] y) {
        //Do Something
        float res[] = new float[3];
        for(float i : y){
            if(i>0){res[0]++;}
            else if(i<0){res[1]++ ;}
        }
        res[2] = x-res[0]-res[1];
        for(int i  = 0; i<3; i++){
            System.out.format("%.3f", res[i]/x);
            System.out.println();
        }
        return ;
    }
}