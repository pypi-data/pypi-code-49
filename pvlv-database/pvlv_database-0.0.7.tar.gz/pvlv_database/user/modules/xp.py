class XpData(object):

    def __init__(self):

        self.level_up_notification = False
        self.xp_value = 10
        self.level = 0

        self.__is_level_up = False  # internal value, it go true when there is a level up

    def extract_data(self, raw_data):

        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.xp_value = raw_data.get('xp', self.xp_value)
        self.level = raw_data.get('level', self.level)

        return self

    def build_data(self):

        data_out = {
            'level_up_notification': self.level_up_notification,
            'xp': self.xp_value,
            'level': self.level,
        }

        return data_out

    @property
    def is_level_up(self):
        """
        Check if is time to level up, once controlled it will auto reset.
        You will find this true only once.
        :return: True or False
        """
        if self.__is_level_up:
            self.__is_level_up = False
            return True
        return False

    @staticmethod
    def __xp_to_level(level):
        return (level * (level + 1) / 4) * 300

    def update_xp_value(self, value: int):
        """
        It will add the xp provided to the total count and check if is time to level up
        After this command check is_level_up to see if there is a level up
        :param value: xp to add
        """
        self.xp_value += value
        xp_to_next_level = self.__xp_to_level(self.level)
        if xp_to_next_level <= self.xp_value:
            self.level += 1
            self.__is_level_up = True

    def xp_in_level(self):
        """
        Total xp in the current level,
        this is the xp you have to gain in this level to level up.
        :return: xp value as int
        """
        if self.level is 0:
            return self.__xp_to_level(self.level)
        else:
            return self.__xp_to_level(self.level) - self.__xp_to_level(self.level - 1)

    def xp_left(self):
        """
        Xp left to level up
        :return: xp left as int
        """
        return self.xp_value - self.__xp_to_level(self.level - 1)
