from edc_reference import ReferenceModelConfig, site_reference_configs


def register_to_site_reference_configs():

    site_reference_configs.registry = {}

    reference = ReferenceModelConfig(
        name="edc_metadata_rules.CrfOne", fields=["f1", "f2", "f3"]
    )
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfTwo", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfThree", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfFour", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfFive", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfSix", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="edc_metadata_rules.CrfSeven", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(
        name="edc_metadata_rules.CrfMissingManager", fields=["f1"]
    )
    site_reference_configs.register(reference)
