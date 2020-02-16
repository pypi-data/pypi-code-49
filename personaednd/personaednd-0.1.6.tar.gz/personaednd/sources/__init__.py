from collections import OrderedDict
from math import ceil
from random import choice, sample

from personaednd.listutils import merge, pick, purge
from personaednd.sources.reader import Reader


class Backgrounds(Reader):
    def __init__(self) -> None:
        super().__init__("backgrounds")

    @classmethod
    def get_backgrounds(cls) -> tuple:
        """Returns a tuple of available backgrounds."""
        return tuple(cls().find().keys())

    @classmethod
    def get_background_equipment(cls, background: str) -> list:
        """Returns a list of bonus equipment by background."""
        return cls().find([background, "equipment"])

    @classmethod
    def get_background_languages(cls, background: str) -> int:
        """Returns a count of bonus languages by background."""
        return cls().find([background, "languages"])

    @classmethod
    def get_background_skills(cls, background: str) -> list:
        """Returns a list of bonus skills by background."""
        return cls().find([background, "skills"])

    @classmethod
    def get_background_tools(cls, background: str) -> list:
        """Returns a list of bonus tool proficiencies by background."""
        background_tools = list()
        for tool in cls().find([background, "tool_proficiency"]):
            if Tools.has_sub_tools(tool):
                sub_tool = choice(Tools.get_sub_tools(tool))
                background_tools.append("{}: {}".format(tool, sub_tool))
            else:
                background_tools.append(tool)
        return background_tools


class Classes(Reader):
    def __init__(self) -> None:
        super().__init__("classes")

    @classmethod
    def get_archetypes(cls, _class: str) -> list:
        """Returns a list of archetypes by class."""
        return cls().find([_class, "archetypes"])

    @classmethod
    def get_class_armor_proficiency(cls, _class: str) -> list:
        """Returns a list of armor proficiencies by class."""
        return cls().find([_class, "armor_proficiency"])

    @classmethod
    def get_class_background(cls, _class: str) -> str:
        """Returns default class background by class."""
        return cls().find([_class, "background"])

    @classmethod
    def get_class_primary_abilities(cls, _class: str) -> dict:
        """Returns a dict of primary abilities by class."""
        return cls().find([_class, "primary_abilities"])

    @classmethod
    def get_class_tool_proficiency(cls, _class: str) -> list:
        """Returns a list of tool proficiencies by class."""
        if _class == "Monk":
            return [choice(Tools.get_tools(["Artisan's tools", "Musical instrument"]))]
        else:
            return cls().find([_class, "tool_proficiency"])

    @classmethod
    def get_class_weapon_proficiency(cls, _class: str) -> list:
        """Returns a list of weapon proficiencies by class."""
        return cls().find([_class, "weapon_proficiency"])

    @classmethod
    def get_classes(cls) -> tuple:
        """Returns a tuple of available classes."""
        return tuple(cls().find().keys())

    @classmethod
    def get_hit_die(cls, _class: str) -> int:
        """Returns a hit die integer value by class."""
        return cls().find([_class, "hit_die"])

    @classmethod
    def get_saving_throws(cls, _class: str) -> list:
        """Returns a list of saving throws by class."""
        return cls().find([_class, "saving_throws"])

    @classmethod
    def get_spell_slots(cls, _class: str, level: int, archetype: str) -> str:
        """Returns spell slots by class, level and archetype."""
        try:
            if _class == "Fighter" and archetype != "Eldritch Knight":
                raise KeyError
            elif _class == "Rogue" and archetype != "Arcane Trickster":
                raise KeyError
            else:
                spell_slots = cls().find([_class, "spell_slots", level])
                if len(spell_slots) is not 0:
                    return spell_slots
                else:
                    raise KeyError
        except KeyError:
            return ""


