from distutils.command.config import config
import logging
import requests

class CDSGraphQLProcessor():
    def __init__(self, config):
        logging.info('Instantiating the GraphQL Processor Class')
        logging.info(config)
        self.config = config

    def run_query(self,query): # A simple function to use requests.post to make the API call. Note the json= section.
        graphql_url = self.config['GRAPHQL_URL']
        request = requests.post(graphql_url, json={'query': query})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
