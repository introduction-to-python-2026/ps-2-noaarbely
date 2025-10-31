def find_mean_std (x1, x2, x3):
    mean = (x1 + x2 +x3) / 3
    variance_std= (((x1-mean)**2 + (x2-mean)**2 + (x3-mean)**2) / 3)**0.5
    return mean, variance_std
