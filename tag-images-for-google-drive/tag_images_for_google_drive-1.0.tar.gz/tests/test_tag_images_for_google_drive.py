# -*- coding: utf-8 -*-
"""
    Test.
"""
import unittest
from pathlib import Path

from tag_images_for_google_drive.exiftool import ExifTool

# noinspection PyProtectedMember
from tag_images_for_google_drive.tag_images_for_google_drive import _extract_tags, _extract_description_and_tags, \
    tag_images_for_google_drive


class TestTagImages(unittest.TestCase):
    """ Unit test of prepare_dataset.
    """

    def test_extract_description_with_classic_description(self) -> None:  # pylint: disable=R0201
        """ Test build_features() with no data.
        """
        # Given
        description = "The description #tag1 #tag2"

        # When
        description, tags = _extract_tags(description, "#")

        # Then
        self.assertEqual("The description", description)
        self.assertEqual(["tag1", "tag2"], tags)

    def test_extract_description_with_empty_description_and_tags(self) -> None:  # pylint: disable=R0201
        """ Test build_features() with no data.
        """
        # Given
        description = " "

        # When
        description, tags = _extract_tags(description, "#")

        # Then
        self.assertEqual("", description)
        self.assertEqual([], tags)

    def test_extract_description_with_empty_description(self) -> None:  # pylint: disable=R0201
        """ Test build_features() with no data.
        """
        # Given
        description = "#tag1 #tag2 "

        # When
        description, tags = _extract_tags(description, "#")

        # Then
        self.assertEqual("", description)
        self.assertEqual(["tag1", "tag2"], tags)

    def test_extract_description_with_tree_tags1(self) -> None:  # pylint: disable=R0201
        """ Test build_features() with no data.
        """
        # Given
        description = "The description #tag1,tag2 #tag3"

        # When
        description, tags = _extract_tags(description, "#")

        # Then
        self.assertEqual("The description", description)
        self.assertEqual(["tag1", "tag2", "tag3"], tags)

    def test_extract_description_with_tree_tags2(self) -> None:  # pylint: disable=R0201
        """ Test build_features() with no data.
        """
        # Given
        description = "The description #tag1;tag2 #tag3"

        # When
        description, tags = _extract_tags(description, "#")

        # Then
        self.assertEqual("The description", description)
        self.assertEqual(["tag1", "tag2", "tag3"], tags)

    def test_image_without_tags(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_without_tags.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("", description)
            self.assertEqual([], tags)

    def test_image_with_headline(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_Headline.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_imageDescription(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_imageDescription.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_CaptionAbstract(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_CaptionAbstract.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_PNGDescription(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_PNGDescription.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_XMPDescription(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_PNGDescription.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_PNGComment(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_PNGComment.png")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    def test_image_with_FileComment(self):
        with ExifTool() as et:
            # Given
            file = Path("tests/image_with_FileComment.jpg")

            # When
            _, description, tags = _extract_description_and_tags(et, file)

            # Then
            self.assertEqual("Description", description)
            self.assertEqual(["tag1", "tag2"], tags)

    # ----------------------
    def test_empty_csv_with_file_to_update(self):
        # Given
        csvfile = Path("tests/empty.csv")
        pngfile = Path("tests/image_with_PNGDescription.png")

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=[],
                dry=True,
                from_files=False,
                from_db=False,
            )

        # Then file was added in ref_description and file was updated
        self.assertEqual({pngfile: ("Description", ["tag1", "tag2"])}, ref_descriptions)
        self.assertEqual({}, updated_files)

    def test_empty_csv_with_file_not_to_update(self):
        # Given
        csvfile = Path("tests/empty.csv")
        pngfile = Path("tests/image_with_tags.png")

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=[],
                dry=True,
                from_files=False,
                from_db=False,
            )

        # Then file was added in ref_description, but not updated
        self.assertEqual({
            pngfile: ("Description", ["tag1", "tag2"]),
        }, ref_descriptions)
        self.assertEqual({}, updated_files)

    def test_from_db(self):
        # Given
        csvfile = Path("tests/description.csv")
        pngfile = Path("tests/image_with_PNGDescription.png")
        csvfile.touch()

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=[],
                dry=True,
                from_files=False,
                from_db=True,
            )

        # Then
        # Priority of csv
        self.assertEqual({
            Path("tests/image_with_tags.png"): ("Description", ["tag1", "tag2"]),
            Path("tests/image_with_tags2.png"): ("Description", ["csv", "tag1", "tag2"]),
            Path("tests/image_without_tags.png"): ("Description", ["csv", "tag1", "tag2"]),
            pngfile: ("Description", ["tag1", "tag2"]),
        }, ref_descriptions)
        self.assertEqual({
            Path("tests/image_with_tags2.png").absolute(): ("Description", ["csv", "tag1", "tag2"]),
            Path("tests/image_without_tags.png").absolute(): ("Description", ["csv", "tag1", "tag2"]),
        }, updated_files)

    def test_from_file(self):
        # Given
        csvfile = Path("tests/description.csv")
        pngfile = Path("tests/image_with_PNGDescription.png")

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=[],
                dry=True,
                from_files=True,
                from_db=False,
            )

        # Then Priority of file
        self.assertEqual({
            Path("tests/image_with_tags.png"): ("Description", ["tag1", "tag2"]),
            Path("tests/image_with_tags2.png"): ("Description", ["csv", "tag1", "tag2"]),
            Path("tests/image_without_tags.png"): ("Description", ["csv", "tag1", "tag2"]),
            Path("tests/not_a_file.png"): ("Description", ["tag1", "tag2"]),
            pngfile: ("Description", ["tag1", "tag2"])
        }, ref_descriptions)
        self.assertEqual({ }, updated_files)

    def test_merge(self):
        # Given
        csvfile = Path("tests/description.csv")
        pngfile = Path("tests/image_with_tags2.png")
        pngfile.touch()

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=[],
                dry=True,
                from_files=False,
                from_db=False,
            )

        # Then Priority of file
        self.assertEqual({
            Path("tests/image_with_tags.png"): ("Description", ["tag1", "tag2"]),
            pngfile: ("One description", ["csv", "tag1", "tag2"]),
            Path("tests/image_without_tags.png"): ("Description", ["csv", "tag1", "tag2"]),
        }, ref_descriptions)
        self.assertEqual({
            pngfile.absolute(): ("One description", ["csv", "tag1", "tag2"]),
            Path("tests/image_without_tags.png").absolute(): ("Description", ["csv", "tag1", "tag2"]),
        }, updated_files)


    def test_extra_tags(self):
        csvfile = Path("tests/description.csv")
        pngfile = Path("tests/image_with_tags2.png")

        # When
        ref_descriptions, updated_files = \
            tag_images_for_google_drive(
                database=csvfile,
                input_files=[pngfile],
                extra_tags=['mytag'],
                dry=True,
            )

        # Then file was added in ref_description and file was updated
        self.assertEqual({
            Path("tests/image_with_tags.png"): ("Description", ["mytag", "tag1", "tag2"]),
            Path("tests/image_with_tags2.png"): ("One description", ["csv", "mytag", "tag1", "tag2"]),
            Path("tests/image_without_tags.png"): ("Description", ["csv", "mytag", "tag1", "tag2"]),
        }, ref_descriptions)
        self.assertEqual({
            Path("tests/image_with_tags2.png").absolute(): ("One description", ["csv", "mytag", "tag1", "tag2"]),
            Path("tests/image_with_tags.png").absolute(): ("Description", ["mytag", "tag1", "tag2"]),
            Path("tests/image_without_tags.png").absolute(): ("Description", ["csv", "mytag", "tag1", "tag2"]),
        }, updated_files)
