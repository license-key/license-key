## License Checker for Python project
This module provides you with a wide functionality for checking license keys and their expiration dates for your program written in Python

### Installing via PyPi

    pip install license-key
### JSON format
Need host JSON file to your site or on GitHub Gists with all licenses data with format:

    {
	    "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX": {
		    "id": "1",
			"expire": "30.12.2022"
        },
        "EXAMPLE_KEY": {
	        "id": "ID ON STRING OR INT",
	        "expire": "DD.MM.YYYY"
	    }
    }
### Using in code

    >>> import license_key
    >>> url = "https://gist.github.com/marat2509/db7026b9dd10cbdbe63052c5d674804e/raw/licenses.json"
    >>> license = init(license_json_url = url)
    >>> print(license.check(license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX"))
    <<< 1  # License key valid
	>>> print(license.check(license_key = "EXPIRED_KEY"))
	<<< -1  # License key expired
	>>> print(check_license(license_url_list = url, license_key = "UNKNOWN_KEY"))
	<<< 0  # License key not registered
    >>> print(license.get(license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX", key = "expire"))
    <<< 30.12.2022
    >>> print(license.get(license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX", key = "THIS_KEY_DOESNT_EXISTS"))
    <<< 404  # Key not found
### Status codes
| Code | Description           |
|------|-----------------------|
| -406 | Failed to fetch       |
| 404  | Key not found         |
| -1   | License key expired   |
| 0    | License key not found |
| 1    | License key valid     |
### Debug mode
Code:

    import license_key
    url = "https://gist.github.com/marat2509/db7026b9dd10cbdbe63052c5d674804e/raw/licenses.json"
    license = license_key.init(license_json_url = url, debug = True)
    print(license.check(license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX"))
Output:

    2022-06-17 23:34:20.553 | DEBUG    | license_key:__init__:10 - Initiated self-based class; Version: 1.0.0
    2022-06-17 23:34:20.873 | INFO     | license_key:get_data:17 - Fetched JSON data, saved to dict 'self.data'
    2022-06-17 23:34:20.877 | DEBUG    | license_key:check:24 - Getting current date from TimeApi
    2022-06-17 23:34:21.157 | INFO     | license_key:check:28 - Fetched JSON data, saved dict to 'self.today'
    2022-06-17 23:34:21.169 | DEBUG    | license_key:check:32 - Setting 'self.to_day' from dict 'self.today'
    2022-06-17 23:34:21.171 | INFO     | license_key:check:34 - Setted 'self.to_day' to: 17
    2022-06-17 23:34:21.201 | DEBUG    | license_key:check:35 - Setting 'self.to_month' from dict 'self.today'
    2022-06-17 23:34:21.203 | INFO     | license_key:check:37 - Setted 'self.to_month' to: 6
    2022-06-17 23:34:21.205 | DEBUG    | license_key:check:38 - Setting 'self.to_year' from dict 'self.today'
    2022-06-17 23:34:21.212 | INFO     | license_key:check:40 - Setted 'self.to_year' to: 2022
    2022-06-17 23:34:21.228 | DEBUG    | license_key:check:41 - Checking license key in license list
    2022-06-17 23:34:21.231 | INFO     | license_key:check:45 - License key in a license list, license info:
    {
    "id": 1,
    "expire": "30.12.2022"
    }
    2022-06-17 23:34:21.234 | DEBUG    | license_key:check:46 - Checking whether the license key expired
    2022-06-17 23:34:21.236 | INFO     | license_key:check:55 - License key valid! The license key valid until: 30.12.2022
    1