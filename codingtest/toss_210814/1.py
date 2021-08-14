import math

def solution(orderAmount, taxFreeAmount, serviceFee):
    if orderAmount - taxFreeAmount == 1: return 0
    return orderAmount - math.floor((taxFreeAmount + 10 * (orderAmount) / 11))

# 틀림
