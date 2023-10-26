from core.Configuration import Config
from core.signal_processing.butterworth_low_pass_filter import get_data_with_butterworth_low_pass_filter
from core.signal_processing.outliers_removal import hampel_filter_forloop


def get_enhanced_data_list(data):
    hampel_and_butterworth_analysis_parameters_dict = Config.get_hampel_and_butterworth_analysis_parameters()

    print('\nHampel_and_butterworth_analysis_parameters_dict: {}'.format(hampel_and_butterworth_analysis_parameters_dict))

    # Hampel algorithm (outliers removal)
    data_without_outliers, detected_outliers_indices = hampel_filter_forloop(
        data,
        window_size=hampel_and_butterworth_analysis_parameters_dict['hampel_window_size'],
        k=hampel_and_butterworth_analysis_parameters_dict['hampel_gaussian_distr_scale_factor'],
        n_sigmas=hampel_and_butterworth_analysis_parameters_dict['hampel_n_sigmas']
    )

    # Butterworth low-pass filter
    data_without_outliers_filtered = get_data_with_butterworth_low_pass_filter(
        data_without_outliers,
        order=hampel_and_butterworth_analysis_parameters_dict['butterworth_low_pass_filter_order'],
        fs=hampel_and_butterworth_analysis_parameters_dict['butterworth_low_pass_filter_fs'],
        cutoff=hampel_and_butterworth_analysis_parameters_dict['butterworth_low_pass_filter_cutoff']
    )

    return data_without_outliers_filtered
