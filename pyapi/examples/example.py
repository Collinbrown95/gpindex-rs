import pandas as pd

from pyas import elementary_index_from_pd, PriceIndex, AggregationStructure

from pyas.helpers import price_relatives

# Users set up input data using whatever tools they see fit.

df = pd.read_csv("./pyapi/data/ms_prices.csv")

pias_df = pd.read_csv("./pyapi/data/ms_weights.csv")

# Some helper utilities exposed to help with tricky operations.

df['relatives'] = price_relatives(df['price'], df['period'], df['product'])

# Bring input data into the pyas object model.

elementals: PriceIndex = elementary_index_from_pd(df['relatives'], df['period'], df['business'], formula=0)
pias: AggregationStructure = AggregationStructure.from_pandas(pias_df)

# All methods can be chained (i.e., return self)
pias = pias.expand()

elementals.aggregate(pias)

t=1
 