class Feats(Reader):
    def __init__(self) -> None:
        super().__init__("feats")

    @classmethod
    def get_ability_requirements(cls, feat: str) -> dict:
        """Returns ALL ability score requirements for feat."""
        requirements = {}
        strength = cls().find([feat, "strength"])
        if strength > 1:
            requirements["Strength"] = strength
        dexterity = cls().find([feat, "dexterity"])
        if dexterity > 1:
            requirements["Dexterity"] = dexterity
        constitution = cls().find([feat, "constitution"])
        if constitution > 1:
            requirements["Constitution"] = constitution
        intelligence = cls().find([feat, "intelligence"])
        if intelligence > 1:
            requirements["Intelligence"] = intelligence
        wisdom = cls().find([feat, "wisdom"])
        if wisdom > 1:
            requirements["Wisdom"] = wisdom
        charisma = cls().find([feat, "charisma"])
        if charisma > 1:
            requirements["Charisma"] = charisma
        return requirements

    @classmethod
    def get_caster_requirement(cls, feat: str) -> dict:
        """Returns caster requirements for feat."""
        return cls().find([feat, "caster"])

    @classmethod
    def get_feats(cls) -> list:
        """Returns a list of feats."""
        return list(cls().find().keys())

    @classmethod
    def get_proficiency_requirement(cls, feat: str) -> tuple:
        """Returns a tuple of proficiency requirements for feat."""
        return tuple(cls().find([feat, "proficiency"]))

    @classmethod
    def has_requirements(
        cls,
        feat: str,
        _class: str,
        archetype: str,
        level: int,
        abilities: OrderedDict,
        armor_proficiency: list,
        weapon_proficiency: list,
    ) -> bool:
        """Checks if all requirements for feat are met."""
        if (
            feat in ("Heavily Armored", "Lightly Armored", "Moderately Armored",)
            and _class == "Monk"
        ):
            return False
        elif feat in (
            "Heavily Armored",
            "Lightly Armored",
            "Moderately Armored",
            "Weapon Master",
        ):
            # Character already has heavy armor proficiency.
            if feat == "Heavily Armored" and "Heavy" in armor_proficiency:
                return False
            # Character already has light armor proficiency.
            if feat == "Lightly Armored" and "Light" in armor_proficiency:
                return False
            # Character already has medium armor proficiency.
            if feat == "Moderately Armored" and "Medium" in armor_proficiency:
                return False
            # Character already has martial weapon proficiency.
            if feat == "Weapon Master" and "Martial" in weapon_proficiency:
                return False
        elif feat == "Magic Initiative" and _class not in (
            "Bard",
            "Cleric",
            "Druid",
            "Sorcerer",
            "Warlock",
            "Wizard",
        ):
            return False
        proficiency = cls().get_proficiency_requirement(feat)
        proficiencies = armor_proficiency + weapon_proficiency
        if len(proficiency) is not 0 and proficiency not in proficiencies:
            return False
        if cls().get_caster_requirement(feat) and not is_caster(
            _class, level, archetype
        ):
            return False
        for name, value in cls().get_ability_requirements(feat).items():
            my_value = abilities[name]["Value"]
            if feat == "Ritual Caster":
                if my_value >= value:
                    return True
            else:
                if my_value < value:
                    return False
        return True


