from advertisingPlan import AdvertisingPlan, RemainingBudgetNotEnoughError



def generate_all_subset(groups):

    if len(groups) == 0:
        return [[]]

    last_group = groups[-1]
    subset_without_last_item = generate_all_subset(groups[:-1])
    subset_with_last_item = []
    for element in subset_without_last_item:
        subset_with_last_item.append(element + [last_group])

    return subset_without_last_item + subset_with_last_item


def bruteforce(budget, groups):
    subset = generate_all_subset(groups)
    plans = []

    for sub_groups in subset:
        candidate = AdvertisingPlan(budget)
        is_break = False
        for group in sub_groups:
            try:
                candidate.add_group(group)
            except RemainingBudgetNotEnoughError:
                is_break = True
                break

        if not is_break:
            plans.append(candidate)

    if not plans:
        return None

    best_plan = plans[0]
    for plan in plans:
        if plan.get_total_clicks() > best_plan.get_total_clicks():
            best_plan = plan

    return best_plan




if __name__ == "__main__":
    print(generate_all_subset([1,2,3,4]))
    print(2**100/4_000_000_000/3600/24/365)