import java.util.Scanner;
public class Main {
    public static void doSomething(int inval) {
        String strinval = String.valueOf(inval);
        if(strinval.length() <4){
            System.out.println("Provided input is less than 4, enter four digit integers");
        }else if(strinval.length() >4){
            System.out.println("Provided input is more than 4, enter four digit integers");
        }else{
            int[] rem = new int[4];
            for(int i = 0; i<4; i++){
                rem[i] = ((inval % 10) + 5)%10;
                inval /= 10;
            }
            System.out.println(rem[0]*100+rem[1]*1000+rem[2]+rem[3]*10);
        }}
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try{
            int input  = Integer.parseInt(scan.nextLine());
            doSomething(input);
        }catch(NumberFormatException e){
            System.out.println("Enter only Integer value");
        }finally{
            scan.close();
        }}
}