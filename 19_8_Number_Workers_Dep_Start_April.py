"Find the number of workers by department who joined in or after April. Output the department name along with the corresponding number of workers.

Sort records based on the number of workers in descending order."



# Import your libraries
import pandas as pd

# Start writing code
worker_april = worker[worker['joining_date']>= '2014-04-01 00:00:00']
worker_april.groupby('department')['worker_id'].count().reset_index(name='num_workers').sort_values(by='num_workers',ascending=False)
