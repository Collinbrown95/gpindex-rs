from typing import Self

import numpy as np
import xarray as xr
import pandas as pd


class AggregationStructure:

    _pias: pd.DataFrame
    levels: None

    @staticmethod
    def from_pandas(pias: pd.DataFrame) -> Self:
        obj = AggregationStructure()
        obj._pias = pias
        return obj
    
    def __init__(self):
        pass
    
    def __getitem__(self, key):
        return self._pias[key]
    
    def __getattr__(self, name):
        return getattr(self._pias, name)
    
    def __repr__(self):
        return self._pias.__repr__()
    
    def __len__(self):
        return len(self._pias)

    def expand(self) -> Self:
        classification = self._pias.astype(str)['classification']

        veclen = np.vectorize(len)

        classification_lengths = veclen(classification)
        maxlen_ix = np.argmax(classification_lengths)

        classifications = np.full(
            (classification_lengths.size, classification_lengths[maxlen_ix]),
            "",
            dtype=f"U{classification_lengths[maxlen_ix]}"
        )

        levels = []

        for i in range(0, classification_lengths[maxlen_ix], 1):
            classifications[:, i] = classification.str[0:i+1]
            levels.append(f"level{i+1}")
        
        new_pias = AggregationStructure()
        new_pias.levels = levels
        new_pias._pias = self._pias.copy()
        new_pias._pias.loc[:, levels] = classifications
        return new_pias
