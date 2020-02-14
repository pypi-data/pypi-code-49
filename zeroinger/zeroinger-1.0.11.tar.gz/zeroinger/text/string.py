class StringUtils:
    @staticmethod
    def is_empty(text: str) -> bool:
        """
        判断这个字符串是否为空
        :param text: 
        :return: 
        """
        if text is None:
            return True
        c = text.strip()
        if len(c) == 0:
            return True
        return False
