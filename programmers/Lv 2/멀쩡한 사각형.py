import math
def solution(w, h): return w * h - (2 * max(w, h) -  math.gcd(w, h) - abs(w - h))
