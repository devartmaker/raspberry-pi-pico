def map(x, in_min, in_max, out_min, out_max):
    result = round((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min
    if result > out_max:
        result = out_max
    elif result < out_min:
        result = out_min
    return result
