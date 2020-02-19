# -*- coding: utf-8 -*-

class VolumeTemplate(object):
	"""
	A template can be created based on a drive and it has the same
	characteristics and holds the same information as the parent drive.
	"""

	def __init__(self, volume_template_label, volume_template_size_mbytes, os_template_architecture):
		self.volume_template_label = volume_template_label;
		self.volume_template_size_mbytes = volume_template_size_mbytes;
		self.os_template_architecture = os_template_architecture;


	"""
	The ID of the volume template.
	"""
	volume_template_id = None;

	"""
	The volume template's label. It is editable and can be used to call API
	functions.
	"""
	volume_template_label = None;

	"""
	The volume template's unique label. Is <volume_template_label>@<user_id>.
	"""
	volume_template_label_unique = None;

	"""
	The volume template's display name.
	"""
	volume_template_display_name = None;

	"""
	Size of the template.
	"""
	volume_template_size_mbytes = None;

	"""
	Wether the template supports booting and running from local disks.
	"""
	volume_template_local_disk_supported = False;

	"""
	Wether the template is an OS template.
	"""
	volume_template_is_os_template = False;

	"""
	A set of all supported methods
	"""
	volume_template_boot_methods_supported = "pxe_iscsi";

	"""
	An arbitrary UTF-8 string which provides a description of the template.
	"""
	volume_template_description = "";

	"""
	Date and time of the template's creation. ISO 8601 timestamp. Example
	format: 2013-11-29T13:00:01Z
	"""
	volume_template_created_timestamp = None;

	"""
	ISO 8601 timestamp which holds the date and time when the VolumeTemplate was
	edited. Example format: 2013-11-29T13:00:01Z.
	"""
	volume_template_updated_timestamp = "0000-00-00T00:00:00Z";

	"""
	User owner ID.
	"""
	user_id = None;

	"""
	OperatingSystem
	"""
	volume_template_operating_system = None;

	"""
	http(s) template base URL.
	"""
	volume_template_repo_url = None;

	"""
	The deprecation status of the volume template.
	"""
	volume_template_deprecation_status = "not_deprecated";

	"""
	The architecture of the OS template.
	"""
	os_template_architecture = None;

	"""
	OSTemplate credentials.
	"""
	os_template_credentials = None;

	"""
	Bootloader used for the local install of OS templates.
	"""
	os_asset_id_bootloader_local_install = None;

	"""
	Bootloader used for the OS boot of OS templates.
	"""
	os_asset_id_bootloader_os_boot = None;

	"""
	List of tags representative for the VolumeTemplate.
	"""
	volume_template_tags = [];

	"""
	The schema type.
	"""
	type = None;
