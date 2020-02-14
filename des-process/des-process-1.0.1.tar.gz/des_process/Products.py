#coding: utf-8

import requests

class Products:

  def __init__(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  # Get all products by their product id:
  def get_products_by_process_id(self, process_id):
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
      }
    }""" % process_id


    response = requests.post(self.url, json={ 'query': query })

    products = response.json()['data']['productsByProcessId']

    return products

  # Get product by its product id:
  def get_product_by_product_id(self, product_id):
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
      }
    }""" % product_id

    response = requests.post(self.url, json={ 'query': query })

    product = response.json()['data']['productByProductId']

    return [product]

  # Get product by its display name:
  def get_product_by_display_name(self, display_name):
    query = """{
      productsList(display_name: %s) {
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

          }
        }
      }
    }""" % display_name


    response = requests.post(self.url, json={ 'query': query })

    edges = response.json()['data']['productsList']['edges']

    # Removing unecessary parent node property inside of every process:
    products = list(map(lambda x: x['node'], edges))

    return products
