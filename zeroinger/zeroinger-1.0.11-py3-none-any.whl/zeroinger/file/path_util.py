import os


class PathUtil:
    @staticmethod
    def path_relative_to_code(code_file, rel_path: str) -> str:
        """
        基于当前代码文件+相对路径生成文件路径
        :param code_file: __file__ 
        :param rel_path: abc/fds/fsd.txt
        :return: 
        """
        return os.path.join(os.path.dirname(code_file), rel_path)
        pass
