Find the most profitable company from the financial sector. Output the result along with the continent.

https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=46647144#gid=46647144

import pandas as pd							
import numpy as np							
							
finance_sector = forbes_global_2010_2014[forbes_global_2010_2014['sector']== 'Financials']							
finance_sector['rank'] = finance_sector['profits'].rank(method='min', ascending=False)							
result = finance_sector[finance_sector['rank'] == 1][['company','continent']]							
