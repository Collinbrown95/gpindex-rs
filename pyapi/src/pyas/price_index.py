from typing import Self

import numpy as np
import xarray as xr
import pandas as pd

from .means import generalized_mean
from .aggregation_structure import AggregationStructure

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
    
    def aggregate(self, pias: AggregationStructure, na_rm: bool = False) -> Self:
        # Temporary implementation just to figure out the ideal interfaces
        df = self._index.to_pandas()
        agg_levels = []
        for level in pias.levels:
            tmp = df.merge(
                pias[['business', level, 'weight']],
                how='left',
                left_on=df.index,
                right_on='business',
            )
            tmp = tmp[self._index.attrs['periods'].tolist() + [level] + ['weight']]
            tmp = tmp.groupby(level).apply(_get_weighted_average).reset_index().rename(columns={'business': 'levels'})
            agg_levels.append(tmp)
        agg_levels.append(
            self._index.to_pandas().reset_index()[['business'] + self._index.attrs['periods'].tolist()].rename(columns={'business': 'levels'})
        )
        index = pd.concat(agg_levels)
        # Fix levels column
        index['levels'] = index[['levels'] + pias.levels].bfill(axis=1).iloc[:, 0]
        index = index[['levels'] + self._index.periods.tolist()]
        new_idx = PriceIndex(index)
        return new_idx


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


def _get_weighted_average(group):
    cols = group.columns.difference(['weight'])
    weighted_values = group[cols].multiply(group['weight'], axis=0)

    valid_weights = group[cols].notnull().multiply(group['weight'], axis=0)

    return weighted_values.sum() / valid_weights.sum()
