#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

typedef struct {
	int f, s, cnt;
	ll sum;
} node;

node seg[1 << 21];
int lz[1 << 21];
int arr[1000001];

node find_fs(node* lc, node* rc) {
	if (lc->f == rc->f)
		return {lc->f, max(lc->s, rc->s), lc->cnt + rc->cnt, lc->sum + rc->sum};
	else {
		if (lc->f < rc->f) swap(lc, rc);
		return {lc->f, max(lc->s, rc->f), lc->cnt, lc->sum + rc->sum};
	}
}

node* init(int s, int e, int i) {
	if (s == e) seg[i] = { arr[s], 0, 1, arr[s] };
	else {
		int m = (s + e) >> 1, c = i << 1;
		node* lc = init(s, m, c);
		node* rc = init(m + 1, e, c + 1);
		seg[i] = find_fs(lc, rc);
	}
	return &seg[i];
}

void propagation(int i) {
	int c = i << 1;
	if (seg[c].f > lz[i]) {
		seg[c].sum -= 1ll * (seg[c].f - lz[i]) * seg[c].cnt;
		seg[c].f = lz[i];
		lz[c] = lz[i];
	}
	if (seg[c + 1].f > lz[i]) {
		seg[c + 1].sum -= 1ll * (seg[c + 1].f - lz[i]) * seg[c + 1].cnt;
		seg[c + 1].f = lz[i];
		lz[c + 1] = lz[i];
	}
	lz[i] = 0;
}

ll get_sum(int s, int e, int l, int r, int i) {
	if (lz[i] && s != e) propagation(i);
	if (l <= s && e <= r) return seg[i].sum;
	int m = (s + e) >> 1, c = i << 1;
	if (m < l) return get_sum(m + 1, e, l, r, c + 1);
	else if (m + 1 > r) return get_sum(s, m, l, r, c);
	else return get_sum(s, m, l, r, c) + get_sum(m + 1, e, l, r, c + 1);
}

int get_max(int s, int e, int l, int r, int i) {
	if (lz[i] && s != e) propagation(i);
	if (l <= s && e <= r) return seg[i].f;
	int m = (s + e) >> 1, c = i << 1;
	if (m < l) return get_max(m + 1, e, l, r, c + 1);
	else if (m + 1 > r) return get_max(s, m, l, r, c);
	else return max(get_max(s, m, l, r, c), get_max(m + 1, e, l, r, c + 1));
}

node* update(int s, int e, int l, int r, int i, int v) {

	if (s == e) {
		if (seg[i].f > v) {
			seg[i].sum -= 1ll * (seg[i].f - v) * seg[i].cnt;
			seg[i].f = v;
		}
	}
	else {
		if (lz[i]) propagation(i);
		int m = (s + e) >> 1, c = i << 1;
		if (l <= s && e <= r && seg[i].s < v) {
			seg[i].sum -= 1ll * (seg[i].f - v) * seg[i].cnt;
			seg[i].f = v;
			if (seg[c].f > v && (lz[c] == 0 || lz[c] > v)) {
				seg[c].sum -= 1ll * (seg[c].f - v) * seg[c].cnt;
				seg[c].f = v;
				lz[c] = v;
			}
			if (seg[c + 1].f > v && (lz[c + 1] == 0 || lz[c + 1] > v)) {
				seg[c + 1].sum -= 1ll * (seg[c + 1].f - v) * seg[c + 1].cnt;
				seg[c + 1].f = v;
				lz[c + 1] = v;
			}
		}
		else {
			node* nl = nullptr, * nr = nullptr;
			if (l <= m && seg[c].f > v)
				nl = update(s, m, l, r, c, v);
			if (m + 1 <= r && seg[c + 1].f > v)
				nr = update(m + 1, e, l, r, c + 1, v);
			if (nl && nr) seg[i] = find_fs(nl, nr);
			else if (nl) seg[i] = find_fs(nl, &seg[c + 1]);
			else if (nr) seg[i] = find_fs(&seg[c], nr);
		}
	}
	return &seg[i];
}


int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);

	int N, M, op, a, b, c;
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> arr[i];
	init(1, N, 1);

	cin >> M;
	while (M--) {
		cin >> op >> a >> b;
		if (op == 1) {
			cin >> c;
			if (seg[1].f > c) update(1, N, a, b, 1, c);
		}
		else if (op == 2) cout << get_max(1, N, a, b, 1) << '\n';
		else if (op == 3) cout << get_sum(1, N, a, b, 1) << '\n';
	}
}
