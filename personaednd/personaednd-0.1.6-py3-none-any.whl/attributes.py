from collections import OrderedDict
from random import choice, sample

import numpy

from personaednd.dice import Dice
from personaednd.listutils import add, merge, pick, purge
from personaednd.sources import (
    get_allotted_feats,
    Classes,
    Feats,
    Races,
    Skills,
    Tools,
    Weapons,
)


class ScoreAssigner:
    def __init__(self, _class: str, race: str, variant: bool) -> None:
        # Initial purged_values.
        raw_scores = list(self.roll_drop_lowest(60))
        primary_abilities = list()
        ability_scores = OrderedDict()
        ability_scores["Strength"] = None
        ability_scores["Dexterity"] = None
        ability_scores["Constitution"] = None
        ability_scores["Intelligence"] = None
        ability_scores["Wisdom"] = None
        ability_scores["Charisma"] = None
        # Assign primary abilities.
        primary_class_abilities = Classes.get_class_primary_abilities(_class)
        for rank, ability in primary_class_abilities.items():
            if isinstance(ability, list):
                ability = choice(ability)
            highest_score = max(raw_scores)
            raw_scores.remove(highest_score)
            modifier = get_ability_modifier(highest_score)
            ability_scores[ability] = {"Value": highest_score, "Modifier": modifier}
            primary_abilities.append(ability)
        # Assign secondary abilities.
        for ability, values in ability_scores.items():
            if values is None:
                chosen_score = choice(raw_scores)
                raw_scores.remove(chosen_score)
                modifier = get_ability_modifier(chosen_score)
                ability_scores[ability] = {"Value": chosen_score, "Modifier": modifier}
        # Apply racial bonus(es).
        bonuses = Races.get_racial_bonus(race, variant)
        for ability, bonus in bonuses.items():
            old_score = ability_scores[ability]["Value"]
            new_score = old_score + bonus
            if new_score > 20:
                new_score = 20
            modifier = get_ability_modifier(new_score)
            ability_scores[ability] = {"Value": new_score, "Modifier": modifier}
        self.abilities = ability_scores
        self.primaries = tuple(primary_abilities)

    @staticmethod
    def roll_drop_lowest(threshold: int) -> numpy.ndarray:
        """Returns six totaled results of 3(4) at threshold or higher."""
        die = Dice("d6", 4)
        results = numpy.array([], dtype=int)
        while results.sum() < threshold:
            for _ in range(1, 7):
                result = die.roll()
                excl_result = result.min(initial=None)
                ability_score = result.sum() - excl_result
                results = numpy.append(results, ability_score)
            score_total = results.sum()
            try:
                maximum_score = results.max(initial=None)
                minimum_score = results.min(initial=None)
            except ValueError:
                # Empty array FIX, force a re-roll.
                maximum_score = 14
                minimum_score = 7
            if score_total < threshold or maximum_score < 15 or minimum_score < 8:
                results = numpy.array([], dtype=int)
        return results


