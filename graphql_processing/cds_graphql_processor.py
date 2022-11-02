from distutils.command.config import config
import logging
import requests

class CDSGraphQLProcessor():

    HTTP_STATUS_OK = 200
    def __init__(self, config):
        logging.info('Instantiating the GraphQL Processor Class')
        logging.info(config)
        self.config = config

   
    def run_query(self,query): 
        '''
         This function runs the graphl query passed in query and returns the JSON response for valid responses.
         The root URL is read from the config file. If error is received, an exception object is returned
        '''
        graphql_url = self.config['GRAPHQL_URL']
        request = requests.post(graphql_url, json={'query': query})
        if request.status_code == self.HTTP_STATUS_OK:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
