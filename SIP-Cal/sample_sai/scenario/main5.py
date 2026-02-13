# Questions:
# 1. Which categories have total stock below 100?
# 2. Which products are priced above category average price?
# 3. Fill missing stock values using category median.
# 4. Identify duplicate product records.
# 5. What is the total inventory value per category?
# Dataset Preparation Script:
import pandas as pd
data = [ [101,'Electronics',50,15000], [102,'Electronics',None,12000],[103,'Furniture',30,8000], [104,'Furniture',70,9000], [104,'Furniture',70,9000] ] 
df =pd.DataFrame(data, columns=['product_id','category','stock','price'])
print(df)

# res=df.groupby('category')['stock'].sum()
# res1=res < 100;
# print(res[res1])


# res=df.groupby('category')['price'].transform('mean')
# res1=df['price'] > res;
# print(df[res1])

# print(df[df['price'] > df.groupby('category')['price'].transform('mean')])


res=df[df.duplicated(subset=['product_name'], keep=False)]
print(res)

