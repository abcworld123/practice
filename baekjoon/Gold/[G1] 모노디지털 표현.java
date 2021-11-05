import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int k = sc.nextInt();
		ArrayList<HashSet<Integer>> list = new ArrayList<>();

		for (int i = 1; i <= 8; i++) {
			HashSet<Integer> set = new HashSet<>(Set.of(Integer.parseInt(Integer.toString(N).repeat(i))));
			for (int j = 1; j < i; j++) {
				for (int x : list.get(j - 1)) {
					for (int y : list.get(i - j - 1)) {
						set.add(x + y);
						set.add(x - y);
						set.add(x * y);
						if (y != 0) set.add(x / y);
					}
				}
			}
			list.add(set);
		}

		for (int i = 0; i < k; i++) {
			int x = sc.nextInt();
			for (int j = 0; j < 8; j++) {
				if (list.get(j).contains(x)) {
					System.out.println(j + 1);
					break;
				}
				else if (j == 7) {
					System.out.println("NO");
				}
			}
		}
	}
}
