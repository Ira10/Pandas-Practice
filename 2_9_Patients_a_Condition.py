Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.									
Return the result table in any order.									


	import pandas as pd						
							
	def find_patients(patients: pd.DataFrame) -> pd.DataFrame:						
	new = patients[patients['conditions'].str.contains(r'\bDIAB1')]						
	return new						


							
1.	new = patients['conditions'].str.contains('DIAB1').reset_index() ---> This is will just check if it is true or false						
2.	if we coverup with  'patients[]'  then we will get the dataframe back based on the true and false.						
							
3.	The \b in the pattern is a word boundary assertion that ensures 'DIAB1' is a separate word and not part of another word.						
							
