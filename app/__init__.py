def ttd(x):
    """
    Trả về Te nếu x chia hết cho 3
    Trả về Ko nếu x chia hết cho 5
    Trả về Teko nếu x chia hết cho cả 3 và 5
    Trả về x nếu x không phù hợp các điều kiện trên
    """
    if x % 5 == 0 and x % 3 == 0:
        return 'Teko'
    elif x % 5 == 0:
        return 'Ko'
    elif x % 3 == 0:
        return 'Te'
    return x


def create_app_setting(data):
    """
    đầu vào gồm key và value đều required
    key chỉ có thể bằng type1 hoặc type2
    với type1 thì value là str
    với type2 thì value là bool
    dữ liệu hợp lệ thì trả về chính nó
    """
    key = data.get('key')
    value = data.get('value')

    if key and value:
        if key not in ['type1', 'type2']:
            return 'Invalid Key'
        if key == 'type1' and isinstance(value, str) or key == 'type2' and isinstance(value, bool):
            return data
        return 'Invalid Value'

    return 'Required Fields'


def create_app_setting_1(data):
    if data.get('key') and data.get('value'):
        pass
    return 'Required Fields'


def create_app_setting_2(data):
    key = data.get('key')
    value = data.get('value')

    if key and value:
        if key not in ['type1', 'type2']:
            return 'Invalid Key'
    return 'Required Fields'


def create_app_setting_3(data):
    key = data.get('key')
    value = data.get('value')

    if key and value:
        if key not in ['type1', 'type2']:
            return 'Invalid Key'
        if key == 'type1' and isinstance(value, str) or key == 'type2' and isinstance(value, bool):
            pass
        return 'Invalid Value'
    return 'Required Fields'
