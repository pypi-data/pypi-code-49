# Copyright 2019 The Johns Hopkins University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from datetime import timezone
from dateutil.tz import tzlocal
import glob
import hashlib
import json
import os
import requests
import sys
import time

from craedl import cache as sync_cache
from craedl import errors

BUF_SIZE = 104857600
RETRY_MAX = 5
RETRY_SLEEP = 1

def get_numbered_upload(parent, childname):
    """
    If a File/Directory comes back instead of a Directory/File, we know this
    directory was created with the same name as an
    existing file and had a number appended to its name
    like this: 'childname' --> 'childname (1)'.
    We must find the matching directory with the highest
    number and get that as a replacement.

    :param parent: the parent directory
    :type parent: Directory
    :param childname: the name of the new child
    :type childname: string
    """
    match_num = 0
    for c in parent.children:
        if (childname in c['name'] and childname != c['name']):
            num = int(c['name'].replace(childname + ' (', '' ).replace(')', ''))
            if num > match_num:
                match_num = num
    return self.get('%s (%d)' % (childname, match_num))

def hash_directory(path):
    """
    Generate a hash string representing the state of the files in a directory.
    The hash changes if any file is added, removed, or modified on disk.

    :param path: the directory path
    :type path: string
    :returns: a SHA1 hash representation of the files in the directory
    """
    children_hash = hashlib.sha1()
    children = os.scandir(path)
    for child in children:
        basename = os.path.basename(child.path)
        if (basename[0] != '.' and basename[0] != '~'):
            children_hash.update(child.stat().st_mtime.hex().encode('utf-8'))
    return children_hash.hexdigest()

def to_x_bytes(bytes):
    """
    Take a number in bytes and return a human-readable string.

    :param bytes: number in bytes
    :type bytes: int
    :returns: a human-readable string
    """
    x_bytes = bytes
    power = 0
    while x_bytes >= 1000:
        x_bytes = x_bytes * 0.001
        power = power + 3
    if power == 0:
        return '%.0f bytes' % x_bytes
    if power == 3:
        return '%.0f kB' % x_bytes
    if power == 6:
        return '%.0f MB' % x_bytes
    if power == 9:
        return '%.0f GB' % x_bytes
    if power == 12:
        return '%.0f TB' % x_bytes

