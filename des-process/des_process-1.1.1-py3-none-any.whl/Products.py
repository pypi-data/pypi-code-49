#coding: utf-8

import requests

class Products:

  def __init__(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  def products(self, parameters=""):
    query = """{
      productsList%s {
        edges {
          node {
            productId
            fileId
            jobId
            tableId
            classId
            flagRemoved
            displayName
            version
            selectedName
            table {
              tableId
              tableName
              schemaName
            }
          }
        }
      }
    }""" % parameters

    response = requests.post(self.url, json={ 'query': query }).json()

    edges = response['data']['productsList']['edges']

    # Removing unecessary parent node property inside of every process:
    products = list(map(lambda x: x['node'], edges))

    return products

  # Get product by its display name:
  def all(self):
    return self.products()

  # Get product by its product id:
  def by_id(self, id):
    query = """{
      productByProductId(productId: %s) {
        productId
        fileId
        jobId
        tableId
        classId
        flagRemoved
        displayName
        version
        selectedName
        table {
          tableId
          tableName
          schemaName
        }
      }
    }""" % id

    response = requests.post(self.url, json={ 'query': query }).json()

    product = response['data']['productByProductId']

    return product

  # Get all products by their product id:
  def by_process_id(self, process_id):
    query = """{
      productsByProcessId(processId: %s) {
        productId
        fileId
        jobId
        tableId
        classId
        flagRemoved
        displayName
        version
        selectedName
        table {
          tableId
          tableName
          schemaName
        }
      }
    }""" % process_id


    response = requests.post(self.url, json={ 'query': query }).json()

    products = response['data']['productsByProcessId']

    return products

  # Get product by its display name:
  def by_name(self, name):
    return self.products('(displayName: "%s")' % name)

  # Get product by its tag id:
  def by_tag_id(self, tag_id):
    return self.products('(tagId: %s)' % tag_id)

  # Get product by its field id:
  def by_field_id(self, field_id):
    return self.products('(fieldId: %s)' % field_id)

  # Get product by its type id:
  def by_type_id(self, type_id):
    return self.products('(typeId: %s)' % type_id)

  # Get product by its class id:
  def by_class_id(self, class_id):
    return self.products('(classId: %s)' % class_id)