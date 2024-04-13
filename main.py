import requests
import logging

logger = logging.getLogger(__name__)

SUCCESS_CODE = 200
#
# take a json
# {
#     url: "",
#     requests: [200, 301, 404, 500],
# }


class Pingo:
    def __init__(self, sites, log_file="pingo.log"):
        self.sites = sites
        self.log_file = log_file

    def log_request(self, req, site, log_level=logging.INFO):
        logging.basicConfig(filename=self.log_file, level=log_level)
        if req.status_code != SUCCESS_CODE:
            logger.error("ALERT: something went wrong!!", req.status_code)
        else:
            logger.info(f" {site}: ALL GOOD: everything seems operational")

    def ping(self):
        for site in self.sites:
            req = requests.get(site)
            self.log_request(req, site)


my_site = Pingo(["https://adios.dev", "https://claeusdev.github.io"])

my_site.ping()
