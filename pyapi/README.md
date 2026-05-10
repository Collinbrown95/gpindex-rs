# Version 2 API Design

# UML Diagram

![Pyas 2.0 UML Diagram](./docs/api-v2.drawio.svg)

# Example Usage

This package would cover a few use cases.

## Collection of Price Index Tools

Working with data in another ecosystem (e.g., Pandas, Numpy), expose a collection of helpers for research/development purposes.

```python
# outliers.py
from pyas.outlier_detection import robust_z

OUTLIER_MASK = robust_z(df['relatives'])
df = df[OUTLIER_MASK]

# helpers.py
from pyas.helpers import price_relatives, offset_period
df['relatives'] = price_relatives(df['price'], df['period'], df['product'])
df['last_period'] = offset_period(df['period'], df['product'], match_first = False)

# means.py
from pyas.means import lehmer_mean
custom_mean_calc = lehmer_mean(df['relatives'], df['weights'], na_rm = True)

# formulas.py
from pyas.formulas import jevons_index
custom_index_calc = jevons_index(df['p1'], df['p0'], na_rm = True)
```

## Price Index Aggregation

Bring external data into the package's object model to perform various operations on `PriceIndex` and `AggregationStructure` objects.

```python
# price_index.py
from pyas import elementary_index_from_pd, PriceIndex
from pyas.formulas import fisher_index
index1: PriceIndex = elementary_index_from_pd(df['relatives'], df['period'], df['business'], formula=0)

# multilaterals.py
from pyas.multilaterals import geks
index2: PriceIndex = geks(df['price'], df['quantity'], df['period'], df['product'], window=13, formula=fisher_index)

# helpers.py
from pyas.helpers import splice_index
index2 = splice_index(index2)

# price_index.py and aggregation_structure.py
from pyas import PriceIndex, AggregationStructure

# Bring input data into the pyas object model.
merged_elementals = index1.merge(index2)
pias: AggregationStructure = AggregationStructure.from_pandas(pias_df)

# All methods can be chained (i.e., return self)
pias = pias.expand()
indexes = elementals.aggregate(pias)

# Expectation that users export data back into a known ecosystem like pandas for downstream work
outputs = indexes.to_pandas()
 
# Anything downstream of here happens in other well-known ecosystem tools like Pandas.
outputs.to_csv("index_outputs.csv")
```