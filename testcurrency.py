""" 
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Sanam Maharjan
Date:   June 8th, 2025
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")

    # Test case 1: space in the middle
    result = currency.before_space("Sanam Maharjan")
    introcs.assert_equals("Sanam", result)

    # Test case 2: space at beginning
    result = currency.before_space(" Sanam")
    introcs.assert_equals("", result)

    # Test case 3: multiple space
    result = currency.before_space("My name is Sanam")
    introcs.assert_equals("My", result)

    #  Test case 4: with numeric
    result = currency.before_space("12345 6789")
    introcs.assert_equals("12345", result)

    #  Test case 5: space at end
    result = currency.before_space("Sanamcha ")
    introcs.assert_equals("Sanamcha", result)

    # Test case 6: special chareacters
    result = currency.before_space("!@#$ %^&*")
    introcs.assert_equals("!@#$", result)

    # Test case 7: empty space
    result = currency.before_space("  ")
    introcs.assert_equals("", result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    result = currency.after_space("Hello World")
    introcs.assert_equals("World", result)

    result = currency.after_space(" World")
    introcs.assert_equals("World", result)

    result = currency.after_space("Hello How are you?")
    introcs.assert_equals("How are you?", result)

    result = currency.after_space("World ")
    introcs.assert_equals("", result)

    result = currency.after_space("  ")
    introcs.assert_equals(" ", result)

    result = currency.after_space("!@#$ ^&*()")
    introcs.assert_equals("^&*()", result)

    result = currency.after_space("1234 56789")
    introcs.assert_equals("56789", result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    # a test with only a single pair of quotes
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)
    
    # a test with multiple pairs of quotes
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    # a test with nothing inside the double quotes
    result = currency.first_inside_quotes('""')
    introcs.assert_equals('', result)

    # test with no pairs 
    result = currency.first_inside_quotes('"A"')
    introcs.assert_equals('A', result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

	# Test with a nonempty value for "src" and spaces after the colon
    result = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

	# Test  with an empty value for "src" and no spaces after the colon
    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

	# Test with a nonempty value for "src" and no spaces after the colon
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)

	# Test  with an empty value for "src" and spaces after the colon
    result = currency.get_src('{"success":false,"src": "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

	# a test with a nonempty value for "dst" and spaces after the colon
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

	# a test with an empty value for "dst" and no spaces after the colon
    result = currency.get_dst('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

	# a test with a nonempty value for "dst" and no spaces after the colon
    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)

	# a test with an empty value for "dst" and spaces after the colon
    result = currency.get_dst('{"success":false,"src":"","dst": "","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")

	# a test with an error message and no spaces after the colon
    result = currency.has_error('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_true(result)

	# a test with no error message and spaces after the colon 
    result = currency.has_error('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

	# a test with no error message and no spaces after the colon 
    result = currency.has_error('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals(False, result)

	# a test with no error message and spaces after the colon 
    result = currency.has_error('{"success":false,"src":"","dst":"","error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")

	# a test with valid currencies and non-negative amount
    expected = '{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}'
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals(expected, result)

    # a test with an invalid src currency
    expected = '{"success": false, "src": "", "dst": "", "error": "The rate for currency AAA is not present."}'
    result = currency.service_response('AAA', 'USD', 1.0)
    introcs.assert_equals(expected, result)

    # a test with valid currencies and negative amount
    expected ='{"success": true, "src": "-10.0 United States Dollars", "dst": "-8.86407 Euros", "error": ""}'
    result = currency.service_response('USD','EUR',-10)
    introcs.assert_equals(expected, result)

    # a test with an invalid dst currency
    expected = '{"success": false, "src": "", "dst": "", "error": "The rate for currency AAA is not present."}'
    result = currency.service_response('USD','AAA',10 )
    introcs.assert_equals(expected, result)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")
	
    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    introcs.assert_equals(True, currency.iscurrency('eur'))
    introcs.assert_equals(False, currency.iscurrency('xxx'))
    introcs.assert_equals(False, currency.iscurrency('aaa'))
	
	
def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")

	# a test with a non-negative amount
    result = currency.exchange('USD', 'EUR', 2.5)
    introcs.assert_floats_equal(2.2160175, result)

    # a test with a negative amount
    result = currency.exchange('USD', 'USD', -2.5)
    introcs.assert_floats_equal(-2.500, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_dst()
test_get_src()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully")