import io
import json
import os
import re
import requests

from bs4 import BeautifulSoup

from seeq.sdk import *
from seeq import spy

from . import _item

from .. import _common
from .. import _config
from .. import _login


class Annotation:
    def __init__(self, worksheet, annotation_type):
        """
        :type worksheet: Worksheet
        """
        self.annotation_type = annotation_type
        self.worksheet = worksheet
        self._html = ''
        self.images = dict()
        self.plots_to_render = set()
        self.id = _common.new_placeholder_guid()

    def refresh_from(self, new_item):
        self.annotation_type = new_item.annotation_type
        # Note that we purposefully don't touch the worksheet reference, since it will have stayed the same
        self.html = new_item.html
        self.images = new_item.images

    def _find_image_references(self):
        if not self.html:
            return list()

        matches = re.finditer(r'src="/api(/annotations/(.*?)/images/(.*?))"', self.html)
        return [(match.group(1), match.group(2), match.group(3)) for match in matches]

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._set_html(value)

    def _set_html(self, value):
        if value is None:
            self._html = ''
        else:
            self._html = value

    @property
    def referenced_items(self):
        return list()

    @property
    def referenced_worksteps(self):
        return self._find_workstep_references()

    def _find_workstep_references(self):
        return set()

    def find_workbook_links(self):
        if not self.html:
            return dict()

        url = _common.get(self.worksheet.workbook, 'Original Server URL')
        if not url:
            return dict()

        # TODO can this be converted to use the _common.workbook_worksheet_url_regex methods?
        edit_link_no_folder_regex = \
            r'%s/workbook/(?P<workbook>%s)/worksheet/(?P<worksheet>%s)' % (url,
                                                                           _common.GUID_REGEX,
                                                                           _common.GUID_REGEX)

        edit_link_with_folder_regex = \
            r'%s/%s/workbook/(?P<workbook>%s)/worksheet/(?P<worksheet>%s)' % (url,
                                                                              _common.GUID_REGEX,
                                                                              _common.GUID_REGEX,
                                                                              _common.GUID_REGEX)

        view_link_regex = \
            r'%s/view/(?P<worksheet>%s)' % (url, _common.GUID_REGEX)

        present_link_regex = \
            r'%s/present/worksheet/(?P<workbook>%s)/(?P<worksheet>%s)' % (url,
                                                                          _common.GUID_REGEX,
                                                                          _common.GUID_REGEX)

        workstep_tuples = dict()
        for regex in [edit_link_no_folder_regex, edit_link_with_folder_regex, view_link_regex, present_link_regex]:
            matches = re.finditer(regex, self.html, re.IGNORECASE)

            for match in matches:
                group_dict = dict(match.groupdict())
                if 'workbook' not in group_dict:
                    items_api = ItemsApi(_login.client)
                    item_output = items_api.get_item_and_all_properties(
                        id=group_dict['worksheet'])  # type: ItemOutputV1
                    href_regex = r'/workbooks/(?P<workbook>%s)/worksheets/(?P<worksheet>%s)' % (_common.GUID_REGEX,
                                                                                                _common.GUID_REGEX)
                    group_dict['workbook'] = re.fullmatch(href_regex, item_output.href).group('workbook')

                if group_dict['workbook'].upper() not in workstep_tuples:
                    workstep_tuples[group_dict['workbook'].upper()] = set()

                workstep_tuples[group_dict['workbook'].upper()].add(
                    (group_dict['workbook'].upper(), group_dict['worksheet'].upper(), None))

        return workstep_tuples

    def pull(self):
        self.images = dict()
        annotations_api = AnnotationsApi(_login.client)
        annotations = annotations_api.get_annotations(
            annotates=[self.worksheet.id])  # type: AnnotationListOutputV1

        for annotation_item in annotations.items:  # type: AnnotationOutputV1
            annotation_output = annotations_api.get_annotation(id=annotation_item.id)  # AnnotationOutputV1
            if annotation_output.type != self.annotation_type:
                continue

            self.id = annotation_output.id
            self._set_html(annotation_output.document)

            image_references = self._find_image_references()
            for query_params, annotation_id, image_id in image_references:
                if (annotation_id, image_id) in self.images:
                    continue

                self.worksheet.workbook.update_status('Pulling image', 1)

                api_client_url = _config.get_api_url()
                request_url = api_client_url + query_params
                response = requests.get(request_url, headers={
                    "Accept": "application/vnd.seeq.v1+json",
                    "x-sq-auth": _login.client.auth_token
                }, verify=_login.https_verify_ssl)

                self.images[(annotation_id, image_id)] = response.content

    def push(self, pushed_workbook_id, pushed_worksheet_id, item_map, push_images):
        self.render_plots()

        annotations_api = AnnotationsApi(_login.client)

        annotations = annotations_api.get_annotations(
            annotates=[pushed_worksheet_id])  # type: AnnotationListOutputV1

        bs = BeautifulSoup(self.html, features='html.parser')
        find_result = bs.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title'])
        name = 'Unnamed'
        description = None

        if len(find_result) > 0:
            name = ' '.join(re.split(r'[\s\n]+', find_result[0].get_text().strip())[:20])
        if len(find_result) > 1:
            description = ' '.join(re.split(r'[\s\n]+', find_result[1].get_text().strip())[:50])

        new_annotation = AnnotationInputV1()
        new_annotation.document = ''
        new_annotation.name = name if len(name.strip()) > 0 else 'Unnamed'
        new_annotation.description = description
        new_annotation.type = self.annotation_type

        relevant_annotations = [a for a in annotations.items if a.type == self.annotation_type]
        if len(relevant_annotations) == 0:
            new_annotation.interests = [
                AnnotationInterestInputV1(interest_id=pushed_worksheet_id)
            ]

            if isinstance(self, Journal):
                # Reports cannot have an interest to the workbook, see CRAB-18738
                new_annotation.interests.append(AnnotationInterestInputV1(interest_id=pushed_workbook_id))

            relevant_annotation = annotations_api.create_annotation(body=new_annotation)  # type: AnnotationOutputV1
        else:
            relevant_annotation = relevant_annotations[0]

        if push_images:
            for query_params, annotation_id, image_id in self._find_image_references():
                api_client_url = _config.get_api_url()
                request_url = api_client_url + '/annotations/%s/images' % relevant_annotation.id

                self.worksheet.workbook.update_status('Pushing image', 1)

                response = requests.post(url=request_url,
                                         files={
                                             "file": (image_id, io.BytesIO(self.images[(annotation_id, image_id)]))
                                         },
                                         headers={
                                             "Accept": "application/vnd.seeq.v1+json",
                                             "x-sq-auth": _login.client.auth_token
                                         },
                                         verify=_login.https_verify_ssl)

                if response.status_code != 201:
                    raise RuntimeError(
                        'Could not upload image file %s for worksheet %d' % (image_id, pushed_worksheet_id))

                link_json = json.loads(response.content)

                item_map['src="/api/annotations/%s/images/%s"' % (annotation_id, image_id)] = \
                    'src="%s"' % link_json['link']

        doc = self.html

        # When a workbook is duplicated via the Workbench UI, the workstep links within Journals actually refer to
        # the original workbook. This works in the UI because workstep content has no real dependency on the
        # workbook/worksheet they're associated with. When pulling, we accommodate this by pulling a Workstep and
        # associating it with the "proper" Worksheet object, but then during push we have to fix up the links in case
        # the "original" workbook/worksheet wasn't included in the workbooks to be pushed.
        workstep_map = _common.get(item_map, self.worksheet.item_map_worksteps_key())
        if workstep_map:
            doc = _item.replace_items(doc, workstep_map)

        doc = _item.replace_items(doc, item_map)

        worksheet_link_replacement = r'links?type=workstep&amp;workbook=%s&amp;worksheet=%s&amp;' % (
            pushed_workbook_id, pushed_worksheet_id
        )

        doc = re.sub(_common.WORKSHEET_LINK_REGEX, worksheet_link_replacement, doc, flags=re.IGNORECASE)

        original_server_url = _common.get(self.worksheet.workbook, 'Original Server URL')
        new_server_url = _item.get_canonical_server_url()
        if len(doc) > 0 and original_server_url:
            doc = doc.replace(original_server_url, new_server_url)

        new_annotation.document = doc
        new_annotation.interests = list()
        for interest in relevant_annotation.interests:  # type: AnnotationInterestOutputV1
            interest_item = interest.item  # type: ItemPreviewV1
            # At Chevron, we encountered a case where there were multiple interests returned with the same ID, which
            # caused Appserver to choke when updating the annotation. So filter those out.
            if any(interest_item.id == i.interest_id for i in new_annotation.interests):
                continue
            if isinstance(self, Report) and interest_item.id == pushed_workbook_id:
                # Reports cannot have an interest to the workbook, see CRAB-18738
                continue
            new_interest = AnnotationInterestInputV1()
            new_interest.interest_id = interest_item.id
            new_interest.detail_id = interest.capsule
            new_annotation.interests.append(new_interest)
        new_annotation.created_by_id = relevant_annotation.created_by.id

        return annotations_api.update_annotation(
            id=relevant_annotation.id, body=new_annotation)  # type: AnnotationOutputV1

    def _get_annotation_html_file(self, workbook_folder):
        return os.path.join(workbook_folder, '%s_%s.html' % (self.annotation_type, self.worksheet.id))

    @staticmethod
    def _get_image_file(workbook_folder, image_id_tuple):
        return os.path.join(workbook_folder, 'Image_%s_%s' % image_id_tuple)

    @staticmethod
    def _get_html_attr(fragment, attribute):
        attr_match = re.findall(r'\s+%s="(.*?)"' % attribute, fragment)
        return attr_match[0] if len(attr_match) > 0 else None

    def save(self, workbook_folder):
        self.render_plots()
        journal_html_file = self._get_annotation_html_file(workbook_folder)
        with open(journal_html_file, 'w', encoding='utf-8') as f:
            if self.html:
                if _item.options.pretty_print_html:
                    html_to_save = BeautifulSoup(self.html, features='html.parser').prettify()
                    # If we don't trim the spaces within <a> tags, you'll get extra spaces underlined in the UI
                    html_to_save = re.sub(r'(<a .*?>)[\s\n]+(.*?)[\s\n]+(</a>)', r'\1\2\3', html_to_save)
                else:
                    html_to_save = self.html

                f.write(html_to_save)

        for image_id_tuple, content in self.images.items():
            image_file = Journal._get_image_file(workbook_folder, image_id_tuple)
            with open(image_file, 'wb') as f:
                f.write(content)

    def _load(self, workbook_folder):
        journal_html_file = self._get_annotation_html_file(workbook_folder)

        with open(journal_html_file, 'r', encoding='utf-8') as f:
            self.html = f.read()

        matches = re.finditer(r'src="/api(/annotations/(.*?)/images/(.*?))"', self.html)
        for match in matches:
            image_id_tuple = (match.group(2), match.group(3))
            image_file = Journal._get_image_file(workbook_folder, image_id_tuple)

            with open(image_file, 'rb') as f:
                self.images[image_id_tuple] = f.read()

    def add_image(self, *, filename=None, buffer=None, image_format=None, placement=None, just_src=False):
        """
        Add an image to the annotation.

        Parameters
        ----------
        filename: str
            The full path to the image file
        buffer: str
            The bytes of the image in memory (must also specify image_format)
        image_format
            The image format of what is supplied in bytes (e.g. 'png', 'jpg')
        placement : {'end', 'beginning', None}, default None
            The location to add the image to an existing document.
        just_src : bool
            False if full <img> html tags desired, True if you just want the
            url to put in the <img src="<url>"> attribute yourself.
        """
        if filename and buffer:
            raise ValueError('Either filename or buffer must be supplied to image function -- not both')

        if buffer and not image_format:
            raise ValueError('image_format must be specified if buffer is supplied')

        if placement not in ['end', 'beginning', None]:
            raise ValueError(f"placement must be one of {['end', 'beginning', None]}")

        if placement and just_src:
            raise ValueError(f"placement must None if just_src is True")

        html = self.html
        if filename:
            image_name = os.path.basename(filename)
            with open(filename, 'rb') as img:
                self.images[(self.id, image_name)] = img.read()
        else:
            image_name = f'{_common.new_placeholder_guid()}.{image_format}'
            self.images[(self.id, image_name)] = buffer

        url = f'/api/annotations/{self.id}/images/{image_name}'
        if just_src:
            return url

        image_html = f'<img class="fr-fic fr-fin fr-dii" src="{url}">'
        if placement is not None:
            if placement == 'beginning':
                html = image_html + html
            else:
                html += image_html
            self._set_html(html)

        return image_html

    def add_plot_to_render(self, plot_render_info, date_range):
        image_id = _common.new_placeholder_guid()
        filename = f'{image_id}.{plot_render_info.image_format}'
        self.plots_to_render.add((self.id, filename, plot_render_info, date_range))
        return f'<img class="fr-fic fr-fin fr-dii" src="/api/annotations/{self.id}/images/{filename}"/>'

    def render_plots(self):
        for annotation_id, filename, plot_render_info, date_range in self.plots_to_render:
            self.images[annotation_id, filename] = plot_render_info.render_function(date_range)

        self.plots_to_render.clear()


