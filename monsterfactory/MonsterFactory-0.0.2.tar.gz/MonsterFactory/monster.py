from math import ceil
from MonsterFactory.monster_lib import *


class Monster:

    def __init__(self, cr=None):
        self.cr = CR(cr) if cr else CR(front_linear(28) + plus_or_minus_gauss(3))
        self.tier = self.cr.tier
        self.type = type_by_tier(str(self.tier))
        self.name = random_monster(self.type)
        variance = plus_or_minus_gauss(self.tier)
        self.ac = monster_stats["AC"][self.cr.key] + variance
        self.att = monster_stats["ATT"][self.cr.key] - variance
        self.hp_range = monster_stats["HP Range"][self.cr.key]
        lo, hi = self.hp_range
        self.hp = distribution_range(middle_linear, lo, hi) - (variance * self.tier)
        self.hp = ceil(self.hp * type_modifier(self.type))
        self.dc = monster_stats["DC"][self.cr.key] + variance
        self.damage_range = monster_stats["Damage Range"][self.cr.key]
        lo, hi = self.damage_range
        self.dam = distribution_range(middle_linear, lo, hi) + (variance * self.tier)
        self.xp = ceil(monster_stats["XP"][self.cr.key] * type_modifier(self.type))

    def get_data(self):
        return {
            "Name": f"{self.name}",
            "Type": f"{self.type}",
            "CR": f"{self.cr.string}",
            "Health": f"{self.hp}",
            "Armor Class": f"{self.ac}",
            "Attack Bonus": f"{self.att}",
            "Save DC": f"{self.dc}",
            "Typical Damage": f"{self.dam}",
            "XP Value": f"{self.xp}",
        }

    def __str__(self):
        output = (
            f"{self.name}",
            f"Type: {self.type}",
            f"CR: {self.cr.string}",
            f"Health: {self.hp}",
            f"Armor Class: {self.ac}",
            f"Attack Bonus: {self.att}",
            f"Save DC: {self.dc}",
            f"Typical Damage: {self.dam}",
            f"XP Value: {self.xp}",
            ""
        )
        return '\n'.join(output)


if __name__ == '__main__':
    m = Monster(10)
    print(m)
