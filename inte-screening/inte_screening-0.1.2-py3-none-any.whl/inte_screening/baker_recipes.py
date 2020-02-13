from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_constants.constants import YES, NO, FEMALE, BLACK
from edc_reportable.units import MILLIGRAMS_PER_DECILITER, MILLIMOLES_PER_LITER
from edc_utils import get_utcnow
from faker import Faker
from model_bakery.recipe import Recipe

from .models import ScreeningPartOne

fake = Faker()
