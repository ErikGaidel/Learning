def max_val(ist):
    m = ist[0]
    for i in ist:
        if i > m:
            m = i
            continue
    return m


def min_val(_list):
    m = _list[0]
    for i in _list:
        if i < m:
            m = i
            continue
    return m


def sum_val(l):
    s = 0
    for i in l:
        s += i
    return s
