import java.util.LinkedList;
import java.util.Queue;

class Solution {
	public int[] solution(int m, int n, int[][] picture) {
		int numberOfArea = 0;
		int maxSizeOfOneArea = 0;
		boolean[][] checked = new boolean[m][n];
		Queue<int[]> queue = new LinkedList<>();

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (picture[i][j] == 0 || checked[i][j]) continue;
				int curAreaSize = 0;
				numberOfArea++;
				queue.offer(new int[] {i, j, picture[i][j]});

				while (!queue.isEmpty()) {
					int[] cur = queue.poll();
					int y = cur[0], x = cur[1], color = cur[2];
					if (checked[y][x]) continue;
					curAreaSize++;
					checked[y][x] = true;
					if (y - 1 >= 0 && picture[y - 1][x] == color && !checked[y - 1][x]) queue.offer(new int[] {y - 1, x, picture[y - 1][x]});
					if (x + 1 < n  && picture[y][x + 1] == color && !checked[y][x + 1]) queue.offer(new int[] {y, x + 1, picture[y][x + 1]});
					if (y + 1 < m  && picture[y + 1][x] == color && !checked[y + 1][x]) queue.offer(new int[] {y + 1, x, picture[y + 1][x]});
					if (x - 1 >= 0 && picture[y][x - 1] == color && !checked[y][x - 1]) queue.offer(new int[] {y, x - 1, picture[y][x - 1]});
				}
				maxSizeOfOneArea = Math.max(maxSizeOfOneArea, curAreaSize);
			}
		}
		return new int[] {numberOfArea, maxSizeOfOneArea};
	}
}
