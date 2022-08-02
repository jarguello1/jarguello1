from tkinter import *
import requests
import pandas as pd

"""
Code pulls data from the federal reservee exchange chart 
and uses it to do rough currency conversions.
"""

#import library

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

#List for symbols of currencies that are presented in USD
extra_currencies = ['AUD', 'EUR', 'NZD', 'GBP']

#key down function
def click():
	selected_variable_1 = country_variable.get()
	selected_variable_2 = to_from_var.get()
	submitted_amount = text_entry.get()
	output.delete(0.0, END)
	result = convert_money(int(selected_variable_1[:2]), selected_variable_2, submitted_amount)
	if selected_variable_2 == "To USD":
		output.insert(END, f"{result:.2f} USD")
	else:
		output.insert(END, f"{result:.2f} {selected_variable_1[-3:]}")


#main
window = Tk()
window.title("Currency Exchanger")
window.configure(background="grey")

#Title
Label (window, text="Currency Exchanger", fg="white", font="none 12 bold", bg="grey"). grid(row=0, column=0, sticky=N)

#create label
Label (window, text="Which currency would you like to exchange?", bg="grey", fg="white", font="none 12 bold") .grid(row=1, column=0,sticky=N)

#create a dropdown menu for countries/currencies
#country list for drop down menu


country_variable = StringVar(window)
country_variable.set("01. AUSTRALIA AUD")

w = OptionMenu(window, country_variable,"01. AUSTRALIA AUD", "02. EUROPEAN UNION EUR", "03. NEW ZEALAND NZD", "04. UNITED KINGDOM GBP", "05. BRAZIL BRL", "06. CANADA CAD", "07. CHINA CNY", "08. DENMARK DKK", "09. HONG KONG HKD", "10. INDIA INR", "11. JAPAN JPY", "12. MALAYSIA MYR", "13. MEXICO MXN", "14. NORWAY NOK", "15. SOUTH AFRICA ZAR", "16. SINGAPORE SGD", "17. KOREA KRW", "18. SRI LANKA LKR", "19. SWEDEN SEK", "20. SWITZERLAND CHF", "21. TAIWAN TWD", "22. THAILAND THB", "23. VENEZUELA VEB") .grid(row=2,column=0,sticky=S)

#create a dropdown menu for exchange direction
to_from_var = StringVar(window)
to_from_var.set("To USD")

v = OptionMenu(window, to_from_var, "To USD", "From USD") .grid(row=3,column=0, sticky=S)

#add a run button
Button(window, text="Run", width=6, command=click) .grid(row=4, column=0, sticky=S)

#create a text entry box
Label (window, text="How much would you like to exchange?", fg="white", font="none 12 bold", bg="grey"). grid(row=5, column=0, sticky=N)

text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=6,column=0, sticky=S)

#create a text box
output = Text(window, width=45, height=6, wrap=WORD, background="white",font="arial",)
output.grid(row=7, column=0, columnspan=2,sticky=S)


#function to convert currency depending on options selected
def convert_money(currency, answer, amount):

	"""
	AUD, EUR, NZD, GBP values are presented in USD for the federal reserve so there has to be a separate if statement for these currencies.
	"""
	#Converts currencies to USD to respective currencies.

	if currency in [1,2,3,4] and answer == 'To USD':
		new_currency = float(amount) * float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[int(currency)][0]}')
		return new_currency

	elif currency > 4 and answer == 'To USD':
		new_currency = float(amount) / float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[1][0]}')
		return new_currency

	elif currency in [1,2,3,4] and answer == 'From USD':
		"""
		AUD, EUR, NZD, GBP values are presented in USD for the federal reserve so there has to be a separate if statement for these currencies.
		"""
		#Converts currencies to USD to respective currencies.
		new_currency = float(amount) / float(df.iloc[int(currency)][1])
		#Subtract 1 from the currency value to obtain the right currency marker from the extra_currencies list.
		print(f'{new_currency} {extra_currencies[int(currency)-1]}')
		return new_currency

	elif currency > 4 and answer == 'From USD':
		new_currency = float(amount) * float(df.iloc[int(currency)][1])
		print(f'{new_currency} {df.iloc[int(currency)][0]}')
		return new_currency


window.mainloop()
