import math

def winsorize(values, lower_pct, upper_pct):
    n = len(values)
    sorted_vals = sorted(values)

    def percentile(p):
        k = (n - 1) * p / 100
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return sorted_vals[int(k)]
        return sorted_vals[f] + (k - f) * (sorted_vals[c] - sorted_vals[f])

    lower = percentile(lower_pct)
    upper = percentile(upper_pct)

    result = []
    for v in values:
        if v < lower:
            result.append(float(lower))
        elif v > upper:
            result.append(float(upper))
        else:
            result.append(float(v))

    return result
