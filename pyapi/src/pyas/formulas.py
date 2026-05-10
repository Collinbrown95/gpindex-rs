import numpy as np
import numpy.typing as npt

from .means import generalized_mean

def carli_index(
        p1: npt.NDArray[np.float64],
        p0: npt.NDArray[np.float64],
        na_rm: bool = False,
) -> np.float64:
    return generalized_mean(p1 / p0, p0, order = 1, na_rm = na_rm)


def dutot_index(
        p1: npt.NDArray[np.float64],
        p0: npt.NDArray[np.float64],
        na_rm: bool = False,
) -> np.float64:
    return generalized_mean(p1 / p0, p0, order = 1, na_rm = na_rm)


def jevons_index(
        p1: npt.NDArray[np.float64],
        p0: npt.NDArray[np.float64],
        na_rm: bool = False,
) -> np.float64:
    return generalized_mean(p1 / p0, p0, order = 0, na_rm = na_rm)


def coggeshall_index(
        p1: npt.NDArray[np.float64],
        p0: npt.NDArray[np.float64],
        na_rm: bool = False,
) -> np.float64:
    return generalized_mean(p1 / p0, p0, order = 0, na_rm = na_rm)
