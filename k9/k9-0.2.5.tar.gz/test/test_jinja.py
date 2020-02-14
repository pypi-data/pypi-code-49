from unittest import TestCase, mock
from jinja2 import Environment, Template, FileSystemLoader

import io
import os
import yaml

class TestJinja(TestCase):

    def test_template_string(self):
        template = Template('Hello {{ name }}!')
        self.assertEqual('Hello John Doe!', template.render(name='John Doe'))

    def test_template_file(self):
        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'charts')
        env = Environment(loader=FileSystemLoader(templates_dir))

        template = env.get_template("jenkins-values.yml")

        result = template.render(domain="fast.sandbox.simoncomputing.com")
        memory_file = io.StringIO(result)

        obj = yaml.safe_load(memory_file)
        self.assertEqual("jenkins.fast.sandbox.simoncomputing.com", obj['jenkins']['clusterZone'])
        self.assertEqual("jenkins.fast.sandbox.simoncomputing.com", obj['jenkins']['master']['ingress']['hostName'])
        self.assertEqual("jenkins.fast.sandbox.simoncomputing.com", obj['jenkins']['master']['ingress']['tls'][0]['hosts'][0])

    def test_template_loop(self):
        workers = [
            {'subnetId': 'subnet-12341234'},
            {'subnetId': 'subnet-34563456'},
            {'subnetId': 'subnet-34563456'},
        ]

        params = {
            'vpc_type': 'prod',
            'color': 'green',
            'workers': workers
        }

        root = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(root, 'charts')
        env = Environment(loader=FileSystemLoader(templates_dir))

        template = env.get_template("03-worker.yml")
        value = template.render(params)
        self.assertTrue('Worker0' in value)
        self.assertTrue('Worker1' in value)
        self.assertTrue('Worker2' in value)
        self.assertFalse('Worker3' in value)
