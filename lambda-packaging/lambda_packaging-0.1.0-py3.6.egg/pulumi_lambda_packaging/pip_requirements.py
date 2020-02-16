import requirements as req
import subprocess
import os

class PipRequirements(object):
    def __init__(self, requirements_path, target_path, no_deploy=[]):
        self.pip_cmd = ['python3', '-m', 'pip', 'install', '-r']
        self.no_deploy = no_deploy
        self.target_path = target_path
        self.target_requirements_path = f'{target_path}/requirements.txt'
        self.target_install_path = os.path.join(target_path, 'requirements')

        self.requirements_path = requirements_path
        if not os.path.isdir(self.target_install_path):
            os.makedirs(self.target_install_path, exist_ok=True)

    def generate_requirements_file(self):
        requirements = self.filter_requirements()
        with open(self.target_requirements_path, 'w') as f:
            for requirements in requirements:
                f.write(f'{requirements}\n')

    def filter_requirements(self):
        with open(self.requirements_path, 'r') as f:
            requirements = {r.name: r.line for r in req.parse(f)}
        for n in self.no_deploy:
            requirements.pop(n)
        return requirements


    def install_requirements(self):
        self.generate_requirements_file()
        self.pip_cmd.append(self.target_requirements_path)
        self.pip_cmd.append(f'--target={self.target_install_path}')
        subprocess.run(self.pip_cmd)
