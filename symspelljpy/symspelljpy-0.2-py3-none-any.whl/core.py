import pexpect
import os
import json
import time
from symspelljpy import path_resolver


class SymSpellClient(object):

    def __init__(self,
                 uni_gram_dict_path=None, bi_gram_dict_path=None, enable_timer=True,
                 max_edit=2, distance_type='VDL', topK=5, max_word_len=10, mode='SMART'):

        jar_path = os.path.join(
            path_resolver.src_dir(), 'resources/spellcheckclient-jar-with-dependencies.jar'
        )
        init_command = [
            '-jar', jar_path,
            '-e', str(max_edit),
            '-d', distance_type,
            '-k', str(topK),
            '-w', str(max_word_len),
            '-m', str(mode)
        ]

        if uni_gram_dict_path is not None:
            init_command.extend(['-u', uni_gram_dict_path])
        if bi_gram_dict_path is not None:
            init_command.extend(['-b', bi_gram_dict_path])
        if enable_timer:
            init_command.append('-t')

        print(' '.join(init_command))

        self.process = pexpect.spawn(
            'java', args=init_command,
            timeout=None,
        )
        print(self.process.readline().decode("utf-8"))

    def lookup(self, input_phase):
        self.process.sendline(input_phase)
        self.process.readline()
        stdout_value = self.process.readline().decode("utf-8")
        return json.loads(stdout_value, encoding='utf-8')

    def close(self):
        self.process.sendline('q')
        self.process.close()