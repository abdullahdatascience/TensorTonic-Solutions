def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    n = len(values)
    sorted_vals = sorted(values)

    # Helper to compute median of a list
    def median(lst):
        m = len(lst)
        mid = m // 2
        if m % 2 == 1:
            return lst[mid]
        else:
            return (lst[mid - 1] + lst[mid]) / 2

    # Compute median
    med = median(sorted_vals)

    # Split into lower and upper halves
    if n % 2 == 1:
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2 + 1:]
    else:
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2:]

    # Compute Q1 and Q3
    q1 = median(lower_half) if lower_half else med
    q3 = median(upper_half) if upper_half else med

    iqr = q3 - q1

    # Scale values
    if iqr == 0:
        return [float(v - med) for v in values]
    else:
        return [float((v - med) / iqr) for v in values]
