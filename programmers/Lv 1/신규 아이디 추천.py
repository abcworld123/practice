def solution(new_id):

    # 1
    new_id = new_id.lower()
    new_id = list(new_id)

    # 2
    trash = []
    for i in range(len(new_id)):
        if not new_id[i].isalnum() and not new_id[i] in ['-', '_', '.']: trash.append(i)
    for i in reversed(trash): new_id.pop(i)

    # 3
    trash = []
    for i in range(1, len(new_id)):
        if new_id[i - 1] == '.' and new_id[i] == '.': trash.append(i)
    for i in reversed(trash): new_id.pop(i)

    # 4
    trash = []
    for i in range(len(new_id)):
        if new_id[i] == '.': trash.append(i)
        else: break
    for i in reversed(trash): new_id.pop(i)

    # 5
    if not new_id: new_id = ['a']

    # 6
    if len(new_id) > 15: new_id = new_id[:15]
    trash = []
    for i in range(len(new_id) - 1, -1, -1):
        if new_id[i] == '.': trash.append(i)
        else: break
    for i in reversed(trash): new_id.pop(i)

    # 7
    if len(new_id) <= 2: new_id += new_id[-1] * (3 - len(new_id))

    return ''.join(new_id)
