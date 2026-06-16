# scenario 1
import pandas as pd
data = [ [1,'IT',70000,6], [2,'HR',45000,4], [3,'IT',None,8], [4,'Finance',55000,3],[5,'HR',38000,6] ] 
df = pd.DataFrame(data,columns=['emp_id','department','salary','experience_years'])
# 1.Which department has the highest average salary?
# 2. Which employees earn more than the department average?
# 3. Count employees with more than 5 years of experience per department.
# 4. Which departments have minimum salary below 40,000?
# 5. Fill missing salary values using department median salary
# print(df)
# q1
# res=df.groupby('department')['salary'].transform('mean')
# dept_name=res.idxmax()
# avg_salary=res.max()
# print(dept_name,avg_salary)

# res = df.groupby('department')['salary'].mean()

# dept_name = res.idxmax()   # department name
# avg_salary = res.max()     # highest average salary

# print(dept_name, avg_salary)

# this when we use the transform it returns the index value only .
# with out transformation we get the dept_name  why ?

#  q2)Which employees earn more than the department average?
# df['dept_avg']=df.groupby('department')['salary'].transform('mean')
# df['more_than_dep_avg']=df['salary'] > df['dept_avg']
# print(df[df['more_than_dep_avg']])

# df['dept_avg'] = df.groupby('department')['salary'].transform('mean')
# print(df['dept_avg'])

#transfrom is used for the comprasion

# Count employees with more than 5 years of experience per department
# print(df)
# res=df['experience_years'] > 5;
# res1=df[res].groupby('department').size()
# print(res1)

# res=(df['experience_years']>5).sum()
# print(res)
#  Which departments have minimum salary below 40,000?q4
# res=df.groupby('department')['salary'].transform('min')
# result=res < 40000
# print(result)

# res=df.groupby('department')['salary'].min()
# result=res[res < 40000]
# print(result)

# q5)Fill missing salary values using department median salary
# res=df['salary'].fillna(df.groupby('department')['salary'].transform('median'))
# print(res)






