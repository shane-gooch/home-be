from base_selenium_class import GetWebElement
from decouple import config
import time


class GetVenmo(GetWebElement):

    def getTotal(self):
        super().start('https://venmo.com/account/sign-in/')
        super().get_element("name", "phoneEmailUsername").send_keys(config('VENMO_USER'))
        super().get_element("name", "password").send_keys(config('VENMO_PASSWORD'))
        super().get_element("class", "ladda-label").click()
        time.sleep(1.5)
        super().get_element(
            "xpath", '//*[@id="content"]/div/div/div/form/button').click()


one = GetVenmo()
one.getTotal()
