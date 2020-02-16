class CertManager:
    def setup(self):
        cmd = [
            '--dns', 'gandiv5', '-d', f'private.{self.domain}', '--email',
            f'{self.email}', 'run'
        ]
        result = self.client.containers.run(
            'goacme/lego',
            command=cmd,
            environment={'GANDIV5_API_KEY': self.meta['dns_api_key']},
            volumes={self.path.absolute(): {
                         'bind': local_path,
                         'mode': 'rw'
                     }},
            auto_remove=True,
            detach=False)
