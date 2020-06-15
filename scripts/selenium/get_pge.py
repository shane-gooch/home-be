from base_selenium_class import GetWebElement
from decouple import config


class GetPge(GetWebElement):

    def getTotal(self, numToSplitBy):
        super().start_headless('https://pge.com/')

        super().get_element("id", "username").send_keys(config('PGE_USER'))
        super().get_element("id", "password").send_keys(config('PGE_PASSWORD'))
        super().get_element("id", "home_login_submit").click()

        super().set_wait("id", "spntotalAmountDueUI")

        bill_total = super().get_element("id", "spntotalAmountDueUI").text
        super().quit()
        return round(float(bill_total[1:])/numToSplitBy, 2)


test = GetPge()
print(test.getTotal(4))
