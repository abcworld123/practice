import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x1, y1, r1, x2, y2, r2;
        int k = sc.nextInt();

        for (int i = 0; i < k; i++)
        {
            x1 = sc.nextInt();
            y1 = sc.nextInt();
            r1 = sc.nextInt();
            x2 = sc.nextInt();
            y2 = sc.nextInt();
            r2 = sc.nextInt();

            double dist = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
            int ans;

            if (x1 == x2 && y1 == y2) ans = r1 == r2 ? -1 : 0;

            else if (dist < r1 + r2)
            {
                if (r1 > dist + r2 || r2 > dist + r1) ans = 0;
                else if (r1 == dist + r2 || r2 == dist + r1) ans = 1;
                else ans = 2;
            }
            else if (dist == r1 + r2) ans = 1;
            else ans = 0;

            System.out.println(ans);
        }
    }
}
