#coding: utf-8

import requests

# API URL:
url = "http://scienceportal-dev.linea.gov.br/api/graphql"

# Get a list of all processes:
# @TODO: Results 504. For now, a limit was set to prevent it.
def processes():
  query = """{
    processesList {
      edges {
        node {
          processId
          startTime
          endTime
          name
          productLog
          processDir
          size
          processStatus {
            displayName
          }
        }
      }
    }
  }"""

  response = requests.post(url, json={ 'query': query })

  edges = response.json()['data']['processesList']['edges']

  # Removing unecessary parent node property inside of every process:
  processes = list(map(lambda x: x['node'], edges))

  return processes


# Get process by its process id:
def process_by_process_id(process_id):
  query = """{
    processByProcessId(processId: %s) {
      processId
      startTime
      endTime
      name
      productLog
      processDir
      size
      processStatus {
        displayName
      }
    }
  }""" % process_id

  response = requests.post(url, json={ 'query': query })

  process = response.json()['data']['processByProcessId']

  return [process]

# Get all products by their product id:
def products_by_process_id(process_id):
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


  response = requests.post(url, json={ 'query': query })

  products = response.json()['data']['productsByProcessId']

  return products

# Get product by its product id:
def product_by_product_id(product_id):
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

  response = requests.post(url, json={ 'query': query })

  product = response.json()['data']['productByProductId']

  return [product]

print(process_by_process_id(10011357))