from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = [str1[i: i + 2] for i in range(len(str1) - 1) if str1[i: i + 2].isalpha()]
    arr2 = [str2[i: i + 2] for i in range(len(str2) - 1) if str2[i: i + 2].isalpha()]
    inter = len(list((Counter(arr1) & Counter(arr2)).elements()))
    union = len(list((Counter(arr1) | Counter(arr2)).elements()))
    return int(65536 * inter / union) if union else 0 if inter else 65536
