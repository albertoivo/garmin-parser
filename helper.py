

def get_sec(time_str):
    """Get Seconds from time."""
    if (len(time_str)) == 5:
        time_str = '00:' + time_str
    try:
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    except ValueError:
        m, s = time_str.split(':')
        return int(float(m)) * 60 + int(float(s))