class Races(Reader):
    def __init__(self) -> None:
        super().__init__("races")

    @classmethod
    def get_languages(cls, race: str, background: str) -> list:
        """Returns a list of languages by race and background."""
        languages = cls().find([race, "languages"])
        # Remove duplicate languages.
        other_languages = [
            "Dwarvish",
            "Elvish",
            "Giant",
            "Gnomish",
            "Goblin",
            "Halfling",
            "Orc",
        ]
        purge(other_languages, languages)
        # Add racial bonus language, if applicable.
        if race in ("Elf, High", "Half-elf", "Human"):
            languages.append(pick(other_languages))
        # Add background bonus language(s).
        background_languages = Backgrounds.get_background_languages(background)
        if background_languages > 0:
            merge(languages, sample(other_languages, background_languages))
        languages.sort()
        return languages

    @classmethod
    def get_races(cls) -> tuple:
        """Returns a tuple of available races."""
        return tuple(cls().find().keys())

    @classmethod
    def get_racial_armor_proficiency(cls, race: str) -> list:
        """Returns a list of armor proficiencies by race."""
        return cls().find([race, "armor_proficiency"])

    @classmethod
    def get_racial_bonus(cls, race: str, variant: bool) -> dict:
        """Returns a dictionary of ability bonuses by race."""
        ability = cls().find([race])
        bonuses = {}
        if ability["strength"] is not 0:
            bonuses["Strength"] = ability["strength"]
        if ability["dexterity"] is not 0:
            bonuses["Dexterity"] = ability["dexterity"]
        if ability["constitution"] is not 0:
            bonuses["Constitution"] = ability["constitution"]
        if ability["intelligence"] is not 0:
            bonuses["Intelligence"] = ability["intelligence"]
        if ability["wisdom"] is not 0:
            bonuses["Wisdom"] = ability["wisdom"]
        if ability["charisma"] is not 0:
            bonuses["Charisma"] = ability["charisma"]
        # Half-elf or Human w/ variant rule.
        if race == "Half-elf" or race == "Human" and variant:
            variant_abilities = [
                "Strength",
                "Dexterity",
                "Constitution",
                "Intelligence",
                "Wisdom",
                "Charisma",
            ]
            # Half-elves get a +2 Charisma, omit this from choices.
            if race == "Half-elf":
                variant_abilities.remove("Charisma")
            abilities = sample(variant_abilities, 2)
            for ability in abilities:
                bonuses[ability] = 1
        # Human w/o variant rule.
        elif race == "Human":
            bonuses["Strength"] = 1
            bonuses["Dexterity"] = 1
            bonuses["Constitution"] = 1
            bonuses["Intelligence"] = 1
            bonuses["Wisdom"] = 1
            bonuses["Charisma"] = 1
        return bonuses

    @classmethod
    def get_racial_tool_proficiency(cls, race: str) -> list:
        """Returns a list of tool proficiencies by race."""
        racial_tools = cls().find([race, "tool_proficiency"])
        if race in ("Dwarf", "Dwarf, Hill", "Dwarf, Mountain"):
            return [choice(racial_tools)]
        return racial_tools

    @classmethod
    def get_racial_weapon_proficiency(cls, race: str) -> list:
        """Returns a list of weapon proficiencies by race."""
        return cls().find([race, "weapon_proficiency"])


class Skills(Reader):
    def __init__(self) -> None:
        super().__init__("skills")

    @classmethod
    def get_class_skills(cls, _class: str) -> list:
        """Returns ALL skills by class."""
        skill_list = list()
        for name in list(cls().find().keys()):
            if _class in cls().get_proficient_classes(name):
                skill_list.append(name)
        return skill_list

    @classmethod
    def get_proficient_classes(cls, skill: str) -> tuple:
        """Returns a tuple of ALL proficient classes by skill."""
        return tuple(cls().find([skill, "classes"]))

    @classmethod
    def get_skill_ability(cls, skill: str) -> str:
        """Returns a skill's associated ability name by skill."""
        return cls().find([skill, "ability"])

    @classmethod
    def get_skills(cls) -> list:
        """Returns ALL skills."""
        return list(cls().find().keys())

    @classmethod
    def select_skills(
        cls, race: str, background: str, _class: str, variant: bool
    ) -> list:
        """Randomly selects skills based upon race, background and class."""
        skills = list()
        background_skills = Backgrounds.get_background_skills(background)
        class_skills = cls().get_class_skills(_class)
        # Add racial skills first.
        if race in ("Elf", "Elf, Drow", "Elf, High", "Elf, Wood", "Half-orc"):
            if race == "Half-orc":
                racial_skill = "Intimidation"
            else:
                racial_skill = "Perception"
            skills.append(racial_skill)
        elif race == "Half-elf" or race == "Human":
            # Remove background, class skills from all skill choices.
            all_skill_choices = cls().get_skills()
            purge(all_skill_choices, background_skills)
            purge(all_skill_choices, class_skills)
            if race == "Half-elf":
                merge(skills, sample(all_skill_choices, 2))
            elif race == "Human" and variant:
                skills.append(choice(all_skill_choices))
        # Next, add background skills.
        if len(background_skills) is not 0:
            merge(skills, background_skills)
        # Finally, choose class skills.
        purge(class_skills, skills)
        merge(skills, sample(class_skills, get_skill_allotment(_class)))
        skills.sort()
        return skills


