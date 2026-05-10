# Version 2 API Design

**Purpose**: The purpose of this folder is to iterate quickly and figure out the user-facing API using Python.

## UML Diagram

![Pyas 2.0 UML Diagram](./docs/api-v2.drawio.svg)

## Example Usage

```python
# --------------
# Pyas scope start
# --------------

# Some helper utilities exposed to help with tricky operations.
df['relatives'] = price_relatives(df['price'], df['period'], df['product'])

# Bring input data into the pyas object model.
elementals: PriceIndex = elementary_index_from_pd(df['relatives'], df['period'], df['business'], formula=0)
pias: AggregationStructure = AggregationStructure.from_pandas(pias_df)

# All methods can be chained (i.e., return self)
pias = pias.expand()
indexes = elementals.aggregate(pias)

# Expectation that users export data back into a known ecosystem like pandas for downstream work
outputs = indexes.to_pandas()
 
# --------------
# Pyas scope end
# --------------

# Anything downstream of here happens in other well-known ecosystem tools
outputs.to_csv("index_outputs.csv")
```