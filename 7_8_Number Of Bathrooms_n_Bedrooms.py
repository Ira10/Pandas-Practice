Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.


# Import your libraries
import pandas as pd

# Start writing code
mean_values = airbnb_search_details.groupby(["city","property_type"])[['bedrooms','bathrooms']].mean().reset_index()

mean_values.rename(columns = {'bedrooms':"n_bedrooms_avg", "bathrooms":"n_bathrooms_avg"}, inplace=True)  ## this line returns nothing
mean_values



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=332893784#gid=332893784
