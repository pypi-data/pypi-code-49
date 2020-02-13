from functools import lru_cache

import textworld
from textworld.logic import State, Rule, Proposition, Variable


@lru_cache()
def _rules_predicates_scope():
    rules = [
        Rule.parse("query :: at(P, r) -> at(P, r)"),
        Rule.parse("query :: at(P, r) & at(o, r) -> at(o, r)"),
        Rule.parse("query :: at(P, r) & at(d, r) -> at(d, r)"),
        Rule.parse("query :: at(P, r) & at(s, r) -> at(s, r)"),
        Rule.parse("query :: at(P, r) & at(c, r) -> at(c, r)"),
        Rule.parse("query :: at(P, r) & at(s, r) & on(o, s) -> on(o, s)"),
        Rule.parse("query :: at(P, r) & at(c, r) & open(c) -> open(c)"),
        Rule.parse("query :: at(P, r) & at(c, r) & closed(c) -> closed(c)"),
        Rule.parse("query :: at(P, r) & at(c, r) & open(c) & in(o, c) -> in(o, c)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') -> at(d, r)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & open(d) -> open(d)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & closed(d) -> closed(d)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & north_of(r', r) -> north_of(d, r)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & south_of(r', r) -> south_of(d, r)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & west_of(r', r) -> west_of(d, r)"),
        Rule.parse("query :: at(P, r) & link(r, d, r') & east_of(r', r) -> east_of(d, r)"),
    ]
    rules += [Rule.parse("query :: at(P, r) & at(f, r) & {fact}(f) -> {fact}(f)".format(fact=fact)) for fact in FOOD_FACTS]
    rules += [Rule.parse("query :: at(P, r) & at(s, r) & on(f, s) & {fact}(f) -> {fact}(f)".format(fact=fact)) for fact in FOOD_FACTS]
    rules += [Rule.parse("query :: at(P, r) & at(c, r) & open(c) & in(f, c) & {fact}(f) -> {fact}(f)".format(fact=fact)) for fact in FOOD_FACTS]
    return rules


@lru_cache()
def _rules_predicates_recipe():
    rules = [
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) -> part_of(f, RECIPE)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & roasted(ingredient) -> to_roast(f)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & grilled(ingredient) -> to_grill(f)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & fried(ingredient) -> to_fry(f)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & sliced(ingredient) -> to_slice(f)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & chopped(ingredient) -> to_chop(f)"),
        Rule.parse("query :: in(ingredient, RECIPE) & base(f, ingredient) & diced(ingredient) -> to_dice(f)"),
    ]
    return rules


@lru_cache()
def _rules_exits():
    rules = [
        Rule.parse("query :: at(P, r) & north_of(r', r) -> north(r)"),
        Rule.parse("query :: at(P, r) & west_of(r', r) -> west(r)"),
        Rule.parse("query :: at(P, r) & south_of(r', r) -> south(r)"),
        Rule.parse("query :: at(P, r) & east_of(r', r) -> east(r)"),
    ]
    return rules


@lru_cache()
def _rules_predicates_inv():
    rules = [
        Rule.parse("query :: in(o, I) -> in(o, I)"),
    ]
    rules += [Rule.parse("query :: in(f, I) & {fact}(f) -> {fact}(f)".format(fact=fact)) for fact in FOOD_FACTS]
    return rules


def find_predicates_in_scope(state):
    actions = state.all_applicable_actions(_rules_predicates_scope())
    return [action.postconditions[0] for action in actions]


def find_exits_in_scope(state):
    actions = state.all_applicable_actions(_rules_exits())
    def _convert_to_exit_fact(proposition):
        return Proposition("has_exit", [proposition.arguments[0],
                                        Variable(proposition.name, "exit")])

    return [_convert_to_exit_fact(action.postconditions[0]) for action in actions]


def find_predicates_in_inventory(state):
    actions = state.all_applicable_actions(_rules_predicates_inv())
    return [action.postconditions[0] for action in actions]


def find_predicates_in_recipe(state):
    actions = state.all_applicable_actions(_rules_predicates_recipe())
    return [action.postconditions[0] for action in actions]


def process_facts(prev_facts, info_game, info_facts, info_last_action, cmd):
    kb = textworld.Game.deserialize(info_game).kb
    if prev_facts is None:
        facts = set()
    else:
        if cmd == "inventory":  # Bypassing TextWorld's action detection.
            facts = set(find_predicates_in_inventory(State(kb.logic, info_facts)))
            return prev_facts | facts

        elif info_last_action is None:
            return prev_facts  # Invalid action, nothing has changed.

        elif info_last_action.name == "examine" and "cookbook" in [v.name for v in info_last_action.variables]:
            facts = set(find_predicates_in_recipe(State(kb.logic, info_facts)))
            return prev_facts | facts

        state = State(kb.logic, prev_facts | set(info_last_action.preconditions))
        success = state.apply(info_last_action)
        assert success
        facts = set(state.facts)

    # Always add facts in sight.
    facts |= set(find_predicates_in_scope(State(kb.logic, info_facts)))
    facts |= set(find_exits_in_scope(State(kb.logic, info_facts)))

    return facts
