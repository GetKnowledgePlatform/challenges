from group import SocialGroup


class RemainingBudgetNotEnoughError(Exception):
    def __init__(self, remaining_budget, new_group):
        self.__remaining_budget = remaining_budget
        self.__new_group = new_group

    def __str__(self):
        return "Remaining budget<"+str(self.__remaining_budget)+"> is not enough for group: " + str(self.__new_group)


class AdvertisingPlan:
    def __init__(self, total_budget):
        self.__total_budget = total_budget
        self.__remaining_budget = total_budget
        self.__groups = []

    def add_group(self, new_group):
        """
        :type new_group: SocialGroup
        """
        if self.__remaining_budget - new_group.get_price() < 0:
            raise RemainingBudgetNotEnoughError(self.__remaining_budget, new_group)

        self.__groups.append(new_group)
        self.__remaining_budget -= new_group.get_price()

    def get_total_clicks(self):
        return sum([g.get_clicks() for g in self.__groups])

    def get_remains_budget(self):
        return self.__remaining_budget

    def __str__(self):
        return "Total clicks: " + str(self.get_total_clicks())
