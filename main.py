import requests
import logging

logger = logging.getLogger(__name__)

SUCCESS_CODE = 200


"""
site structure

{
    baseUrl: "https://nmanu.dev",
    urls: ["projects", "about"],
}

should have some config of expected behaviour to check against.

Such behavior includes:
 - expected response code
 - authenticated ? with token and stuff?
 - headers??
 - request types accepted?

Should be able to parse page, save html state

For another project:
    - should be able to parse meta tags and see what competition is doing
"""


class Pingo:
    def __init__(self, sites, log_file="pingo.log"):
        self.sites = sites
        self.log_file = log_file

    def log_request(self, req, site, log_level=logging.INFO):
        logging.basicConfig(filename=self.log_file, level=log_level)
        if req.status_code is not SUCCESS_CODE:
            logger.error("ALERT: something went wrong!!", req.status_code)
        else:
            logger.info(f" {site}: ALL GOOD: everything seems operational")

    def ping(self):
        for site in self.sites:
            req = requests.get(site)
            print(req.text, req.headers)
            self.log_request(req, site)
