https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=126870973#gid=126870973



Write a solution to find all the classes that have at least five students. Return the result table in any order.							



import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
new = courses.groupby('class')['student'].count().reset_index(name='appeared')
return new[new['appeared'] >= 5][['class']]


