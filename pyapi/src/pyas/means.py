from typing import Callable

import numpy.typing as npt
import numpy as np


def generalized_mean(
    x: npt.ArrayLike,
    weights: npt.ArrayLike = None,
    order: float = 1,
    na_rm: bool = False
) -> Callable:
    """
    Parameterizes a generalized mean function and returns
    the result of that function called on an array of floats.
    """
    if _not_finite_scalar(order):
        raise ValueError(f"Recieved invalid r value {order}.")
   
    def enclosed(x, w = None, na_rm = False):
        # Case: no weight vector
        if w is None:
            # Drop np.nan values if user requests it
            if na_rm and x.isna().any():
                x = x[~x.isna()]
            # 3 cases for r
            if order == 0:
                return np.exp(np.log(x).mean())
            elif order == 1:
                return x.sum() / x.size
            else:
                return ((x**order).sum() / x.size)^(1/r)
        # Case: weight vector is passed
        else:
            # if x/w don't have same dimension, value error
            if x.size != w.size:
                raise ValueError(f"`x` and `w` must be the same length.")
            # Handle dropping np.nan values
            if na_rm and (x.isna().any() or w.isna().any()):
                KEEP_MASK = ~(x.isna() | w.isna())
                x = x[KEEP_MASK]
                w = w[KEEP_MASK]
            # 3 cases for r
            if order == 0:
                return np.exp(np.sum(np.log(x) * w) / np.sum(w))
            elif order == 1:
                return np.sum(x * w) / np.sum(w)
            else:
                return (np.sum(x ** order * w) / np.sum(w))^(1/r)
    return enclosed(x, weights, na_rm)


def _not_finite_scalar(r: float) -> bool:
    if not float('nan'):
        return True
    return False
