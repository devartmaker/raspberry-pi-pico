def proportion(x: int, in_min: int, in_max: int, out_min: int, out_max: int) -> int:
    result = round((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min
    if result > out_max:
        result = out_max
    elif result < out_min:
        result = out_min
    return result
