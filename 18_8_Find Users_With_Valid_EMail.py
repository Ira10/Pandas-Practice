"Write a solution to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where:

The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
Return the result table in any order."



import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
pattern = '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'
users['mail_check'] = users['mail'].apply(lambda x: bool(re.match(pattern, x)))
return users[users['mail_check']==True][['user_id','name','mail']]



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=110663918#gid=110663918
