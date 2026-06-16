# secanrio 2
# Dataset Columns: order_id, customer_id, order_amount, order_date
# Questions:
# 1. Which day had the highest total order value?
# 2. Which customers placed more than 2 orders?
# 3. What is the monthly total revenue?
# 4. Fill missing order amounts using daily average.
# 5. Which orders were placed on weekends?
# Dataset Preparation Script:
# import pandas as pd 
# data = [ [101,1,2500,'2024-01-01'], [102,2,1800,'2024-01-02'],[103,1,None,'2024-01-02'], [104,3,3200,'2024-01-06'], [105,2,2100,'2024-01-07'] ] 
# df =pd.DataFrame(data, columns=['order_id','customer_id','order_amount','order_date']) 
# df['order_date']= pd.to_datetime(df['order_date'])
# print(df)

# res=df.sort_values(by='order_amount',ascending=False)
# print(res.head(1))
# res=df.groupby('order_date')['order_amount'].sum()
# res1=res.idxmax()
# print(res1)

# res=df.groupby(df['order_date'].dt.month)['order_amount'].sum()
# print(res)

#dt.month is used for the conversion of the days into months..
# res=df.groupby('customer_id').size()
# res1=res[res==2]
# print(res1)



# df['order_amount'] = df['order_amount'].fillna(
#     df.groupby('order_date')['order_amount'].transform('mean')
# )

# print(df)