class ScoreImprovement:
    def __init__(
        self,
        _class: str,
        archetype: str,
        level: int,
        race: str,
        abilities: OrderedDict,
        primaries: tuple,
        armor_proficiency: list,
        tool_proficiency: list,
        weapon_proficiency: list,
        languages: list,
        skills: list,
        feats: list,
        variant: bool,
    ) -> None:
        # Character data
        self._class = _class
        self.archetype = archetype
        self.level = level
        self.race = race
        self.abilities = abilities
        self.primaries = primaries
        self.armors = armor_proficiency
        self.tools = tool_proficiency
        self.weapons = weapon_proficiency
        self.languages = languages
        self.skills = skills
        self.feats = feats
        self.variant = variant
        self.saves = Classes.get_saving_throws(self._class)
        # Humans w/ variant rule get a bonus feat.
        if race == "Human" and variant:
            self._upgrade_feats()

    def _assign_features(self, feat) -> None:
        """Assign associated features by specified feat."""
        # Actor
        if feat == "Actor":
            self._set_ability("Charisma", 1)
        # Athlete/Lightly Armored/Moderately Armored/Weapon Master
        if feat in (
            "Athlete",
            "Lightly Armored",
            "Moderately Armored",
            "Weapon Master",
        ):
            ability_choice = choice(["Strength", "Dexterity"])
            self._set_ability(ability_choice, 1)
            if feat == "Lightly Armored":
                add(self.armors, "Light")
            elif feat == "Moderately Armored":
                add(self.armors, "Medium")
                add(self.armors, "Shield")
        # Durable
        if feat == "Durable":
            self._set_ability("Constitution", 1)
        # Heavily Armored/Heavy Armor Master
        if feat in ("Heavily Armored", "Heavy Armor Master"):
            self._set_ability("Strength", 1)
            if feat == "Heavily Armored":
                add(self.armors, "Heavy")
        # Keen Mind/Linguist
        if feat in ("Keen Mind", "Linguist"):
            self._set_ability("Intelligence", 1)
            if feat == "Linguist":
                # Remove already known languages.
                linguist_languages = [
                    "Abyssal",
                    "Celestial",
                    "Common",
                    "Deep Speech",
                    "Draconic",
                    "Dwarvish",
                    "Elvish",
                    "Giant",
                    "Gnomish",
                    "Goblin",
                    "Halfling",
                    "Infernal",
                    "Orc",
                    "Primordial",
                    "Sylvan",
                    "Undercommon",
                ]
                purge(linguist_languages, self.languages)
                # Choose 3 bonus languages.
                merge(self.languages, sample(linguist_languages, 3))
        # Observant
        if feat == "Observant":
            if self._class in ("Cleric", "Druid"):
                self._set_ability("Wisdom", 1)
            elif self._class in ("Wizard",):
                self._set_ability("Intelligence", 1)
        # Resilient
        if feat == "Resilient":
            # Remove all proficient saving throws.
            resilient_saves = [
                "Strength",
                "Dexterity",
                "Constitution",
                "Intelligence",
                "Wisdom",
                "Charisma",
            ]
            purge(resilient_saves, self.saves)
            # Choose one non-proficient saving throw.
            ability_choice = choice(resilient_saves)
            self._set_ability(ability_choice, 1)
            add(self.saves, ability_choice)
        # Skilled
        if feat == "Skilled":
            for _ in range(3):
                skilled_choice = choice(["Skill", "Tool"])
                if skilled_choice == "Skill":
                    skills = purge(Skills.get_skills(), self.skills)
                    add(self.skills, choice(skills))
                elif skilled_choice == "Tool":
                    tools = purge(Tools.get_tools(None), self.tools)
                    add(self.tools, choice(tools))
        # Tavern Brawler
        if feat == "Tavern Brawler":
            self._set_ability(choice(["Strength", "Constitution"]), 1)
            add(self.weapons, "Improvised weapons")
            add(self.weapons, "Unarmed strikes")
        # Weapon Master
        if feat == "Weapon Master":
            weapons = Weapons.get_martial_weapons()
            if "Simple" not in self.weapons:
                merge(weapons, Weapons.get_simple_weapons())
            for weapon in self.weapons:
                if weapon in ("Simple", "Martial"):
                    continue
                if weapon in weapons:
                    weapons.remove(weapon)
            bonus_weapons = sample(weapons, 4)
            for weapon in bonus_weapons:
                add(self.weapons, weapon)

    def _isadjustable(self, abilities: (list, set, str, tuple), bonus: int) -> bool:
        """Checks if abilities is lt or eq to 20 with bonus."""
        if isinstance(abilities, (list, set, tuple)):
            for ability in abilities:
                score = self.abilities[ability]["Value"] + bonus
                if score > 20:
                    return False
            return True
        elif isinstance(abilities, str):
            score = self.abilities[abilities]["Value"] + bonus
            return score <= 20 and True or False
        return True

    def _set_ability(self, ability_name: str, bonus: int) -> None:
        if self._isadjustable(ability_name, bonus):
            old = self.abilities[ability_name]["Value"]
            new = old + bonus
            self.abilities[ability_name]["Value"] = new
            self.abilities[ability_name]["Modifier"] = get_ability_modifier(new)

    def _upgrade_ability(self) -> None:
        """Assigns ability upgrade or adds a feat (if not applicable)."""
        bonus = choice([1, 2])
        try:
            if bonus is 2:
                if self._isadjustable(self.primaries, bonus):
                    for ability in self.primaries:
                        if self._isadjustable(ability, bonus):
                            self._set_ability(ability, bonus)
                            break
                else:
                    raise ValueError
            elif bonus is 1:
                if all(
                    self._isadjustable(ability, bonus) is True
                    for ability in self.primaries
                ):
                    for ability in self.primaries:
                        self._set_ability(ability, bonus)
                else:
                    raise ValueError
        except ValueError:
            self._upgrade_feats()

    def _upgrade_feats(self) -> None:
        """Assigns a random valid feat."""
        feats = purge(Feats.get_feats(), self.feats)
        feat = pick(feats)
        has_required = False
        while True:
            if has_required:
                break
            while True:
                if Feats.has_requirements(
                    feat=feat,
                    _class=self._class,
                    archetype=self.archetype,
                    level=self.level,
                    abilities=self.abilities,
                    armor_proficiency=self.armors,
                    weapon_proficiency=self.weapons,
                ):
                    has_required = True
                    self.feats.append(feat)
                else:
                    feat = pick(feats)
                break
        self.feats.sort()
        self._assign_features(feat)

    def assign_upgrades(self):
        num_of_feats = get_allotted_feats(self._class, self.level)
        if num_of_feats > 0:
            for upgrade in range(num_of_feats):
                upgrade_selection = choice(("Ability", "Feat"))
                if upgrade_selection == "Ability":
                    self._upgrade_ability()
                elif upgrade_selection == "Feat":
                    self._upgrade_feats()


def get_ability_modifier(score) -> int:
    """Returns ability modifier by score."""
    return score is not 0 and int((score - 10) / 2) or 0
