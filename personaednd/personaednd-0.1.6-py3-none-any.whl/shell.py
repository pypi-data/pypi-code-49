from collections import OrderedDict
import os
import time

from bs4 import BeautifulSoup
import click

from personaednd.attributes import ScoreAssigner, ScoreImprovement
from personaednd.sources import (
    get_ability_modifier,
    get_proficiency,
    get_proficiency_bonus,
    Backgrounds,
    Classes,
    Races,
    Skills,
)
from personaednd.sources.reader import Reader
from personaednd.version import __version__


class ValidParameters(Reader):
    def __init__(self, source=None) -> None:
        super().__init__(source)

    @classmethod
    def __toTuple__(cls, source, index=None) -> (tuple, str):
        _tuple = tuple(cls(source).find().keys())
        if isinstance(index, int):
            try:
                return _tuple[index]
            except IndexError:
                return _tuple
        return _tuple

    @classmethod
    def get(cls, source, index=None) -> (__toTuple__, str):
        try:
            if source not in ("backgrounds", "classes", "races", "skills"):
                raise ValueError
        except ValueError:
            exit("source: invalid source specified '{}'.".format(source))
        return cls.__toTuple__(source, index)


class WriterBlobTypeError(TypeError):
    """Raised if data is not of type 'dict'."""


class WriterBlobValueError(Exception):
    """Raised if not all keys have purged_values."""


class Writer:
    def __init__(self, output_file: str, data: dict) -> None:
        if not isinstance(data, dict):
            raise WriterBlobTypeError("data: argument must be of type 'dict'!")
        data_keys = (
            "race",
            "background",
            "class",
            "archetype",
            "level",
            "proficiency",
            "abilities",
            "saves",
            "armors",
            "weapons",
            "tools",
            "slots",
            "languages",
            "skills",
            "feats",
            "equipment",
        )
        if not all(k in data for k in data_keys):
            raise WriterBlobValueError("data: all keys must have a value!")
        blob = list()
        blob.append(data["race"])
        blob.append(data["background"])
        blob.append(data["class"])
        blob.append(data["archetype"])
        blob.append(data["level"])
        blob.append(data["proficiency"])
        blob.append(self._format_ability_scores(data["abilities"]))
        blob.append(
            self._format_saving_throws(data["abilities"], data["level"], data["saves"])
        )
        blob.append(self._format_list(data["armors"]))
        blob.append(self._format_list(data["weapons"]))
        blob.append(self._format_list(data["tools"]))
        blob.append(data["slots"])
        blob.append(self._format_list(data["languages"]))
        blob.append(
            self._format_skills(data["skills"], data["abilities"], data["level"])
        )
        blob.append(self._format_list(data["feats"]))
        blob.append(self._format_list(data["equipment"]))
        self.file = output_file
        self.data = tuple(blob)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, value, traceback):
        pass

    @staticmethod
    def _format_ability_scores(scores: OrderedDict) -> str:
        """Formats ability scores for character sheet."""
        my_scores = ""
        for ability, values in scores.items():
            value = values["Value"]
            modifier = values["Modifier"]
            my_scores += '<{} score="{}" modifier="{}" />'.format(
                ability, value, modifier
            )
        return my_scores

    @staticmethod
    def _format_list(iterable: (list, set, tuple)) -> str:
        """Formats list elements for character sheet."""
        my_iterable = ""
        if len(iterable) < 1:
            return my_iterable
        for entry in iterable:
            entry = entry.replace(" ", "_")
            my_iterable += '<item value="{}" />'.format(entry)
        return my_iterable

    @staticmethod
    def _format_saving_throws(
        scores: OrderedDict, level: int, proficient_saving_throws: (list, set, tuple)
    ) -> str:
        """Formats saving throws for character sheet."""
        saving_throws = (
            "Strength",
            "Dexterity",
            "Constitution",
            "Intelligence",
            "Wisdom",
            "Charisma",
        )
        my_saves = ""
        for saving_throw in saving_throws:
            ability_modifier = scores[saving_throw]["Modifier"]
            proficiency_bonus = (
                saving_throw in proficient_saving_throws
                and get_proficiency_bonus(level)
                or 0
            )
            total_save = ability_modifier + proficiency_bonus
            my_saves += '<{} value="{}"/>'.format(saving_throw, total_save)
        return my_saves

    @staticmethod
    def _format_skills(
        skills: (list, set, tuple), scores: OrderedDict, level: int
    ) -> str:
        """Formats skill values for character sheet."""
        expanded_skills = {}
        for skill in skills:
            skill_ability = Skills.get_skill_ability(skill)
            expanded_skills[skill] = {
                "Ability": skill_ability,
                "Modifier": get_ability_modifier(scores, skill_ability),
            }
        my_skills = ""
        for skill, values in sorted(expanded_skills.items()):
            skill_name = skill.replace(" ", "_")
            skill_total = get_proficiency_bonus(level) + values["Modifier"]
            my_skills += '<{} ability="{}" value="{}" />'.format(
                skill_name, values["Ability"], skill_total,
            )
        return my_skills

    def write(self) -> None:
        """Writes data to character sheet."""
        template = """<?xml version="1.0"?>
            <Personae>
                <Race name="%s" background="%s" />
                <Class name="%s" archetype="%s" level="%s" proficiency="%s" />
                <AbilityScores>%s</AbilityScores>
                <SavingThrows>%s</SavingThrows>
                <ArmorProficiencies>%s</ArmorProficiencies>
                <WeaponProficiencies>%s</WeaponProficiencies>
                <ToolProficiencies>%s</ToolProficiencies>
                <Spell slots="%s" />
                <Languages>%s</Languages>
                <Skills>%s</Skills>
                <Feats>%s</Feats>
                <Equipment>%s</Equipment>
            </Personae>"""
        with open(self.file, "w+") as character_sheet:
            data = template % self.data
            character_sheet.write(BeautifulSoup(data, "xml").prettify())
        character_sheet.close()


