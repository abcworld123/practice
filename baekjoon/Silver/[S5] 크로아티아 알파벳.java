import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.next().replace("dz=", "*").replace("c=", "*").replace("c-", "*").replace("d-", "*").replace("lj", "*").replace("nj", "*").replace("z=", "*").replace("s=", "*");
        System.out.println(s.length());
    }
}
