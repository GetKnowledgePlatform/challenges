import time

import tree
import fast_tree
from group import SocialGroup


def build_n_groups(n):
    result = []
    for i in range(n):
        result.append(SocialGroup.generate_random_group())
    return result


def test_tree():
    for n in range(15, 100):

        start = time.time()
        groups = build_n_groups(n)
        tree.counter.clear()
        best_plan = tree.tree(groups, 20_000)
        end = time.time()

        print("******************")
        print("N:",n)
        print("Groups", groups)
        print("Best plan clicks: ", best_plan)
        print("Num of calls: ", tree.counter.count)
        print("Time: ", end-start)
        print("******************\n")


def test_fast_tree():
    for n in range(15, 100):

        start = time.time()
        groups = build_n_groups(n)
        fast_tree.counter.clear()
        best_plan = fast_tree.fast_tree(groups, 20_000)
        end = time.time()

        print("******************")
        print("N:",n)
        print("Groups", groups)
        print("Best plan clicks: ", best_plan)
        print("Num of calls:", fast_tree.counter.count)
        print("Num of hit cache:", fast_tree.counter.cache)
        print("Time: ", end-start)
        print("******************\n")


def test_identity():
    for n in range(5, 20):

        start = time.time()
        groups = build_n_groups(n)
        best_plan_1 = tree.tree(groups, 20_000)
        best_plan_2 = fast_tree.fast_tree(groups, 20_000)
        end = time.time()

        print("******************")
        print("N:",n)
        print("Groups", groups)
        print("Best plan clicks1: ", best_plan_1)
        print("Best plan clicks2: ", best_plan_2)
        print("Time: ", end-start)
        print("******************\n")


# test_tree()

test_fast_tree()

# test_identity()