from typing import Tuple, List
import re
from colorama import Fore, Back
from colorama.ansi import code_to_chars


def clrm_from_color_char_to_code(char):
    return int(re.findall(r"\x1b\[(\d+)m", char)[0])


class Detector:
    # TODO: понять что я написал
    def __init__(self, level=1):
        self.targets = ["57", "69", "179", "228"]
        self.pattern = "[(%s)]" % (")(".join(self.targets))
        self.level = level

    def analyse(self, calc_res, level=None) -> List[Tuple[int, int]]:
        if level is None:
            level = self.level
        string = str(calc_res)
        if level == 0:
            return []
        elif level == 1:
            if string in self.targets:
                return [(0, len(string))]
        elif level == 2:
            detection_res = []
            p = 0
            while p < len(string):
                search_res = re.search(self.pattern, string[p:])
                if search_res is None:
                    break
                p_new = p + search_res.end() + 1
                detection_res.append((p + search_res.start(), p_new))
                p = p_new
            return detection_res
        else:
            raise ValueError("Invalid cool numbers detection level")

    def color_marked(self, text: str, fg: str = Fore.WHITE, bg: str = Back.BLACK):
        new_fg = code_to_chars(clrm_from_color_char_to_code(bg) - 10)
        new_bg = code_to_chars(clrm_from_color_char_to_code(fg) + 10)
        suspiciously = self.analyse(text)
        listed_text: List = list(text)
        expanded = 0
        # Govnokod, syda ne smotri
        for mark_st, mark_end in suspiciously:
            listed_text.insert(mark_st + expanded, new_fg)
            expanded += 1
            listed_text.insert(mark_st + expanded, new_bg)
            expanded += 1
            listed_text.insert(mark_end + expanded, fg)
            expanded += 1
            listed_text.insert(mark_end + expanded, bg)
            expanded += 1
        return "".join(listed_text)
