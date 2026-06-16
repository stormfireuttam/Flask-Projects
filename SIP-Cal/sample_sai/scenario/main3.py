# Scenario 3: Website Logs
# Dataset Columns: user_id, page, response_time, status_code
# Questions:
# 1. What is the average response time per page?
# 2. How many failed requests exist (status_code != 200)?
# 3. Which pages have response time above overall average?
# 4. Remove duplicate log entries.
# 5. Fill missing response times using median.
# Dataset Preparation Script:
import pandas as pd 
data = [ [1,'/home',120,200], [2,'/login',300,500], [1,'/home',None,200],[3,'/dashboard',250,200], [3,'/dashboard',250,200] ] 
df = pd.DataFrame(data,columns=['user_id','page','response_time','status_code'])
print(df)

res=df.groupby('page')['response_time'].mean()
print(res)
