from advertisingPlan import AdvertisingPlan, RemainingBudgetNotEnoughError


def greedy(groups, budget, key_function):

    sorted_groups = sorted(groups, key=key_function, reverse=True)
    plan = AdvertisingPlan(budget)

    for candidate in sorted_groups:
        try:
            plan.add_group(candidate)
        except RemainingBudgetNotEnoughError:
            continue

    return plan
