https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=863601722#gid=863601722


Output ids of students with a median score from the writing SAT.	

	
	
import pandas as pd	
import numpy as np	
	
sat_scores['writing_percentile'] = sat_scores['sat_writing'].rank(axis = 0 , pct = True)	
sat_scores['writing_percentile'] = (sat_scores['writing_percentile']*100).apply(np.floor)	
result = sat_scores[sat_scores['writing_percentile'] == 50][['student_id']]	

	
	
# The line sat_scores['writing_percentile'] = sat_scores['sat_writing'].rank(axis = 0 , pct = True) is like figuring out where each student stands compared to their friends. It gives each student a rank based on their score.	
# The pct = True part means we're turning these ranks into percentages. So, if a student is better than half the class, they might get a 50%!	


