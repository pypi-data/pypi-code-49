#coding: utf-8

import requests

class Processes:

  def __init__(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  # Get a list of all processes:
  # @TODO: Results 504. For now, a limit was set to prevent it.
  def get_processes(self):
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

    response = requests.post(self.url, json={ 'query': query })

    edges = response.json()['data']['processesList']['edges']

    # Removing unecessary parent node property inside of every process:
    processes = list(map(lambda x: x['node'], edges))

    return processes


  # Get process by its process id:
  def get_process_by_id(self, process_id):
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

    response = requests.post(self.url, json={ 'query': query })

    process = response.json()['data']['processByProcessId']

    return process