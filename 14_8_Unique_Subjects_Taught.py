Write a solution to calculate the number of unique subjects each teacher teaches in the university. Return the result table in any order.									


import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
        return teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1912571693#gid=1912571693
