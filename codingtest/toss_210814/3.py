import re

def solution(amountText):
    if len(amountText) >= 2 and amountText[0] == '0': return False
    elif amountText.isdigit(): return True
    elif not re.fullmatch('[\d|,]+', amountText): return False
    else:
        arr = [len(x) for x in amountText.split(',')]
        if arr[0] == 0 or arr[0] > 3: return False
        elif any([x != 3 for x in arr[1:]]): return False
        else: return True
