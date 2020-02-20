from Fortuna import *


class CR:
    """ The CR class is a numeric system representing the relative power of a monster in D&D 5e.
    This system is a bit funky with values below 1, be careful... here be dragons!
    CR less than 1 are printed as fractions but valued mathematically as integers [-3, 0].
    CR(-3) is CR 1/16 - same as CR 0 in the books.
    CR(-2) is CR 1/8
    CR(-1) is CR 1/4
    CR(0) is CR 1/2
    CR(1)..CR(30) is CR 1 to CR 30
    Why is this system so crazy? Because wizards are bad at math!
    And I wanted to ignore the fractions...
    So that subtracting 1 always takes you to the next CR down.
    Currently: CR(1) + CR(1) is CR(2)
    what is CR 1/2 + CR 1/4 ???
    This is an open question! It may cause me to switch to floats internally, eww.
    """

    def __init__(self, val):
        self.val = smart_clamp(val, -3, 30)

    @property
    def value(self):
        return self.val

    @property
    def key(self):
        return self.val + 3

    @property
    def string(self):
        if self.val > 0:
            str_cr = f"{self.val}"
        else:
            str_cr = ("1/16", "1/8", "1/4", "1/2")[self.key]
        return str_cr

    @property
    def tier(self):
        return (
            0, 0, 0, 0,
            1, 1, 1, 1, 1,
            2, 2, 2, 2, 2,
            3, 3, 3, 3, 3,
            4, 4, 4, 4, 4,
            5, 5, 5, 5, 5,
            6, 6, 6, 6, 6,
        )[self.key]

    @classmethod
    def party_adapter(cls, average_level, num_players=5, difficulty=0):
        average_level = smart_clamp(average_level, 1, 20)
        num_players = smart_clamp(num_players, 1, 9) - 5
        magic_bonus = (
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4,
        )[average_level]
        diff_modifier = smart_clamp(difficulty, -5, 5)
        return CR(num_players + average_level + magic_bonus + diff_modifier)

    def __str__(self):
        return self.string

    def __add__(self, other):
        self.val = smart_clamp(self.val + other, -3, 30)
        return self

    def __sub__(self, other):
        self.val = smart_clamp(self.val - other, -3, 30)
        return self


def type_modifier(monster_type):
    lookup = {
        "Minion": 0.5,
        "Monster": 1.0,
        "Elite Monster": 1.10,
        "Villain": 1.20,
        "Dungeon Boss": 1.50,
        "Campaign Boss": 2.0,
    }
    return lookup[monster_type]


monster_stats = {
    "AC": (
        8, 9, 10, 11,
        11, 12, 13, 14, 14, 15, 15, 16, 16, 17,
        17, 17, 18, 18, 18, 18, 19, 19, 19, 19,
        19, 20, 20, 20, 20, 20, 21, 21, 21, 22,
    ),
    "ATT": (
        0, 1, 2, 3,
        3, 3, 4, 5, 5, 6, 6, 7, 7, 7,
        8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14,
    ),
    "HP Range": (
        (1, 7), (7, 36), (36, 50), (50, 71),
        (71, 86), (86, 101), (101, 116), (116, 131), (131, 146),
        (146, 161), (161, 176), (176, 191), (191, 206), (206, 221),
        (221, 236), (236, 251), (251, 266), (266, 281), (281, 296),
        (296, 311), (311, 326), (326, 341), (341, 356), (356, 401),
        (401, 446), (446, 491), (491, 536), (536, 581), (581, 626),
        (626, 671), (671, 716), (716, 761), (761, 806), (806, 851),
    ),
    "DC": (
          13, 13, 13, 13,
          13, 13, 13, 14, 15, 15, 15, 16, 16, 16,
          17, 17, 18, 18, 18, 18, 19, 19, 19, 19,
          20, 20, 20, 21, 21, 21, 22, 22, 23, 24,
    ),
    "Damage Range": (
        (1, 2), (2, 3), (4, 5), (6, 8),
        (9, 14), (15, 20), (21, 26), (27, 32), (33, 38),
        (39, 44), (45, 50), (51, 56), (57, 62), (63, 68),
        (69, 74), (75, 80), (81, 86), (87, 92), (93, 98),
        (99, 104), (105, 110), (111, 116), (117, 122), (123, 140),
        (141, 158), (159, 176), (177, 194), (195, 212), (213, 230),
        (231, 248), (249, 266), (267, 284), (285, 302), (303, 320),
    ),
    "XP": (
        10, 25, 50, 100,
        200, 450, 700, 1100, 1800,
        2300, 2900, 3900, 5000, 5900,
        7200, 8400, 10000, 11500, 13000,
        15000, 18000, 20000, 22000, 25000,
        33000, 41000, 50000, 62000, 155000,
        155000, 155000, 155000, 155000, 155000,
        155000, 155000, 155000, 155000, 155000,
    ),
}


