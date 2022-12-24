
class SocialGroup:

    def __init__(self, name, clicks, price):
        self.__name = name
        self.__clicks = clicks
        self.__price = price

    def __str__(self):
        return self.__name + "<clicks:" + str(self.__clicks) + ",price:" + str(self.__price) + ">"

    def __repr__(self):
        return self.__str__()

    def get_clicks(self):
        return self.__clicks

    def get_price(self):
        return self.__price
