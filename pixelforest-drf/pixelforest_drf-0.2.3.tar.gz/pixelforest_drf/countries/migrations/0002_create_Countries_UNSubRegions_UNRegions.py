# Imports ##############################################################################################################
import csv
import json
import os

from zipfile import ZipFile

from django.db import migrations
from django.conf import settings


# CSV Methods ##########################################################################################################

def get_column_index(header, name):
    """
    Get the column index from the header of the csv
    """
    # Get all the indexes matching the name
    indexes = [idx for idx, key in enumerate(header) if key == name]
    # Raise an error if they are none or multiples
    if not len(indexes):
        raise ValueError("Couldn't find a column named ", name, " in the CSV file")
    if len(indexes) > 1:
        raise ValueError("Found multiple columns named ", name, " in the CSV file")
    # Return the index itself
    return indexes[0]


# Forward and backward functions #######################################################################################

def load_initial_region_data(apps, schema_editor):
    """
    Using migrations_files/countries_objects.csv, create the base countries and default Regions/SubRegions
    """
    # Get the correct versions of models using the app registry
    Region = apps.get_model("countries", "Region")
    SubRegion = apps.get_model("countries", "SubRegion")
    Country = apps.get_model("countries", "Country")

    # Get the Migration Path
    csv_path = os.path.join(os.path.dirname(__file__))
    csv_file = csv_path.replace('migrations', '')
    csv_file = csv_file + 'migrations_files/countries_objects.csv'

    with open(csv_file) as csv_content:
        # Read the csv and skip the header
        reader = csv.reader(csv_content)
        header = next(reader)

        # Verify that we have the correct columns names in the csv and get the index of each one
        reg_col = get_column_index(header, 'region')
        sub_col = get_column_index(header, 'sub-region')
        cnt_col = get_column_index(header, 'name')
        cod_col = get_column_index(header, 'country-code')
        al3_col = get_column_index(header, 'alpha-3')
        al2_col = get_column_index(header, 'alpha-2')

        # Create the elements sets
        regions_names = set()
        subregions_jsons = set()

        # Create the country list
        countries_list = []
        for row in reader:
            regions_names.add(row[reg_col])
            subregions_jsons.add(json.dumps({'name': row[sub_col],
                                             'region_name': row[reg_col]}))
            countries_list.append({'name': row[cnt_col],
                                   'iso_num': row[cod_col],
                                   'iso_alpha_3': row[al3_col],
                                   'iso_alpha_2': row[al2_col],
                                   'sub_region_name': row[sub_col]})

    # Create the regions
    create_regions = [Region(name=name) for name in regions_names if name != ""]
    regions = Region.objects.bulk_create(create_regions)

    # Create a function to get the region from a local cached list of regions using the region name
    def region_from_name(name):
        if name == "":
            return None
        return [region for region in regions if region.name == name][0]

    # Create the SubRegions
    create_subregions = [SubRegion(name=sr['name'],
                                   region=region_from_name(sr['region_name'])) for sr in
                         [json.loads(sr_json) for sr_json in subregions_jsons] if sr['name'] != ""]
    subregions = SubRegion.objects.bulk_create(create_subregions)

    # Create a function to get the sub_region from a local cached list of sub_regions using the sub_region name
    def sub_region_from_name(name):
        if name == "":
            return None
        return [sub_region for sub_region in subregions if sub_region.name == name][0]

    # Create the countries with flags
    flags_dir = Country.flag.field.upload_to
    zip_file = csv_path.replace('migrations', '')
    zip_file = zip_file + 'migrations_files/flags.zip'
    zf = ZipFile(zip_file, 'r')
    zf.extractall(settings.MEDIA_ROOT + '/' + flags_dir)
    zf.close()
    create_countries = [Country(name=c['name'],
                                iso_num=c['iso_num'],
                                iso_alpha_3=c['iso_alpha_3'],
                                iso_alpha_2=c['iso_alpha_2'],
                                sub_region=sub_region_from_name(c['sub_region_name']),
                                flag=(flags_dir + c['iso_alpha_2'] + '.png')) for c in countries_list]
    Country.objects.bulk_create(create_countries)


def remove_initial_region_data(apps, schema_editor):
    """
    Remove all the Countries/Regions/SubRegions that were created by the data migration

    Note: The matching is done by the name. Any object with a name matching the CSV will be deleted.
    """
    # Get the correct versions of models using the app registry
    Region = apps.get_model("countries", "Region")
    SubRegion = apps.get_model("countries", "SubRegion")
    Country = apps.get_model("countries", "Country")

    # Get the Migration Path
    csv_path = os.path.join(os.path.dirname(__file__))
    csv_file = csv_path.replace('migrations', '')
    csv_file = csv_file + 'migrations_files/countries_objects.csv'

    with open(csv_file) as csv_content:
        # Read the csv and skip the header
        reader = csv.reader(csv_content)
        header = next(reader)

        # Verify that we have the correct columns names in the csv and get the index of each one
        reg_col = get_column_index(header, 'region')
        sub_col = get_column_index(header, 'sub-region')
        cnt_col = get_column_index(header, 'name')

        # Get the name of the regions/subregions/countries to remove from the CSV
        region_names = set()
        subregion_names = set()
        country_names = set()
        for row in reader:
            region_names.add(row[reg_col])
            subregion_names.add(row[sub_col])
            country_names.add(row[cnt_col])

        # Delete the objects from the CSV
        Region.objects.filter(name__in=region_names).delete()
        SubRegion.objects.filter(name__in=subregion_names).delete()
        Country.objects.filter(name__in=country_names).delete()


# Migration ############################################################################################################

class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_region_data, remove_initial_region_data)
    ]
