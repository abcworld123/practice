def solution(phone_book):
    phone_book.sort(key=lambda x: len(x), reverse=True)
    table = {}
    for phone in phone_book:
        cur = table
        for i in range(len(phone)):
            if phone[i] in cur:
                if i == len(phone) - 1: return False
            else: cur[phone[i]] = {}
            cur = cur[phone[i]]
    return True
