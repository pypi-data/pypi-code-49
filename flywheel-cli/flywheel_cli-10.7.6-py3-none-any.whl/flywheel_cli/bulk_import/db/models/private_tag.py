"""Provides the PrivateTag class."""


class PrivateTag:

    """Represents a private tag entry.

    Attributes:
        ingest_id (int): The id of the ingest operation this belongs to.
        private_creator (str): Private creator
        tag (str): Dicom tag.
        vr (str): Value Representation.
        description (str): Description.
        vm (str):  Value Multiplicity.
    """

    def __init__(self, ingest_id=None, private_creator=None, tag=None, vr=None,
                 description=None, vm=None):
        self.ingest_id = ingest_id
        self.private_creator = private_creator
        self.tag = tag
        self.vr = vr  # pylint: disable=invalid-name
        self.description = description
        self.vm = vm  # pylint: disable=invalid-name

    @staticmethod
    def map_field(_, value):
        """Convert from object to map for serialization"""
        return value

    @staticmethod
    def from_map(kwargs):
        """Deserialize kwargs into PrivateTag

        Args:
            kwargs (dict): The constructor arguments

        Returns:
            PrivateTag: The deserialized ingest item
        """
        result = PrivateTag(**kwargs)
        return result

    def __repr__(self):
        return f"PrivateTag(ingest_id={self.ingest_id},tag={self.tag})"