class Journal(Annotation):
    def __init__(self, worksheet):
        super().__init__(worksheet, 'Journal')

    @staticmethod
    def load(worksheet, workbook_folder):
        journal = Journal(worksheet)
        journal._load(workbook_folder)
        return journal

    @property
    def referenced_items(self):
        referenced_items = list()
        if self.html:
            matches = re.finditer(r'item%s(%s)' % (_common.HTML_EQUALS_REGEX, _common.GUID_REGEX), self.html,
                                  re.IGNORECASE)
            for match in matches:
                referenced_items.append(_item.Reference(match.group(1).upper(), _item.Reference.JOURNAL,
                                                        self.worksheet))

        return referenced_items

    def _find_workstep_references(self):
        if not self.html:
            return set()

        workstep_references = set()
        regex = r'workbook%s(%s)&amp;worksheet%s(%s)&amp;workstep%s(%s)' % (
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX,
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX,
            _common.HTML_EQUALS_REGEX, _common.GUID_REGEX)
        matches = re.finditer(regex, self.html, re.IGNORECASE)

        for match in matches:
            workstep_references.add((match.group(1).upper(), match.group(2).upper(), match.group(3).upper()))

        return workstep_references


class Report(Annotation):
    def __init__(self, worksheet):
        super().__init__(worksheet, 'Report')

    @staticmethod
    def load(worksheet, workbook_folder):
        report = Report(worksheet)
        report._load(workbook_folder)
        return report

    def _find_workstep_references(self):
        if not self.html:
            return set()

        workstep_references = set()
        link_matches = re.finditer(r'<a .*?</a>', self.html, re.IGNORECASE)
        for link_match in link_matches:
            link_html = link_match.group(0)
            href_regex = r'.*href="\/view\/worksheet\/(%s)\/(%s)\?workstepId%s(%s).*?".*' % (
                _common.GUID_REGEX, _common.GUID_REGEX, _common.HTML_EQUALS_REGEX, _common.GUID_REGEX)
            href_match = re.match(href_regex, link_html)
            if href_match:
                workstep_references.add((href_match.group(1).upper(),
                                         href_match.group(2).upper(),
                                         href_match.group(3).upper()))

        img_matches = re.finditer(r'<img .*?>', self.html, re.IGNORECASE)
        for img_match in img_matches:
            img_html = img_match.group(0)
            data_seeq_workbookid = Annotation._get_html_attr(img_html, 'data-seeq-workbookid')
            data_seeq_worksheetid = Annotation._get_html_attr(img_html, 'data-seeq-worksheetid')
            data_seeq_workstepid = Annotation._get_html_attr(img_html, 'data-seeq-workstepid')
            if data_seeq_workbookid and data_seeq_worksheetid and data_seeq_workstepid:
                workstep_references.add((data_seeq_workbookid.upper(),
                                         data_seeq_worksheetid.upper(),
                                         data_seeq_workstepid.upper()))

        return workstep_references