rand_elemental = TruffleShuffle((
    "Fire",
    "Water",
    "Lightning",
    "Smoke",
    "Mud",
    "Steam",
    "Ice",
    "Magma",
    "Dust",
))

rand_golem = TruffleShuffle((
    "Bone",
    "Flesh",
    "Steampunk",
    "Mud",
    "Ice",
    "Copper",
    "Tin",
    "Silver",
))

rand_color = FlexCat({
    "chromatic": (
        "Red",
        "Green",
        "Blue",
        "Black",
        "White",
        "Shadow",
    ),
    "metal": (
        "Brass",
        "Copper",
        "Bronze",
        "Silver",
        "Gold",
        "Platinum",
    ),
    "crystal": (
        "Ruby",
        "Emerald",
        "Sapphire",
        "Quartz",
        "Diamond",
        "Onyx",
    ),
}, key_bias="front_linear", val_bias="front_linear")

rand_knight = TruffleShuffle((
    "Flaming Tongue",
    "Frozen Waste",
    "Drunken Monkey",
    "Hidden Rose",
    "Thunderbolts",
    "Shadows",
    "Broken Lance",
    "Grim Reaper",
    "Three-eyed Raven",
))

rand_adventurer = TruffleShuffle((
    "Fighter",
    "Rogue",
    "Beast Master",
    "Archer",
    "Cleric",
    "Wizard",
    lambda: f"Warlock" if percent_true(50) else f"Witch",
    lambda: f"Sorceress" if percent_true(50) else f"Sorcerer",
    lambda: f"Barbarian" if percent_true(50) else f"Valkyrie",
    "Dark Paladin",
    "Demonic Summoner",
    lambda: f"Enchantress" if percent_true(50) else f"Enchanter",
    "Voodoo Witch Doctor",
    "Wild Mage",
    lambda: f"Knight of the {rand_knight()}",
    "Defender",
    "Acolyte",
    lambda: f"Priestess" if percent_true(50) else f"Priest",
    "Zealot",
    "Cultist",
    "Gladiator",
    "Pirate",
    "Ninja",
    "Alchemist",
    "Artificer",
    "Shaman",
    "Blood Witch",
    "Necromancer",
    "Arcane Trickster",
    "Acrobat",
    "Assassin",
    "Inquisitor",
))


rand_giant = TruffleShuffle((
    'Hill',
    'Stone',
    'Cloud',
    'Frost',
    'Fire',
    'Storm',
    'Two-headed',
))

rand_race = QuantumMonty((
    "Human",
    "Dwarf",
    "Halfling",
    "Gnome",
    "Elf",
    "Half-elf",
    "Drow",
    "Tiefling",
    "Dragonborn",
    "Half-orc",
    "Goblin",
    "Orc",
    "Half-giant",
    "Half-dragon",
)).front_linear


rand_devil = TruffleShuffle((
    "Flames",
    "Ice",
    "Barbs",
    "Bones",
    "Chains",
    "Blades",
    "Hooks",
    "the Horned One",
))

rand_lycanthrope = QuantumMonty((
    "Werewolf",
    "Wererat",
    "Werecat",
    "Wereboar",
    "Werebear",
    "Werecheetah",
    "Werepanther",
    "Weretiger",
    "Werelion",
)).front_linear

type_by_tier = FlexCat({
    "0": ('Minion', 'Monster'),
    "1": ('Monster', 'Minion'),
    "2": ('Monster', 'Minion', 'Elite Monster'),
    "3": ('Villain', 'Monster', 'Elite Monster'),
    "4": ('Villain', 'Elite Monster', 'Monster'),
    "5": ('Dungeon Boss', 'Villain', 'Elite Monster', 'Monster'),
    "6": ('Campaign Boss', 'Dungeon Boss', 'Villain', 'Elite Monster'),
}, val_bias="front_linear")