class Auth():
    """
    This base class handles low-level RESTful API communications. Any class that
    needs to perform RESTful API communications should extend this class.
    """
    base_url = 'https://api.craedl.org/'

    token = None

    if sys.platform == 'win32':
        token_path = os.path.abspath(os.path.join(os.sep, 'Users',
            os.getlogin(), 'AppData', 'Local', 'Craedl', 'craedl'))
    elif sys.platform == 'darwin':
        token_path = os.path.abspath(os.path.join(os.sep, 'Users',
            os.getlogin(), 'Library', 'Preferences', 'Craedl', 'craedl'))
    else:
        token_path = os.path.expanduser('~/.config/Craedl/craedl')

    def __init__(self):
        if not os.path.isfile(os.path.expanduser(self.token_path)):
            raise errors.Missing_Token_Error

    def __repr__(self):
        string = '{'
        for k, v in vars(self).items():
            if k != 'token':
                if type(v) is str:
                    string += "'" + k + "': '" + v + "', "
                else:
                    string += "'" + k + "': " + str(v) + ", "
        if len(string) > 1:
            string = string[:-2]
        string += '}'
        return string

    def GET(self, path):
        """
        Handle a GET request.

        :param path: the RESTful API method path
        :type path: string
        :returns: a dict containing the contents of the parsed JSON response or
            an HTML error string if the response does not have status 200
        """
        if not self.token:
            self.token = open(os.path.expanduser(self.token_path)).readline().strip()
        attempt = 0
        while attempt < RETRY_MAX:
            attempt = attempt + 1
            try:
                response = requests.get(
                    self.base_url + path,
                    headers={'Authorization': 'Bearer %s' % self.token},
                )
                return self.process_response(response)
            except requests.exceptions.ConnectionError:
                time.sleep(RETRY_SLEEP)
        raise errors.Retry_Max_Error

    def POST(self, path, data):
        """
        Handle a POST request.

        :param path: the RESTful API method path
        :type path: string
        :param data: the data to POST to the RESTful API method as described at
            https://api.craedl.org
        :type data: dict
        :returns: a dict containing the contents of the parsed JSON response or
            an HTML error string if the response does not have status 200
        """
        if not self.token:
            self.token = open(os.path.expanduser(self.token_path)).readline().strip()
        attempt = 0
        while attempt < RETRY_MAX:
            attempt = attempt + 1
            try:
                response = requests.post(
                    self.base_url + path,
                    json=data,
                    headers={'Authorization': 'Bearer %s' % self.token},
                )
                return self.process_response(response)
            except requests.exceptions.ConnectionError:
                time.sleep(RETRY_SLEEP)
        raise errors.Retry_Max_Error

    def PUT_DATA(self, path, file_path):
        """
        Handle a data PUT request.

        :param path: the RESTful API method path
        :type path: string
        :param file_path: the data to POST to the RESTful API method as described at
            https://api.craedl.org
        :type file_path: string
        :returns: a dict containing the contents of the parsed JSON response or
            an HTML error string if the response does not have status 200
        """
        if not self.token:
            self.token = open(os.path.expanduser(self.token_path)).readline().strip()
        with open(file_path, 'rb') as data:
            d = data.read(BUF_SIZE)
            if d:
                while d:
                    attempt = 0
                    while attempt < RETRY_MAX:
                        attempt = attempt + 1
                        try:
                            response = requests.put(
                                self.base_url + path,
                                data=d,
                                headers={
                                    'Authorization': 'Bearer %s' % self.token,
                                    'Content-Disposition': 'attachment; filename="craedl-upload"',
                                },
                            )
                            break
                        except requests.exceptions.ConnectionError:
                            time.sleep(RETRY_SLEEP)
                    if attempt >= RETRY_MAX:
                        raise errors.Retry_Max_Error
                    d = data.read(BUF_SIZE)
                return self.process_response(response)
            else: # force request for empty file
                attempt = 0
                while attempt < RETRY_MAX:
                    attempt = attempt + 1
                    try:
                        response = requests.put(
                            self.base_url + path,
                            # no data
                            headers={
                                'Authorization': 'Bearer %s' % self.token,
                                'Content-Disposition': 'attachment; filename="craedl-upload"',
                            },
                        )
                        return self.process_response(response)
                    except requests.exceptions.ConnectionError:
                        time.sleep(RETRY_SLEEP)
                raise errors.Max_Retry_Error

    def GET_DATA(self, path):
        """
        Handle a data GET request.

        :param path: the RESTful API method path
        :type path: string
        :returns: the data stream being downloaded
        """
        if not self.token:
            self.token = open(os.path.expanduser(self.token_path)).readline().strip()
        attempt = 0
        while attempt < RETRY_MAX:
            attempt = attempt + 1
            try:
                response = requests.get(
                    self.base_url + path,
                    headers={'Authorization': 'Bearer %s' % self.token},
                    stream=True,
                )
                return response
            except requests.exceptions.ConnectionError:
                time.sleep(RETRY_SLEEP)
        raise errors.Retry_Max_Error

    def process_response(self, response):
        """
        Process the response from a RESTful API request.

        :param response: the RESTful API response
        :type response: a response object
        :returns: a dict containing the contents of the parsed JSON response or
            an HTML error string if the response does not have status 200
        """
        if response.status_code == 200:
            out = json.loads(response.content.decode('utf-8'))
            if out:
                return out
        elif response.status_code == 400:
            raise errors.Parse_Error(details=response.content.decode('ascii'))
        elif response.status_code == 401:
            raise errors.Invalid_Token_Error
        elif response.status_code == 403:
            raise errors.Unauthorized_Error
        elif response.status_code == 404:
            raise errors.Not_Found_Error
        elif response.status_code == 500:
            raise errors.Server_Error
        else:
            raise errors.Other_Error

