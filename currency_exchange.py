#import library
import requests
import pandas as pd

#URL for the United States Federal Reserve Currency Exchange Data
url = 'https://www.federalreserve.gov/datadownload/Output.aspx?rel=H10&series=60f32914ab61dfab590e0e470153e3ae&lastobs=10&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package'
#Files to write data 
filename = 'fed_exchange.csv'
test_file = 'fed_exchange2.csv'

#requests functions to gather data from the Federal Reserve
request = requests.get(url)
content = request.text

#Write requested data to csv file
with open(filename, 'w') as file:
	file.write(request.text)

#Use pandas to reduce data, only including the country, currency and value. 
rows_to_skip = list(range(2,6)) + list(range(8,30))
df = pd.read_csv(filename, skiprows = rows_to_skip)
df = df.transpose()
df = df.reset_index()
#Prints and writes the reformatted data so it can be checked.
#print(df)
#df.to_csv(test_file)
#first_row = df.loc[[1]]
#print(first_row)
#first_rate = df.iloc[1][1]
#print(first_rate)

currency = ''
amount = 0
#Range for rows 5-23
upper_rows = list(range(5,24))

print("\nThis program only converts to and from USD at the moment.")
#Input statements for type of currency, converting to or from USD and the amount to be converted.
for i in range(1,24):
	print(f"{i} {df.iloc[i]['index']}")
currency = input("\nPlease input the currency you are converting. (1-23) ")
to_or_from = input("\nWould you like to convert to USD or from USD? T/F ")
amount = (input("\nPlease input that amount you would like to exchange? "))

def convert_money():
	"""
	Converts currency to and from USD. 
	Only works with currencies on the federal reserve foreign exchange rates
	"""
	if int(currency) in [1,2,3,4] and to_or_from.lower() == 't':
		#AUD, EUR, NZD, GBP values are presented in USD for the federal reserve so there has to be a separate if statement for these currencies.
		new_currency = float(amount) * float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[int(currency)][0]}')
		return new_currency

	elif int(currency) in upper_rows and to_or_from.lower() == 't':
		#Converts currencies to USD
		new_currency = float(amount) / float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[1][0]}')
		return new_currency

	elif int(currency) in [1,2,3,4] and to_or_from.lower() == 'f':
		#AUD, EUR, NZD, GBP values are presented in USD for the federal reserve so there has to be a separate if statement for these currencies.
		new_currency = float(amount) / float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[int(currency)][0]}')
		return new_currency

	elif int(currency) in upper_rows and to_or_from.lower() == 'f':
		#Converts currencies to USD
		new_currency = float(amount) * float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[int(currency)][0]}')
		return new_currency


convert_money()