import requests
import json
from loguru import logger

__version__ = "1.0.4"


class init:

    def __init__(self, license_json_url, debug = False):
        self.debug = debug
        if self.debug == True: logger.debug("""Initiated self-based class; Version: 1.1.0""")
        self.license_json_url = license_json_url
        self.get_data()
    
    def get_data(self):
        try:
            self.data = requests.get(self.license_json_url).json()
            if self.debug == True: logger.info("Fetched JSON data, saved to dict 'self.data'")
        except requests.exceptions.RequestException as error:
            if self.debug == True: logger.error("Failed to fetch JSON license list\nException: " + str(error))
            return(-406)

    def check(self, license_key):
        self.license_key = license_key
        if self.debug == True: logger.debug("Getting current date from TimeApi")
        try:
            self.today = requests.get(
                "https://timeapi.io/api/Time/current/coordinate").json()
            if self.debug == True: logger.info("Fetched JSON data, saved dict to 'self.today'")
        except requests.exceptions.RequestException as error:
            if self.debug == True: logger.error("Failed to fetch TimeAPI.io\nException: " + str(error))
            return(-406)
        if self.debug == True: logger.debug("Setting 'self.to_day' from dict 'self.today'")
        self.to_day = self.today["day"]
        if self.debug == True: logger.info("Setted 'self.to_day' to: " + str(self.to_day))
        if self.debug == True: logger.debug("Setting 'self.to_month' from dict 'self.today'")
        self.to_month = self.today["month"]
        if self.debug == True: logger.info("Setted 'self.to_month' to: " + str(self.to_month))
        if self.debug == True: logger.debug("Setting 'self.to_year' from dict 'self.today'")
        self.to_year = self.today["year"]
        if self.debug == True: logger.info("Setted 'self.to_year' to: " + str(self.to_year))
        if self.debug == True: logger.debug("Checking license key in license list")
        if self.license_key in self.data:  # check if license exists
            self.id = int(self.data[self.license_key]["id"])
            self.license_json = self.data[self.license_key]
            if self.debug == True: logger.info("License key in a license list, license info:\n" + str(json.dumps(self.license_json, indent = 2)))
            if self.debug == True: logger.debug("Checking whether the license key expired")
            self.expire = self.data[self.license_key]["expire"]
            self.exp_day = int(self.data[self.license_key]["expire"].split(".")[0])
            self.exp_month = int(self.data[self.license_key]["expire"].split(".")[1])
            self.exp_year = int(self.data[self.license_key]["expire"].split(".")[2])
            if self.exp_day <= self.to_day and self.exp_month <= self.to_month and self.exp_year <= self.to_year:
                if self.debug == True: logger.info("License key expired! The license key valid until: " + str(self.expire))
                return(-1)
            else:
                if self.debug == True: logger.info("License key valid! The license key valid until: " + str(self.expire))
                return(1)
        else:
            if self.debug == True: logger.info("Key not found in license list")
            return(0)

    def get(self, license_key, key):
        try:
            return(self.data[license_key][key])
        except KeyError:
            if self.debug == True: logger.error("Key " + key + "not found")
            return(-404)