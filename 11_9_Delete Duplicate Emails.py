Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter



import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
person.sort_values(by='id', inplace=True)

person.drop_duplicates('email', keep='first', inplace=True)



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=491663247#gid=491663247
