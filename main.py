import time

import matplotlib.pyplot as plt
import numpy as np

from core.signal_processing.signal_processing_utils import get_enhanced_data_list

if __name__ == '__main__':
    start_time = time.time()

    data_list = np.random.normal(0, 1, 100)
    print('\nNoisy data: {}'.format(data_list))

    # Plot noise data list
    plt.plot(data_list)
    plt.title('Noisy data')
    plt.show()

    enhanced_data_list = get_enhanced_data_list(data_list)
    print('\nEnhanced data: {}'.format(data_list))

    # Plot enhanced data list
    plt.plot(enhanced_data_list)
    plt.title('Enhanced data: Hampel + Butterworth low pass filter')
    plt.show()

    print('\n\nDone! It took {:.2f} seconds'.format(time.time() - start_time))
