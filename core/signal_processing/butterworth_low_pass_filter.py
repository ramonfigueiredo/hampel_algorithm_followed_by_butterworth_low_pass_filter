import numpy as np
from scipy.signal import butter, filtfilt


def get_data_with_butterworth_low_pass_filter(data, order, fs, cutoff):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq

    b, a = butter(order, normal_cutoff)

    y_np = filtfilt(b, a, data)

    y_list = [round(y, 2) for y in y_np]
    y_np = np.array(y_list)

    return y_np
