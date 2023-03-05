from group import SocialGroup
from counter import Counter

counter = Counter()

def fast_tree(candidates, remaining_budget, cache={}):
    """
    :param cache:
    :param remaining_budget:
    :type candidates: list[SocialGroup]
    :return tuple
    """
    counter.count += 1

    key = (tuple(candidates), remaining_budget)
    if key in cache:
        counter.cache += 1
        return cache[key]

    if not candidates or remaining_budget == 0:
        return (0, tuple())

    candidate = candidates[0]

    if candidate.get_price() > remaining_budget:
        # Пропустили элемент, так как не хватает бюджета
        result = fast_tree(candidates[1:], remaining_budget, cache)
        cache[key] = result
        return result

    # Выбираем нашего кандидата
    clicks_with_candidate, groups_with_candidate =\
        fast_tree(candidates[1:], remaining_budget-candidate.get_price(), cache)
    clicks_with_candidate += candidate.get_clicks()

    # Не выбираем нашего кандидата
    clicks_without_candidate, groups_without_candidate = \
        fast_tree(candidates[1:], remaining_budget, cache)

    if clicks_with_candidate < clicks_without_candidate:
        result = (clicks_without_candidate, groups_without_candidate)
        cache[key] = result
        return result
    else:
        result = (clicks_with_candidate, groups_with_candidate+(candidate,))
        cache[key] = result
        return result