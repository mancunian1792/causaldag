import numpy as np
from typing import Union, List, Optional
from ._utils import combined_mat
from causaldag.utils.ci_tests import kci_test


def kci_invariance_test(
        samples1: np.ndarray,
        samples2: np.ndarray,
        i: int,
        cond_set: Optional[Union[List[int], int]]=None,
        width: float=0,
        alpha: float=0.05,
        unbiased: bool=False,
        regress: bool=True,
        gamma_approx: bool=True,
        n_draws: int=500,
        lam: float=1e-3,
        thresh: float=1e-5,
        num_eig: int=0,
):
    if isinstance(cond_set, int):
        cond_set = [cond_set]
    if cond_set is None:
        cond_set = []

    mat = combined_mat(samples1, samples2, i, cond_set)
    return kci_test(
        mat, 0, 1, list(range(2, 2+len(cond_set))),
        width=width,
        alpha=alpha,
        unbiased=unbiased,
        gamma_approx=gamma_approx,
        regress=regress,
        n_draws=n_draws,
        lam=lam,
        thresh=thresh,
        num_eig=num_eig,
    )
    # i_values = np.concatenate((samples1[:, i], samples2[:, i]))
    # labels = np.concatenate((np.zeros(samples1.shape[0]), np.ones(samples2.shape[0])))
    # if cond_set is None or len(cond_set) == 0:
    #     return ki_test_vector(
    #         i_values,
    #         labels,
    #         width_x=width,
    #         width_y=width,
    #         alpha=alpha,
    #         gamma_approx=gamma_approx,
    #         n_draws=n_draws,
    #         lam=lam,
    #         thresh=thresh,
    #         num_eig=num_eig,
    #         catgorical_x=True
    #     )
    # else:
    #     cond_set_values = np.concatenate((samples1[:, cond_set], samples2[:, cond_set]))
    #     return kci_test_vector(
    #         i_values,
    #         labels,
    #         cond_set_values,
    #         width=width,
    #         alpha=alpha,
    #         unbiased=unbiased,
    #         gamma_approx=gamma_approx,
    #         n_draws=n_draws,
    #         lam=lam,
    #         thresh=thresh,
    #         num_eig=num_eig,
    #         catgorical_e=True
    #     )
