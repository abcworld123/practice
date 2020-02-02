import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int ans;
        char op;

        ans = sc.nextInt();
        while (true)
        {
            op = sc.next().charAt(0);
            if (op == '+') ans += sc.nextInt();
            else if (op == '-') ans -= sc.nextInt();
            else if (op == '*') ans *= sc.nextInt();
            else if (op == '/') ans /= sc.nextInt();
            else if (op == '=') break;
        }
        System.out.println(ans);
    }
}
