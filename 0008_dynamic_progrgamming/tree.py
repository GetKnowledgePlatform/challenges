from group import SocialGroup
from counter import Counter

counter = Counter()

def tree(candidates, remaining_budget):
    """
    :type candidates: list[SocialGroup]
    :return tuple
    """
    counter.count += 1

    if not candidates or remaining_budget == 0:
        return (0, tuple())

    candidate = candidates[0]

    if candidate.get_price() > remaining_budget:
        # Пропустили элемент, так как не хватает бюджета
        return tree(candidates[1:], remaining_budget)

    # Выбираем нашего кандидата
    clicks_with_candidate, groups_with_candidate =\
        tree(candidates[1:], remaining_budget-candidate.get_price())
    clicks_with_candidate += candidate.get_clicks()

    # Не выбираем нашего кандидата
    clicks_without_candidate, groups_without_candidate = \
        tree(candidates[1:], remaining_budget)

    if clicks_with_candidate < clicks_without_candidate:
        return (clicks_without_candidate, groups_without_candidate)
    else:
        return (clicks_with_candidate, groups_with_candidate+(candidate,))


