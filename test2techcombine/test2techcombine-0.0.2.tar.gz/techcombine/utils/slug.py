from django.utils.crypto import get_random_string
from django.utils.text import slugify
from unidecode import unidecode

NUMBER_OF_SLUG = 6

class Slug:
  @staticmethod 
  def generate_unique(obj):
    """ A function to generate a 6 character slug and see if it has been used and contains naughty words."""
    slug = ''
    if not slug: # if there isn't a slug
      slug = get_random_string(NUMBER_OF_SLUG).upper() # create one
      slug_is_wrong = True  
      while slug_is_wrong: # keep checking until we have a valid slug
          slug_is_wrong = False
          other_objs_with_slug = type(obj).objects.filter(slug=slug)
          if len(other_objs_with_slug) > 0:
              # if any other objects have current slug
              slug_is_wrong = True
          if slug_is_wrong:
              # create another slug and check it again
              slug = get_random_string(NUMBER_OF_SLUG).upper()
    return slug

  @staticmethod 
  def generate_unique_from_name(obj, name):
    """ A function to generate a 10 character slug and see if it has been used and contains naughty words."""
    slug = ''
    if not slug: # if there isn't a slug
      slug = Slug.slugify_by_name(name)
      slug_is_wrong = True  
      while slug_is_wrong: # keep checking until we have a valid slug
          slug_is_wrong = False
          other_objs_with_slug = type(obj).objects.filter(slug=slug)
          if len(other_objs_with_slug) > 0:
              # if any other objects have current slug
              slug_is_wrong = True
          if slug_is_wrong:
              # create another slug and check it again
              slug = f'{Slug.slugify_by_name(name)}-{get_random_string(NUMBER_OF_SLUG).upper()}'
    return slug
  
  @staticmethod
  def slugify_by_name(name):
    return slugify(unidecode(name))