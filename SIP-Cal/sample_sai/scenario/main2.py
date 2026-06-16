# secanrio 4
import pandas as pd 
data = [ [1,'Math',78], [1,'Science',None], [2,'Math',35], [2,'Science',55],
[3,'Math',90] ] 
df = pd.DataFrame(data, columns=['student_id','subject','marks'])


# 1What is the average marks per subject?
# 2. Which students scored below 40 in any subject?
# 3. Count number of subjects per student.
# 4. Fill missing marks using subject average.
# 5. Which subject has the highest variance in marks?
# res=df.groupby('subject')['marks'].transform('mean')
# print(res)

# res= df['marks'] < 40;
# print(res.idxmax())

# res=df.groupby('student_id')['marks'].apply(lambda x: (x < 40).any())
# print(res)

# res=df['marks'].fillna(df.groupby('student_id')['marks'].transform('mean'))
# print(res)

# res=df.groupby('student_id')['marks'].var().idxmax()
# print(res)
# print(df)


