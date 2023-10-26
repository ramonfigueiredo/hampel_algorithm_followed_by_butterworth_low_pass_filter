## Hampel algorithm followed by Butterworth low pass filter using Python

### Hampel algorithm and Butterworth low pass filter
The Hampel algorithm is a method used for identifying and replacing outliers (anomalies) in a dataset. It is particularly useful for time series data or data that contains noise and occasional extreme values. The algorithm is based on the median absolute deviation (MAD) and involves the following steps:

- Calculate the median of the data.
- Calculate the MAD (median absolute deviation) of the data.
- Define a threshold value, typically a constant multiplier (e.g., 3 or 4) times the MAD.
- Identify data points that are further from the median than the threshold.
- Replace identified outliers with a central value, typically the median.

Here's a Python code snippet to perform the Hampel outlier detection:

```python
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
```

Now, for a Butterworth low-pass filter, it is used to attenuate high-frequency noise and retain the low-frequency components in a signal. You can use the scipy library in Python to apply a Butterworth low-pass filter. 

Here's a code snippet to do that:

```python
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
```

### To test the code

- Create and activate the virtual environment
```shell
virtualenv venv -p python3
source venv/bin/activate
pip install --upgrade pip
```

- Install the python requirements
```shell
pip install -r requirements.txt
```

- Run the code
```python
python main.py
```

### Example

- Noisy data

![Noisy data](https://github.com/ramonfigueiredo/hampel_algorithm_followed_by_butterworth_low_pass_filter/blob/main/images/noisy_data.png)

- Enhanced data: Hampel + Butterworth low pass filter

![Enhanced data: Hampel + Butterworth low pass filter](https://github.com/ramonfigueiredo/hampel_algorithm_followed_by_butterworth_low_pass_filter/blob/main/images/noisy_data.png)