class Tools(Reader):
    def __init__(self) -> None:
        super().__init__("tools")

    @classmethod
    def get_main_tools(cls) -> tuple:
        """Returns a tuple of all main level tools."""
        return tuple(cls().find().keys())

    @classmethod
    def get_sub_tools(cls, tool: str) -> tuple:
        """Return a tuple of sub level tools for a tool."""
        tools = tuple(cls().find([tool]))
        if len(tools) > 0:
            return tools
        return tuple()

    @classmethod
    def get_tools(cls, main_tools: (list, set, tuple, None)) -> list:
        """Returns a tuple of ALL tools or main tools, if applicable."""
        tools = list()
        if isinstance(main_tools, (list, set, tuple)):
            for tool in main_tools:
                if not cls().has_sub_tools(tool):
                    continue
                for sub_tool in cls().get_sub_tools(tool):
                    tools.append("{}: {}".format(tool, sub_tool))
        else:
            for tool in list(cls().get_main_tools()):
                if cls().has_sub_tools(tool):
                    for sub_tool in cls().get_sub_tools(tool):
                        tools.append("{}: {}".format(tool, sub_tool))
                else:
                    tools.append(tool)
        tools.sort()
        return tools

    @classmethod
    def has_sub_tools(cls, tool: str) -> bool:
        """Checks if a tool has sub level tools."""
        if len(cls().get_sub_tools(tool)) is 0:
            return False
        return True


class Weapons(Reader):
    def __init__(self) -> None:
        super().__init__("weapons")

    @classmethod
    def get_martial_weapons(cls) -> list:
        """Returns a list of martial weapons."""
        return cls().find(["Martial"])

    @classmethod
    def get_simple_weapons(cls) -> list:
        """Returns a list of simple weapons."""
        return cls().find(["Simple"])


def get_ability_modifier(scores, ability) -> int:
    """Returns ability modifier value from dictionary of abilities."""
    return scores[ability]["Modifier"]


def get_skill_allotment(_class: str) -> int:
    """Returns allotment value of skills by class."""
    if _class in ("Rogue",):
        skill_allotment = 4
    elif _class in ("Bard", "Ranger"):
        skill_allotment = 3
    else:
        skill_allotment = 2
    return skill_allotment


def get_allotted_feats(_class: str, level: int) -> int:
    """Returns allotment value of feats by class and level."""
    allotted_feats = 0
    for _ in range(1, level + 1):
        if (_ % 4) == 0 and _ is not 20:
            allotted_feats += 1
    if _class == "Fighter" and level >= 6:
        allotted_feats += 1
    if _class == "Rogue" and level >= 8:
        allotted_feats += 1
    if _class == "Fighter" and level >= 14:
        allotted_feats += 1
    if level >= 19:
        allotted_feats += 1
    return allotted_feats


def get_proficiency(proficiency: str, _race: str, _class: str) -> list:
    proficiency_list = {
        "armors": {
            "class": Classes.get_class_armor_proficiency(_class),
            "racial": Races.get_racial_armor_proficiency(_race),
        },
        "tools": {
            "class": Classes.get_class_tool_proficiency(_class),
            "racial": Races.get_racial_tool_proficiency(_race),
        },
        "weapons": {
            "class": Classes.get_class_weapon_proficiency(_class),
            "racial": Races.get_racial_weapon_proficiency(_race),
        },
    }
    try:
        proficiencies = proficiency_list[proficiency]["racial"]
        proficiencies += proficiency_list[proficiency]["class"]
        proficiencies = list(dict.fromkeys(proficiencies))
        proficiencies.sort()
        return proficiencies
    except KeyError:
        return list()


def get_proficiency_bonus(level: int) -> int:
    """Returns a proficiency bonus value by level."""
    return ceil((level / 4) + 1)


def is_caster(_class: str, level: int, archetype=None) -> bool:
    """Returns True if caster by _class, level, archetype or False if not."""
    if _class in ("Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"):
        return True
    elif _class in ("Paladin", "Ranger") and level > 1:
        return True
    elif _class is "Fighter" and archetype in ("Eldritch Knight",):
        return True
    elif _class is "Rogue" and archetype in ("Arcane Trickster",):
        return True
    return False
