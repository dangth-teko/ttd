"""
Trả về Te nếu x chia hết cho 3
Trả về Ko nếu x chia hết cho 5
Trả về Teko nếu x chia hết cho cả 3 và 5
"""


def ttd(x):
    if x % 5 == 0 and x % 3 == 0:
        return 'Teko'
    elif x % 5 == 0:
        return 'Ko'
    elif x % 3 == 0:
        return 'Te'
    return x