random_monster = FlexCat({
    'Minion': (
        lambda: f"Novice {rand_adventurer()}",
        lambda: f"{rand_elemental()} Mephit",
        lambda: f"Zombie {rand_race()}",
        "Troll",
        "Ogre",
        "Jackalope",
        "Imp",
        lambda: f"Skeleton {rand_adventurer()}",
        "Quasit",
        "Gremlin",
        "Kobold",
        "Gnoll",
        "Gelatinous Cube",
        "Drider",
        "Tasmanian Devil",
        "Crawling Claw",
        "Gargoyle",
        "Hell Hound",
        "Gelatinous Spores",
        "Sasquatch",
        "Yeti",
        "Umber Hulk",
        "Bugbear",
        "Owlbear",
        "Winged Kobold",
        lambda: f"{rand_color()} Dragon Hatchling",
    ),
    'Monster': (
        "Chimera",
        "Demon Cat",
        "Basilisk",
        "Hobgoblin",
        "Cyclops",
        "Cave Troll",
        "Displacer Beast",
        "Gelatinous Sphere",
        lambda: f"{rand_golem()} Golem",
        "Shield Guardian",
        "Wyvern",
        "Wraith",
        "Intellect Devourer",
        "Ghoul",
        "Shadow",
        "Rust Monster",
        "Worg",
        "Hook Horror",
        "Mimic",
        "Flameskull",
        lambda: f"Vampire Spawn, {rand_race()}",
        lambda: f"Young {rand_color()} Dragon",
    ),
    'Elite Monster': (
        "Xorn",
        "Bafu",
        "Chupacabra",
        "Skeletal Monstrosity",
        "Nightmare",
        "Bile Demon",
        lambda: f"Goblin {rand_adventurer()}",
        lambda: f"Lycanthrope: {rand_lycanthrope()}",
        lambda: f"{rand_giant()} Giant",
        lambda: f"Ghost: {rand_race()}",
        lambda: f"{rand_elemental()} Elemental",
        lambda: f"Vampire, {rand_race()}",
        lambda: f"{rand_color()} Dragon",
    ),
    'Villain': (
        lambda: f"{rand_race()} {rand_adventurer()}",
        lambda: f"{rand_elemental()} Demon",
        lambda: f"Incubus" if percent_true(30) else f"Succubus",
        lambda: f"Doppelganger: {rand_race()}",
        "Wailing Banshee",
        lambda: f"{'Goblin' if percent_true(50) else 'Gnomish'} War Tank",
        lambda: f"Devil of {rand_devil()}",
        lambda: f"Legendary Lycanthrope: {rand_lycanthrope()}",
        "Efreeti",
        "Mummy",
        lambda: f"Elder Vampire, {rand_race()}",
        "Death Tyrant",
        "Demilich",
        "Mind Flayer",
        lambda: f"Adult {rand_color()} Dragon",
        lambda: f"Legendary {rand_race()} {rand_adventurer()}",
    ),
    'Dungeon Boss': (
        "Hydra",
        "The Rat King",
        "Behemoth",
        "Cerberus",
        lambda: f"Arch Devil of {rand_devil()}",
        "Poltergeist",
        "Death Knight",
        "Pit Lord",
        lambda: f"Vampire Lord, {rand_race()}",
        "Mummy Lord",
        "Beholder",
        lambda: f"Ancient {rand_color()} Dragon",
        "Ancient Dracolich",
    ),
    'Campaign Boss': (
        lambda: f"Elemental Lord of {rand_elemental()}",
        "Goblin King",
        "Balor",
        lambda: f"Legendary Devil of {rand_devil()}",
        "Mummy Pharaoh",
        "Lich King",
        "Beholder Overseer",
        lambda: f"Legendary Vampire: {rand_race()} {rand_adventurer()}",
        "Lord of the Pit",
        "Grim Reaper",
        "Flying Spaghetti Monster",
        lambda: f"Legendary {rand_color()} Dragon",
        "The Nameless One",
    ),
})
