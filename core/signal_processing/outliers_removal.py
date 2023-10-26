import numpy as np


def hampel_filter_forloop(input_series, window_size, k, n_sigmas=3):
    n = len(input_series)
    new_series = input_series.copy()

    indices = []

    for i in range((window_size), (n - window_size)):
        x0 = np.median(input_series[(i - window_size):(i + window_size)])
        S0 = k * np.median(np.abs(input_series[(i - window_size):(i + window_size)] - x0))

        if (np.abs(input_series[i] - x0) > n_sigmas * S0):
            new_series[i] = round(x0, 2)
            indices.append(i)

    return new_series, indices
