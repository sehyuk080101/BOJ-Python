import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = a.toUpperCase();
        
        for (int i = 0; i < a.length(); i++) {
            char c = a.charAt(i);
            if (c == b.charAt(i)) {
                System.out.print(Character.toLowerCase(c));
            } else {
                System.out.print(Character.toUpperCase(c));
            }
        }
    }
}