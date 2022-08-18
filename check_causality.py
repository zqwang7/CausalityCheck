import numpy as np


def check_causality(model, sr=16000, algo_lat=0.005):
    """
    :param model: your DNN model in Torch, Tensorflow, etc.
    :param sr: sampling rate in Hz
    :param algo_lat: allowed algorithmic latency in seconds

    The idea is that we set samples starting from a random position to NaN,
        and the DNN model peeks the NaNs would output NaNs.
    """ 

    algo_lat = int(algo_lat*sr)
    sig_len_range = [2., 8.] # range of signal length in seconds

    R = 100
    for r in range(R):
        l = np.random.uniform(low=sig_len_range[0], high=sig_len_range[1])
        l = int(l*sr)
        sig = np.random.randn(l)
        sig = sig / np.max(np.abs(sig)) * 0.9
        p = np.random.randint(len(sig))
        sig[p:] = np.nan

        est_sig = model(sig) # obtain separation results using your model

        if p-algo_lat+1 >= 1 and np.sum(np.isnan(est_sig[:p-algo_lat+1])) > 0:
            print('For example %d, your model does NOT satisfy the algorithmic latency requirement!'%r)
            return

    print('Your model satisfies the algorithmic latency requirement!')
