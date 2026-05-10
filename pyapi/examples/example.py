import pandas as pd

from pyas import elementary_index_from_pd, PriceIndex

from pyas.helpers import price_relatives

# Users set up input data using whatever tools they see fit.

df = pd.read_csv("./pyapi/data/ms_prices.csv")

pias = pd.read_csv("./pyapi/data/ms_weights.csv")

# Some helper utilities exposed to help with tricky operations.

df['relatives'] = price_relatives(df['price'], df['period'], df['product'])

# Bring input data into the pyas object model.

elementals = elementary_index_from_pd(df['relatives'], df['period'], df['business'], formula=0)

t=1
 