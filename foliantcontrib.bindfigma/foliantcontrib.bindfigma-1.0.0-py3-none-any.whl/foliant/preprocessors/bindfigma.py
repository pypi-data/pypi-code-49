'''
Preprocessor for Foliant documentation authoring tool.
Downloads design layout images from Figma
using its REST API, resizes these images
and binds them with the documentation project.
'''

import re
import json
from pathlib import Path
from hashlib import md5
from subprocess import run, PIPE, STDOUT, CalledProcessError
from urllib import request
from urllib.error import HTTPError
from urllib.parse import quote
from typing import Dict
OptionValue = int or float or bool or str

from foliant.preprocessors.base import BasePreprocessor


class Preprocessor(BasePreprocessor):
    defaults = {
        'cache_dir': Path('.bindfigmacache'),
        'convert_path': 'convert',
        'caption': '',
        'resize': None,
        'access_token': None,
        'file_key': None,
        'ids': None,
        'scale': None,
        'format': None,
        'svg_include_id': None,
        'svg_simplify_stroke': None,
        'use_absolute_bounds': None,
        'version': None
    }

    tags = 'figma',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cache_dir_path = (self.project_path / self.options['cache_dir']).resolve()

        self.logger = self.logger.getChild('bindfigma')

        self.logger.debug(f'Preprocessor inited: {self.__dict__}')

    def _http_request(
        self,
        request_url: str,
        request_method: str = 'GET',
        request_headers: dict or None = None,
        request_data: bytes or None = None
    ) -> dict:
        http_request = request.Request(request_url, method=request_method)

        if request_headers:
            http_request.headers = request_headers

        if request_data:
            http_request.data = request_data

        try:
            with request.urlopen(http_request) as http_response:
                response_status = http_response.getcode()
                response_headers = http_response.info()
                response_data = http_response.read()

        except HTTPError as http_response_not_ok:
            response_status = http_response_not_ok.getcode()
            response_headers = http_response_not_ok.info()
            response_data = http_response_not_ok.read()

        return {
            'status': response_status,
            'headers': response_headers,
            'data': response_data
        }

    def _download_and_resize(self, image_url: str, resized_image_width: str or None, format: str) -> Path or None:
        image_hash = f'{md5(image_url.encode()).hexdigest()}'
        downloaded_image_path = (self._cache_dir_path / f'downloaded_{image_hash}.{format}').resolve()

        self.logger.debug(f'Downloaded image path: {downloaded_image_path}')

        if downloaded_image_path.exists():
            self.logger.debug('Downloaded image found in cache')

        else:
            self.logger.debug(f'Downloading the image, URL: {image_url}')

            download_response = self._http_request(image_url)

            self.logger.debug(f'Response received, status: {download_response["status"]}')
            self.logger.debug(f'Response headers: {download_response["headers"]}')

            if download_response['status'] == 200:
                self._cache_dir_path.mkdir(parents=True, exist_ok=True)

                with open(downloaded_image_path, 'wb') as downloaded_image_file:
                    downloaded_image_file.write(download_response['data'])

                self.logger.debug('Response data written to the file')

            else:
                self.logger.error('Error occured while downloading the image')

                return None

        if resized_image_width and (format == 'png' or format == 'jpg'):
            self.logger.debug(f'Resize needed, image format: {format}, image width: {resized_image_width}')

            resized_image_path = (
                self._cache_dir_path / f'resized_{resized_image_width}_{image_hash}.{format}'
            ).resolve()

            self.logger.debug(f'Resized image path: {resized_image_path}')

            if resized_image_path.exists():
                self.logger.debug('Resized image found in cache')

            else:
                try:
                    self.logger.debug('Performing resize')

                    command = (
                        f'{self.options["convert_path"]} ' +
                        f'"{downloaded_image_path}" ' +
                        f'-resize {resized_image_width} ' +
                        f'"{resized_image_path}"'
                    )

                    run(command, shell=True, check=True, stdout=PIPE, stderr=STDOUT)

                except CalledProcessError as exception:
                    self.logger.error(str(exception))

                    return None

            return resized_image_path

        else:
            self.logger.debug('Do not perform resize')

            return downloaded_image_path

    def _process_figma(self, options: Dict[str, OptionValue]) -> str:
        api_request_params = {}

        for option_name in self.options.keys():
            if option_name in [
                'access_token',
                'file_key',
                'ids',
                'scale',
                'format',
                'svg_include_id',
                'svg_simplify_stroke',
                'use_absolute_bounds',
                'version'
            ]:
                api_request_params[option_name] = options.get(option_name, None) or self.options[option_name]

        self.logger.debug(f'Figma definition found. API request parameters: {api_request_params}')

        if not (
            api_request_params['access_token']
            and
            api_request_params['file_key']
            and
            api_request_params['ids']
        ):
            self.logger.error('Ignoring: access_token, file_key, and ids must be specified')

            return ''

        token_header = {'X-Figma-Token': api_request_params.pop('access_token')}

        api_request_url = 'https://api.figma.com/v1/images/' + api_request_params.pop('file_key')

        if isinstance(api_request_params['ids'], list):
            api_request_params['ids'] = ','.join(api_request_params['ids'])

        api_request_url += '?ids=' + quote(api_request_params.pop('ids'), encoding='utf-8', safe='%')

        for param_name in api_request_params.keys():
            if api_request_params[param_name]:
                api_request_url += f'&{param_name}={api_request_params[param_name]}'

        self.logger.debug(
            f'Calling Figma API to get images URLs, {api_request_url}, custom header: {token_header}'
        )

        api_response = self._http_request(api_request_url, 'GET', token_header)

        api_response_data = json.loads(api_response['data'].decode('utf-8'))

        self.logger.debug(f'Response received, status: {api_response["status"]}')
        self.logger.debug(f'Response headers: {api_response["headers"]}')
        self.logger.debug(f'Response data: {api_response_data}')

        if api_response['status'] != 200 or api_response_data.get('err', None):
            self.logger.error('Error occurred while performing API request')

            return ''

        output = ''

        for index, image_id in enumerate(api_response_data['images'].keys()):
            image_url = api_response_data['images'][image_id]

            self.logger.debug(f'Image ID: {image_id}, image URL: {image_url}')

            if image_url:
                caption = options.get('caption', None)

                if caption is None:
                    caption = self.options['caption']

                caption = caption.replace('{{image_id}}', image_id)

                resized_image_width = options.get('resize', None) or self.options['resize']
                format = options.get('format', None) or self.options['format'] or 'png'

                image_path = self._download_and_resize(image_url, resized_image_width, format)

                if image_path:
                    if index > 0:
                        output += '\n'

                    output += f'![{caption}]({image_path})'

                else:
                    self.logger.error('No path for the image, skipping')

            else:
                self.logger.error('No URL for the image, skipping')

        return output

    def process_figma(self, markdown_content: str) -> str:
        def _sub(figma_definition) -> str:
            return self._process_figma(self.get_options(figma_definition.group('options')))

        return self.pattern.sub(_sub, markdown_content)

    def apply(self):
        self.logger.info('Applying preprocessor')

        for markdown_file_path in self.working_dir.rglob('*.md'):
            self.logger.debug(f'Processing the file: {markdown_file_path}')

            with open(markdown_file_path, encoding='utf8') as markdown_file:
                content = markdown_file.read()

            processed_content = self.process_figma(content)

            if processed_content:
                with open(markdown_file_path, 'w', encoding='utf8') as markdown_file:
                    markdown_file.write(processed_content)

        self.logger.info('Preprocessor applied')
