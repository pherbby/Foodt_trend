#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the CSV file
df = pd.read_csv('C:\\Users\\USER\\Downloads\\Africa Food Production (2004 - 2013).csv')

# Display the table
print(df)


# In[2]:


import pandas as pd
import pip

# Install pint library if not already installed
pip.main(['install', 'pint'])

import pint

# Read the CSV file
df = pd.read_csv('C:\\Users\\USER\\Downloads\\Africa Food Production (2004 - 2013).csv')

# Convert dates to datetime objects
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Add units to the values
df['Value'] = df['Value'].astype(str) + ' kt'  # 'kt' represents kilotons

# Create a Unit Registry
ureg = pint.UnitRegistry()

# Convert the 'Value' column to quantities
df['Value'] = df['Value'].apply(lambda x: ureg.Quantity(x))

# Display the modified dataframe
print(df)


# In[3]:


import pandas as pd

# Path to the CSV file
csv_file = 'C:\\Users\\USER\\Downloads\\Africa Food Production (2004 - 2013).csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Group the data by country, year, and item
grouped_df = df.groupby(['Country', 'Year', 'Item'])

# Iterate over the groups and perform operations
for group, data in grouped_df:
    country, year, item = group
    # Perform desired operations on the data
    # Example: calculate the sum of values for each group
    total_value = data['Value'].sum()
    print(f"Country: {country}, Year: {year}, Item: {item}")
    print(f"Total Value: {total_value}\n")


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
csv_file = 'C:\\Users\\USER\\Downloads\\Africa Food Production (2004 - 2013).csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Filter the data for African countries
african_countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
                     'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
                     'Congo, Dem. Rep.', 'Congo, Rep.', "Cote d'Ivoire", 'Djibouti', 'Egypt',
                     'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia',
                     'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
                     'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco',
                     'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe',
                     'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa',
                     'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

african_data = df[df['Country'].isin(african_countries)]

# Group the data by year and calculate the average value for each year
yearly_average = african_data.groupby('Year')['Value'].mean()

# Plot the trend using a line plot
plt.plot(yearly_average.index, yearly_average.values)
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.title('Trend of Average Value for African Countries')
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
csv_file = 'C:\\Users\\USER\\Downloads\\Africa Food Production (2004 - 2013).csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Box plot of the 'Value' column
plt.figure(figsize=(10, 6))  # Optional: Set the size of the plot
plt.boxplot(df['Value'])
plt.xlabel('Value')
plt.ylabel('Production')
plt.title('Box Plot of Production')
plt.show()

