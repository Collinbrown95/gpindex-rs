from typing import Tuple

import numpy as np
import xarray as xr
import pandas as pd

from .means import generalized_mean

class PriceIndex:

    _index: xr.DataArray

    def __init__(self, elementals: xr.DataArray):
        self._index = elementals

    def __getitem__(self, key):
        return self._index.loc[key]
    
    def __getattr__(self, name):
        return getattr(self._index, name)
    
    def __repr__(self):
        return self._index.__repr__()
    
    def __len__(self):
        return len(self._index)


def elementary_index_from_pd(
        relatives: pd.Series,
        period: pd.Series,
        business: pd.Series,
        formula: float = 1,
        na_rm = False
) -> PriceIndex:
    # Logic to remove missing values
    if na_rm:
        MASK = ~np.isnan(relatives)
        relatives = relatives[MASK]
        period = period[MASK]
        business = business[MASK]
    
    # Get unique values for businesses and periods and indexes for each value
    u_p, p_idx = np.unique(period, return_inverse=True)
    u_b, b_idx = np.unique(business, return_inverse=True)
    u_p = u_p.astype(str)
    u_b = u_b.astype(str)

    # Make elementals grid
    elementals = np.full((len(u_p), len(u_b)), np.nan)

    # Calculate each elemental
    for (r_ix, c_ix), val in np.ndenumerate(elementals):
        elementals[r_ix, c_ix] = generalized_mean(relatives[(p_idx == c_ix) & (b_idx == r_ix)], order=formula)
    
    elementals = xr.DataArray(data=elementals, dims=['business', 'period'], coords={"business": u_b, "period": u_p})
    elementals.attrs['periods'] = u_p
    elementals.attrs['businesses'] = u_b

    return PriceIndex(elementals)