class Directory(Auth):
    """
    A Craedl directory object.
    """

    def __init__(self, id):
        super().__init__()
        data = self.GET('directory/' + str(id) + '/info/')['directory']
        for k, v in data.items():
            setattr(self, k, v)

    def __eq__(self, other):
        if not isinstance(other, Directory):
            return NotImplemented
        equal = True
        for i1, i2 in list(zip(vars(self).items(), vars(other).items())):
            if i1[0] != i2[0] or i1[1] != i2[1]:
                equal = False
        return equal

    def create_directory(self, name):
        """
        Create a new directory contained within this directory.

        **Note:** This method returns the updated instance of this directory
        (because it has a new child). The recommended usage is:

        .. code-block:: python

            home = home.create_directory('new-directory-name')

        Use :meth:`Directory.get` to get the new directory.

        :param name: the name of the new directory
        :type name: string
        :returns: the updated instance of this directory
        """
        data = {
            'name': name,
            'parent': self.id,
        }
        response_data = self.POST('directory/', data)
        return Directory(self.id)

    def download(self, save_path, rescan=True, output=False):
        """
        Download the data associated with this directory. This returns the
        active version of all files. It generates a cache database file in the
        `save_path` that is used to enhance performance of retries and
        synchronizations.

        :param save_path: the path to the directory on your computer that will
            contain this file's data
        :type save_path: string
        :param rescan: whether to rescan the directories (defaults to True);
            ignores new children in already transferred directories if False
        :type rescan: boolean
        :param output: whether to print to STDOUT (defaults to False)
        :type output: boolean
        :returns: the updated instance of this directory
        """
        accumulated_size = 0
        save_path = os.path.expanduser(save_path)
        if not os.path.isdir(save_path):
            print('Failure: %s is not a directory.' % save_path)
            exit()

        # create this directory
        save_path = save_path + '/' + self.name
        if output:
            print('CREATE DIR %s/...' % (save_path), end='', flush=True)
        try:
            os.mkdir(save_path)
            if output:
                print('created', flush=True)
        except FileExistsError:
            if os.path.isfile(save_path):
                print('Failure: %s is a file.' % save_path)
            else:
                if output:
                    print('exists', flush=True)
                pass
        cache_path = save_path + '/.craedl-download-cache-%d.db' % (
            self.id
        )
        cache = sync_cache.Cache()
        cache.open(cache_path)

        # begin the recursive download 
        (self, this_size) = self.download_recurse(
            cache,
            save_path,
            rescan,
            output,
            0
        )

        if cache:
            cache.close()

        return self

    def download_recurse(
        self,
        cache,
        save_path,
        rescan,
        output,
        accumulated_size
    ):
        """
        The recursive function that does the downloading. There is little reason
        to call this directly; use :meth:`Directory.download` to start a
        directory download.

        :param cache: the cache database
        :type cache: :py:class:`~craedl.cache.Cache`
        :param save_path: the path to the directory on your computer that will
            contain this file's data
        :type save_path: string
        :param rescan: whether to rescan the directories (defaults to True);
            ignores new children in already transferred directories if False
        :type rescan: boolean
        :param output: whether to print to STDOUT (defaults to False)
        :type output: boolean
        :param accumulated_size: the amount of data that has been downloaded so
            far
        :type: integer
        :returns: a tuple containing the updated instance of this directory and
            the amount of data that has been downloaded by this recursion level
            and its children
        """
        this_size = 0

        do_download = True
        if cache.check(save_path, self.directory_hash):
            # no need to download
            do_download = False
            if not rescan:
                # skip this recursion branch if user requests not to look for
                # changes to already downloaded children
                return (self, this_size)
        else:
            # record the directory hash
            cache.start(save_path, self.directory_hash)

        (dirs, files) = self.list()
        if do_download:
            for f in files:
                # download child files
                (f, new_size) = f.download(
                    save_path,
                    output=output,
                    accumulated_size=accumulated_size + this_size
                )
                this_size = this_size + new_size
        else:
            for f in files:
                # safe to skip this file
                if output:
                    print('SYNCHD FIL %s...skip (%s)' % (
                        save_path + '/' + f.name,
                        to_x_bytes(accumulated_size + this_size)
                    ))

        for d in dirs:
            # recurse into child directories
            if output:
                print('CREATE DIR %s/...' % (save_path + '/' + d.name), end='', flush=True)
            try:
                os.mkdir(save_path + '/' + d.name)
                if output:
                    print('created', flush=True)
            except FileExistsError:
                if os.path.isfile(save_path + '/' + d.name):
                    print('Failure: %s is a file.' % save_path + '/' + d.name)
                else:
                    if output:
                        print('exists', flush=True)
                    pass

            (d, new_size) = d.download_recurse(
                cache,
                save_path + '/' + d.name,
                output=output,
                accumulated_size=accumulated_size + this_size
            )
            this_size = this_size + new_size

        # mark download as completed in cache
        cache.finish(save_path, self.directory_hash)

        return (self, this_size)

    def get(self, path):
        """
        Get a particular directory or file. This can be an absolute or
        relative path.

        :param path: the directory or file path
        :type path: string
        :returns: the requested directory or file
        """
        if not path or path == '.':
            return self
        if path[0] == '/':
            try:
                return Directory(self.parent).get(path)
            except errors.Not_Found_Error:
                while path.startswith('/') or path.startswith('./'):
                    if path.startswith('/'):
                        path = path[1:]  # 1 = len('/')
                    else:
                        path = path[2:]  # 2 = len('./')
                if not path or path == '.':
                    return self
                p = path.split('/')[0]
                if p != self.name:
                    raise FileNotFoundError(p + ': No such file or directory')
                path = path[len(p):]
                if not path:
                    return self
        while path.startswith('/') or path.startswith('./'):
            if path.startswith('/'):
                path = path[1:]  # 1 = len('/')
            else:
                path = path[2:]  # 2 = len('./')
        if not path or path == '.':
            return self
        p = path.split('/')[0]
        if p == '..':
            path = path[2:]  # 2 = len('..')
            while path.startswith('/'):
                path = path[1:]  # 1 = len('/')
            try:
                return Directory(self.parent).get(path)
            except errors.Not_Found_Error:
                raise FileNotFoundError(p + ': No such file or directory')
        for c in self.children:
            if p == c['name']:
                path = path[len(p):]
                while path.startswith('/'):
                    path = path[1:]  # 1 = len('/')
                if path:
                    return Directory(c['id']).get(path)
                else:
                    if c['type'] == 'd':
                        return Directory(c['id'])
                    elif c['type'] == 'f':
                        return File(c['id'])
        raise FileNotFoundError(p + ': No such file or directory')

    def list(self):
        """
        List the contents of this directory.

        :returns: a tuple containing a list of directories and a list of files
        """
        dirs = list()
        files = list()
        for c in self.children:
            if 'd' == c['type']:
                dirs.append(Directory(c['id']))
            else:
                files.append(File(c['id']))
        return (dirs, files)

    def upload_file(self, file_path, output=False, accumulated_size=0):
        """
        Upload a new file contained within this directory.

        **Note:** This method returns the updated instance of this directory
        (because it has a new child). The recommended usage is:

        .. code-block:: python

            home = home.upload_file('/path/on/local/computer/to/read/data')

        Use :meth:`Directory.get` to get the new file.

        :param file_path: the path to the file to be uploaded on your computer
        :type file_path: string
        :param output: whether to print to STDOUT (defaults to False)
        :type output: boolean
        :param accumulated_size: the size that has accumulated prior to this
            upload (defaults to 0); this is entirely for output purposes
        :type accumulated_size: int
        :returns: a tuple with the updated instance of this directory and the
            uploaded size
        """
        file_path = os.path.expanduser(file_path)
        if not os.path.isfile(file_path):
            print('Failure: %s is not a file.' % file_path)
            exit()

        if (os.path.basename(file_path)[0] == '.'
            or os.path.basename(file_path)[0] == '~'
        ):
            if output:
                print('UPLOAD FIL %s...skip' % (file_path), flush=True)
            return (self, 0)

        if output:
            print('UPLOAD FIL %s...' % (file_path), end='', flush=True)
        stream_data = False
        try:
            # check if file exists remotely
            f = self.get(os.path.basename(file_path))
            # check timestamps to determine whether we should stream this data
            local_mtime = os.path.getmtime(file_path)
            remote_mtime = (datetime.fromisoformat(
                f.versions[-1]['upload_date']
            ) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
            if local_mtime > remote_mtime:
                stream_data = True
        except FileNotFoundError:
            stream_data = True
        if stream_data:
            data = {
                'name': file_path.split('/')[-1],
                'parent': self.id,
                'size': os.path.getsize(file_path)
            }
            response_data = self.POST('file/', data)
            response_data2 = self.PUT_DATA(
                'data/%d/?vid=%d' % (
                    response_data['id'],
                    response_data['active_version']
                ),
                file_path
            )
            D = Directory(self.id)
            size = os.path.getsize(file_path)
            if output:
                print('uploaded %s (%s)' % (
                    to_x_bytes(size),
                    to_x_bytes(size + accumulated_size),
                ), flush=True)
            return (D, size)
        else:
            if output:
                print('current (%s)' % to_x_bytes(accumulated_size), flush=True)
            return (self, 0)

    def upload_directory(
        self,
        directory_path,
        rescan=True,
        follow_symlinks=False,
        output=False
    ):
        """
        Upload a new directory contained within this directory. It generates a
        cache database in the `directory_path` that is used to enhance
        performance of retries and synchronizations.

        **Note:** This method returns the updated instance of this directory
        (because it has a new child). The recommended usage is:

        .. code-block:: python

            home = home.upload_directory('/path/on/local/computer/to/read/data')

        Use :meth:`Directory.get` to get the new directory.

        :param directory_path: the path to the directory to be uploaded on your
            computer
        :type directory_path: string
        :param follow_symlinks: whether to follow symlinks (default False)
        :type follow_symlinks: boolean
        :param rescan: whether to rescan the directories (defaults to True);
            ignores new children in already transferred directories if False
        :type rescan: boolean
        :param output: whether to print to STDOUT (defaults to False)
        :type output: boolean
        :returns: the updated instance of this directory
        """
        accumulated_size = 0
        directory_path = os.path.expanduser(directory_path)
        if not os.path.isdir(directory_path):
            print('Failure: %s is not a directory.' % directory_path)
            exit()

        cache_path = directory_path + '/.craedl-upload-cache-%d.db' % (
            self.id
        )
        cache = sync_cache.Cache()
        cache.open(cache_path)

        # begin the recursive upload
        (self, this_size) = self.upload_directory_recurse(
            cache,
            directory_path,
            rescan,
            follow_symlinks,
            output,
            0
        )

        if cache:
            cache.close()

        return self

    def upload_directory_recurse(
        self,
        cache,
        directory_path,
        rescan,
        follow_symlinks,
        output,
        accumulated_size
    ):
        """
        The recursive function that does the uploading. There is little reason
        to call this directly; use :meth:`Directory.upload_directory` to start a
        directory upload.

        :param cache: the cache database
        :type cache: :class:`Cache`
        :param directory_path: the path to the directory on your computer that
            will contain this file's data
        :type directory_path: string
        :param rescan: whether to rescan the directories (defaults to True);
            ignores new children in already transferred directories if False
        :type rescan: boolean
        :param follow_symlinks: whether to follow symlinks
        :type follow_symlinks: boolean
        :param output: whether to print to STDOUT
        :type output: boolean
        :param accumulated_size: the amount of data that has been uploaded so
            far
        :type: integer
        :returns: a tuple containing the updated instance of this directory and
            the amount of data that has been downloaded by this recursion level
            and its children
        """
        this_size = 0

        children = sorted(os.scandir(directory_path), key=lambda d: d.path)

        directory_hash = hash_directory(directory_path)
        do_upload = True
        if cache.check(directory_path, directory_hash):
            # no need to upload
            do_upload = False
            if not rescan:
                # skip this recursion branch if user requests not to look for
                # changes to already uploaded children
                return (self, this_size)
        else:
            # record the directory hash
            cache.start(directory_path, directory_hash)

        # create new directory
        if output:
            print('CREATE DIR %s/...' % (directory_path), end='', flush=True)
        if (os.path.basename(directory_path)[0] == '.'
            or os.path.basename(directory_path)[1] == '~'
        ):
            if output:
                print('skip', flush=True)
            return (self, this_size)

        try:
            new_dir = self.get(os.path.basename(directory_path))
            if output:
                print('exists', flush=True)
        except FileNotFoundError:
            self = self.create_directory(os.path.basename(directory_path))
            new_dir = self.get(os.path.basename(directory_path))
            if output:
                print('created', flush=True)

        for child in children:
            if not follow_symlinks and child.is_symlink():
                # skip this symlink if ignoring symlinks
                if output:
                    print('SKIP SMLNK %s/...done' % (child.path), flush=True)
            elif child.is_file():
                if do_upload:
                    # upload file
                    (new_dir, new_size) = new_dir.upload_file(
                        child.path,
                        output,
                        accumulated_size + this_size
                    )
                    this_size = this_size + new_size
                else:
                    # safe to skip this file
                    if output:
                        print('SYNCHD FIL %s/...skip (%s)' % (
                            child.path,
                            to_x_bytes(accumulated_size + this_size)
                        ))
            else:
                # recurse into this directory
                (new_dir, new_size) = new_dir.upload_directory_recurse(
                    cache,
                    child.path,
                    rescan=rescan,
                    follow_symlinks=follow_symlinks,
                    output=output,
                    accumulated_size=accumulated_size + this_size
                )
                this_size = this_size + new_size

        # mark upload as completed in cache
        cache.finish(directory_path, directory_hash)

        return (self, this_size)

class File(Auth):
    """
    A Craedl file object.
    """

    def __init__(self, id):
        super().__init__()
        data = self.GET('file/' + str(id) + '/')
        for k, v in data.items():
            if k == 'versions':
                v.reverse() # list versions in chronological order
            setattr(self, k, v)

    def download(self,
        save_path,
        version_index=-1,
        output=False,
        accumulated_size=0
    ):
        """
        Download the data associated with this file. This returns the most
        recent version by default.

        :param save_path: the path to the directory on your computer that will
            contain this file's data
        :type save_path: string
        :param version_index: the (optional) index of the version to be
            downloaded; defaults to the most recent version
        :type version_index: int
        :param output: whether to print to STDOUT (defaults to False)
        :type output: boolean
        :param accumulated_size: the size that has accumulated prior to this
            upload (defaults to 0); this is entirely for output purposes
        :type accumulated_size: int
        :returns: a tuple containing this file and the size downloaded
        """
        this_size = 0
        save_path = os.path.expanduser(save_path)
        if output:
            print('DOWNLD FIL %s...' % (save_path + '/' + self.name),
                end='',
                flush=True
            )

        # check timestamps to determine whether we should stream this data
        stream_data = True
        if os.path.isfile(save_path + '/' + self.name):
            local_mtime = os.path.getmtime(save_path + '/' + self.name)
            remote_mtime = (datetime.fromisoformat(
                self.versions[version_index]['upload_date']
            ) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
            if local_mtime > remote_mtime:
                stream_data = False
        if stream_data: # stream the data only if remote is newer than local
            data = self.GET_DATA('data/%d/?vid=%d' % (
                self.id, self.versions[version_index]['id']
            ))
            try:
                f = open(save_path, 'wb')
            except IsADirectoryError:
                f = open(save_path + '/' + self.name, 'wb')
            for chunk in data.iter_content():
                # because we are using iter_content and GET_DATA uses stream=True
                # in the request, the data is not read into memory but written
                # directly from the stream here
                f.write(chunk)
            f.close()
            size = self.versions[version_index]['size']
            if output:
                print('downloaded %s (%s)' % (
                    to_x_bytes(size),
                    to_x_bytes(size + accumulated_size)
                ), flush=True)
            return (self, size)
        else:
            if output:
                print('current (%s)' % to_x_bytes(accumulated_size), flush=True)
            return (self, 0)

class Profile(Auth):
    """
    A Craedl profile object.
    """

    def __init__(self, data=None, id=None):
        super().__init__()
        if not data and not id:
            data = self.GET('profile/whoami/')
        elif not data:
            data = self.GET('profile/' + str(id) + '/')
        for k, v in data.items():
            setattr(self, k, v)

    def create_project(self, name):
        """
        Create a new project belonging to this profile.

        Use :meth:`Profile.get_project` to get the new project.

        :param name: the name of the new project
        :type name: string
        :returns: this profile
        """
        data = {
            'name': name,
            'research_group': '',
        }
        response_data = self.POST('project/', data)
        return self

    def get_project(self, name):
        """
        Get a particular project that belongs to this profile.

        :param name: the name of the project
        :type name: string
        :returns: a project
        """
        projects = self.get_projects()
        for project in projects:
            if project.name == name:
                return project
        raise errors.Not_Found_Error

    def get_projects(self):
        """
        Get a list of projects that belong to this profile.

        :returns: a list of projects
        """
        data = self.GET('profile/' + str(self.id) + '/projects/')
        projects = list()
        for project in data:
            projects.append(Project(project['id']))
        return projects

    def get_publications(self):
        """
        Get a list of publications that belongs to this profile.

        :returns: a list of publications
        """
        data = self.GET('profile/' + str(self.id) + '/publications/')
        publications = list()
        for publication in data:
            publications.append(Publication(publication))
        return publications

    def get_research_group(self, slug):
        """
        Get a particular research group.

        :param slug: the unique slug in this research group's URL
        :type slug: string
        :returns: a research group
        """
        return Research_Group(slug)

    def get_research_groups(self):
        """
        Get a list of research groups that this profile belongs to.

        :returns: a list of research groups
        """
        data = self.GET('research_group/')
        research_groups = list()
        for research_group in data:
            research_groups.append(Research_Group(research_group['slug']))
        return research_groups

class Project(Auth):
    """
    A Craedl project object.
    """

    def __init__(self, id):
        super().__init__()
        data = self.GET('project/' + str(id) + '/')
        for k, v in data.items():
            if not (type(v) is dict or type(v) is list):
                if not v == None:
                    setattr(self, k, v)

    def get_data(self):
        """
        Get the data attached to this project. It always begins at the home
        directory.

        :returns: this project's home directory
        """
        d = Directory(self.root)
        return d

    def get_publications(self):
        """
        Get a list of publications attached to this project.

        :returns: a list of this project's publications
        """
        data = self.GET('project/' + str(self.id) + '/publications/')
        publications = list()
        for publication in data:
            publications.append(Publication(publication))
        return publications

class Publication(Auth):
    """
    A Craedl publication object.
    """

    authors = list()

    def __init__(self, data=None, id=None):
        self.authors = list()
        super().__init__()
        if not data:
            data = self.GET('publication/' + str(id) + '/')
        for k, v in data.items():
            if k == 'authors':
                for author in v:
                    self.authors.append(Profile(author))
            else:
                if not v == None:
                    setattr(self, k, v)

class Research_Group(Auth):
    """
    A Craedl research group object.
    """

    def __init__(self, id):
        super().__init__()
        data = self.GET('research_group/' + str(id) + '/')
        for k, v in data.items():
            if not (type(v) is dict or type(v) is list):
                if not v == None:
                    setattr(self, k, v)

    def create_project(self, name):
        """
        Create a new project belonging to this research group.

        Use :meth:`Research_Group.get_project` to get the new project.

        :param name: the name of the new project
        :type name: string
        :returns: this research group
        """
        data = {
            'name': name,
            'research_group': self.pk,
        }
        response_data = self.POST('project/', data)
        return self

    def get_project(self, name):
        """
        Get a particular project that belongs to this research group.

        :param name: the name of the project
        :type name: string
        :returns: a project
        """
        projects = self.get_projects()
        for project in projects:
            if project.name == name:
                return project
        raise errors.Not_Found_Error

    def get_projects(self):
        """
        Get a list of projects that belong to this research group.

        :returns: a list of projects
        """
        data = self.GET('research_group/' + self.slug + '/projects/')
        projects = list()
        for project in data:
            projects.append(Project(project['id']))
        return projects

    def get_publications(self):
        """
        Get a list of publications that belong to this research group.

        :returns: a list of publications
        """
        data = self.GET('research_group/' + self.slug + '/publications/')
        publications = list()
        for publication in data:
            publications.append(Publication(publication))
        return publications
