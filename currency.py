"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Sanam Maharjan
Date:   June 8, 2025
"""

import introcs

APIKEY = "IUJanYIQGeFwQDX0xuzcRRQiCsBDxHRTSvAeMbz3Rqge"
	

def before_space(s):
	"""
	Returns the substring of s up to, but not including, the first space.

	Example: before_space('Hello World') returns 'Hello'

	Parameter s: the string to slice
	Precondition: s is a string with at least one space in it
	"""
	# Assert that s is a string
	assert type(s) == str, "Input must be string"
	assert " " in s

	return s[:introcs.find_str(s, ' ')]


def after_space(s):
	"""
	Returns the substring of s after the first space

	Example: after_space('Hello World') returns 'World'

	Parameter s: the string to slice
	Precondition: s is a string with at least one space in it
	"""
	# Assert that s is a string
	assert type(s) == str, "Input must be string"
	assert " " in s
	
	return s[introcs.find_str(s,' ') + 1 :]

def first_inside_quotes(s):
	"""
	Returns the first substring of s between two (double) quote characters

	Note that the double quotes must be part of the string.  So "Hello World" is a 
	precondition violation, since there are no double quotes inside the string.

	Example: first_inside_quotes('A "B C" D') returns 'B C'
	Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
	picks the first such substring.

	Parameter s: a string to search
	Precondition: s is a string with at least two (double) quote characters inside
	"""
	assert type(s) == str, "Input must be string"
	assert introcs.count_str(s, '"') >= 2

	start = introcs.find_str(s,  '"')
	end = introcs.find_str(s, '"', start + 1)

	return s[start + 1: end ]


def get_src(json):
	"""
	Returns the src value in the response to a currency query.

	Given a JSON string provided by the web service, this function returns the string
	inside string quotes (") immediately following the substring '"src"'. For example,
	if the json is
		
		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
	On the other hand if the json is 
		
		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns the empty string.

	The web server does NOT specify the number of spaces after the colons. The JSON
		
		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
		
	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""
	# locate to position to 'src'
	key = introcs.find_str(json, '"src"')

	# find first key after 'src'
	first_key = introcs.find_str(json, '"', key + len('"src"'))

	# return 
	return first_inside_quotes(json[first_key:])


def get_dst(json):
	"""
	Returns the dst value in the response to a currency query.

	Given a JSON string provided by the web service, this function returns the string
	inside string quotes (") immediately following the substring '"dst"'. For example,
	if the json is
		
		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
	hand if the json is 
		
		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns the empty string.

	The web server does NOT specify the number of spaces after the colons. The JSON
		
		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
		
	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""

	# locate to position to 'dst'
	key = introcs.find_str(json,'"dst"')

	# find first key after 'dst'
	first_dst = introcs.find_str(json,'"', key + len('"dst"'))

	return first_inside_quotes(json[first_dst:])




def has_error(json):
	"""
	Returns True if the response to a currency query encountered an error.

	Given a JSON string provided by the web service, this function returns True if the
	query failed and there is an error message. For example, if the json is
		
		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns True (It does NOT return the error message 
	'Source currency code is invalid'). On the other hand if the json is 
		
		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns False.

	The web server does NOT specify the number of spaces after the colons. The JSON
		
		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
		
	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""

	# find the `"error"` key 
	key_error = introcs.find_str(json, '"error"')

	# find the first quote after 'error' key
	start_quote = introcs.find_str(json, '"', key_error + len('"error"'))

	# get the qouted substring and determine its non empty
	return first_inside_quotes(json[start_quote :]) !=''
	



def service_response(src, dst, amt):
	"""
	Returns a JSON string that is a response to a currency query.

	A currency query converts amt money in currency src to the currency dst. The response 
	should be a string of the form

		'{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'

	where the values src-amount and dst-amount contain the value and name for the src 
	and dst currencies, respectively. If the query is invalid, both src-amount and 
	dst-amount will be empty, and the error message will not be empty.

	There may or may not be spaces after the colon.  To test this function, you should
	choose specific examples from your web browser.

	Parameter src: the currency on hand
	Precondition: src is a nonempty string with only letters

	Parameter dst: the currency to convert to
	Precondition: dst is a nonempty string with only letters

	Parameter amt: amount of currency to convert
	Precondition: amt is a float or int

	"""

		# Enforce each parameter's precondition

	assert type(src) == str and src.isalpha(), "src must be non-empty letters"
	assert type(dst) == str and dst.isalpha(), "dst must be non-empty letters"
	assert type(amt) is int or type(amt) is float

	url = f"https://ecpyfac.ecornell.com/python/currency/fixed?src={src}&dst={dst}&amt={amt}&key={APIKEY}"

	resp = introcs.urlread(url)
	return resp


	    
def iscurrency(currency):
	"""
	Returns True if currency is a valid (3 letter code for a) currency.

	It returns False otherwise.

	Parameter currency: the currency code to verify
	Precondition: currency is a nonempty string with only letters
	"""

	assert type(currency) == str and currency != "" and currency.isalpha(), "currency must be a nonempty string with only letters"

	len(currency)== 3
	resp = service_response(currency, currency, 1.0)

	return '"success": true' in resp or '"valid": true' in resp
	



def exchange(src, dst, amt):
	"""
	Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency src to the currency 
	dst. The value returned represents the amount in currency currency_to.

	The value returned has type float.

	Parameter src: the currency on hand
	Precondition: src is a string for a valid currency code

	Parameter dst: the currency to convert to
	Precondition: dst is a string for a valid currency code

	Parameter amt: amount of currency to convert
	Precondition: amt is a float or int
	"""

	# 	# Enforce preconditions
	assert type(src) == str and src.isalpha(), "src must be a valid currency code"
	assert type(dst) == str and dst.isalpha(), "dst must be a valid currency code"
	assert type(amt) is int or type(amt) is float, "amt must be a float or int"

	# Get JSON response
	resp = service_response(src, dst, amt)

	# Extract destination amount
	dst_str = get_dst(resp)
	numeric_str = before_space(dst_str)

	return float(numeric_str)



