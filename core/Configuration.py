class Config:
    # Hampel
    HAMPEL_WINDOW_SIZE = 3
    HAMPEL_GAUSSIAN_DISTR_SCALE_FACTOR = 1.4826
    HAMPEL_N_SIGMAS = 1

    # Butterworth low pass filter
    BUTTERWORTH_LOW_PASS_FILTER_ORDER = 2
    BUTTERWORTH_LOW_PASS_FILTER_FS = 100.0
    BUTTERWORTH_LOW_PASS_FILTER_CUTOFF = 15

    def get_hampel_and_butterworth_analysis_parameters():
        analysis_parameters_dict = {}

        # Hampel
        analysis_parameters_dict['hampel_window_size'] = \
            Config.HAMPEL_WINDOW_SIZE
        analysis_parameters_dict['hampel_gaussian_distr_scale_factor'] = \
            Config.HAMPEL_GAUSSIAN_DISTR_SCALE_FACTOR
        analysis_parameters_dict['hampel_n_sigmas'] = \
            Config.HAMPEL_N_SIGMAS

        # Butterworth low pass filter
        analysis_parameters_dict['butterworth_low_pass_filter_order'] = \
            Config.BUTTERWORTH_LOW_PASS_FILTER_ORDER
        analysis_parameters_dict['butterworth_low_pass_filter_fs'] = \
            Config.BUTTERWORTH_LOW_PASS_FILTER_FS
        analysis_parameters_dict['butterworth_low_pass_filter_cutoff'] = \
            Config.BUTTERWORTH_LOW_PASS_FILTER_CUTOFF

        return analysis_parameters_dict