def _err(message: str) -> None:
    click.secho(
        message, bold=True, err=True, fg="red",
    )
    exit()


def _out(message: str) -> None:
    click.secho(
        message, bold=True, fg="green",
    )


@click.command()
@click.option(
    "-race",
    default=ValidParameters.get("races", 0),
    show_default=True,
    type=str,
    required=True,
    help="Character's chosen race.",
)
@click.option(
    "-background",
    default=Classes.get_class_background(ValidParameters.get("classes", 0)),
    show_default=True,
    type=str,
    required=True,
    help="Character's chosen background.",
)
@click.option(
    "-class_",
    default=ValidParameters.get("classes", 0),
    show_default=True,
    type=str,
    required=True,
    help="Character's chosen class.",
)
@click.option(
    "-archetype", default=None, type=str, help="Character's chosen archetype."
)
@click.option(
    "-level",
    default=1,
    show_default=True,
    type=int,
    required=True,
    help="Character's chosen class level.",
)
@click.option(
    "-variant",
    default="false",
    show_default=True,
    type=str,
    required=True,
    help="Determines if variant trait applies.",
)
@click.version_option(version=__version__)
def main(
    race: str, background: str, class_: str, archetype: str, level: int, variant=str,
) -> None:
    # Create sources save directory (if necessary).
    home_directory = os.path.expanduser("~/Personae")
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)
        click.echo("Personae directory created at '{}'.".format(home_directory))
    click.echo("Characters will be saved to '{}'.".format(home_directory))

    # CLI argument checking
    if race not in ValidParameters.get("races"):
        _err("Invalid sources race '{}'.".format(race))
    if background not in ValidParameters.get("backgrounds"):
        _err("Invalid sources background '{}'.".format(background))
    if class_ not in ValidParameters.get("classes"):
        _err("Invalid sources class '{}'.".format(class_))
    if archetype is not None and archetype not in Classes.get_archetypes(class_):
        _err("Invalid sources archetype '{}' for '{}'.".format(archetype, class_))
    if level not in range(0, 21):
        _err("Invalid level '{}' specified. Range (1-20).".format(level))
    if variant not in ("false", "true"):
        _err("Invalid variant option '{}' specified. false|true.".format(variant))
    else:
        if variant == "false":
            variant = False
        elif variant == "true":
            variant = True

    # Rudimentary sources additions.
    equipment = Backgrounds.get_background_equipment(background)
    slots = Classes.get_spell_slots(class_, level, archetype)

    # Determine and assign ability score improvements, if applicable.
    a = ScoreAssigner(class_, race, variant)
    asi = ScoreImprovement(
        _class=class_,
        archetype=archetype,
        level=level,
        race=race,
        abilities=a.abilities,
        primaries=a.primaries,
        armor_proficiency=get_proficiency("armors", race, class_),
        tool_proficiency=get_proficiency("tools", race, class_),
        weapon_proficiency=get_proficiency("weapons", race, class_),
        languages=Races.get_languages(race, background),
        skills=Skills.select_skills(race, background, class_, variant),
        feats=list(),
        variant=variant,
    )
    asi.assign_upgrades()
    languages = asi.languages
    armors = asi.armors
    tools = asi.tools
    weapons = asi.weapons
    feats = asi.feats
    skills = asi.skills
    abilities = asi.abilities
    saves = asi.saves

    # Prepare data for writing.
    data = dict()
    data["race"] = race
    data["background"] = background
    data["class"] = class_
    data["archetype"] = archetype
    data["level"] = level
    data["proficiency"] = get_proficiency_bonus(level)
    data["abilities"] = abilities
    data["saves"] = saves
    data["armors"] = armors
    data["tools"] = tools
    data["weapons"] = weapons
    data["slots"] = slots
    data["languages"] = languages
    data["skills"] = skills
    data["feats"] = feats
    data["equipment"] = equipment

    # Character sheet data review.
    _out("*" * 40)
    _out("Race (Background): {} ({})".format(data["race"], data["background"]))
    _out("Class (Level): {} ({})".format(data["class"], level))
    _out("Archetype: {}".format(data["archetype"]))
    for ability, values in data["abilities"].items():
        _out("{}: {} ({})".format(ability, values["Value"], values["Modifier"]))
    _out("Armor Proficiencies: {}".format(", ".join(data["armors"])))
    _out("Tool Proficiencies: {}".format(", ".join(data["tools"])))
    _out("Weapon Proficiencies: {}".format(", ".join(data["weapons"])))
    _out("Languages: {}".format(", ".join(data["languages"])))
    _out("Feats: {}".format(", ".join(data["feats"])))
    _out("Skills: {}".format(", ".join(data["skills"])))
    _out("Saving Throws: {}".format(", ".join(data["saves"])))
    _out("Equipment: {}".format(", ".join(data["equipment"])))
    _out("*" * 40)

    # Prompt.
    while True:
        click.echo("Save character? (y/n) ", nl=False)
        prompt = click.getchar()
        click.echo()
        if prompt in ("y", "Y"):
            try:
                file_name = time.ctime(time.time()).replace(" ", "_") + ".xml"
                fp = "{}/{}".format(home_directory, file_name)
                with Writer(fp, data) as output:
                    output.write()
                click.echo("Character saved to '{}'.".format(fp))
            except WriterBlobValueError as err:
                click.echo(err)
            except WriterBlobTypeError as err:
                click.echo(err)
            break
        elif prompt in ("n", "N"):
            click.echo("Aborted. Character not saved.")
            break
        else:
            continue


if __name__ == "__main__":
    main()
