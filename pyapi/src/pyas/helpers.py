import numpy as np
import pandas as pd

def price_relatives(price, period, product):
    structured = np.rec.fromarrays([product, period, price], names="product,period,price")

    df = pd.DataFrame(structured)

    df = df.sort_values(['product', 'period'])

    df['relative'] = df.groupby('product')['price'].pct_change(1) + 1

    df.loc[(df['period'] == df['period'].min()) & (~df['price'].isna()), 'relative'] = 1.0

    return df.sort_index()['relative']
