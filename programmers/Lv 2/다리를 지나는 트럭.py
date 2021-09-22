def solution(bridge_length, weight, truck_weights):
    tick = 0
    bridge = [0] * bridge_length
    total_weight = 0
    while truck_weights:
        cur = tick % bridge_length
        total_weight -= bridge[cur]
        if truck_weights[0] + total_weight <= weight:
            bridge[cur] = truck_weights.pop(0)
            total_weight += bridge[cur]
        else: bridge[cur] = 0
        tick += 1
    return tick + bridge_length
