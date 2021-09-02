import java.util.LinkedList;

class Solution {
	LinkedList<String> list = new LinkedList<>();

	void permute(String s, String answer) {
		if (s.length() == 0) {
			list.add(answer);
			return;
		}
		for (int i = 0; i < s.length(); i++) {
			this.permute(s.substring(0, i) + s.substring(i + 1), answer + s.charAt(i));
		}
	}

	public int solution(int n, String[] data) {
		int answer = 0;
		int c1, c2, distance, expect;
		char op;
		boolean pass;

		permute("ACFJMNRT", "");

		for (String line : list) {
			pass = true;
			for (String cmd : data) {
				c1 = line.indexOf(cmd.charAt(0));
				c2 = line.indexOf(cmd.charAt(2));
				distance = Math.abs(c1 - c2) - 1;
				expect = cmd.charAt(4) - '0';
				op = cmd.charAt(3);
				if (!(op == '=' ? distance == expect : op == '>' ? distance > expect : distance < expect)) {
					pass = false;
					break;
				}
			}
			if (pass) answer++;
		}
		return answer;
	}
}
