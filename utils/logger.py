def normalize(xs):
    s = sum(xs) + 1e-9
    return [x / s for x in xs]