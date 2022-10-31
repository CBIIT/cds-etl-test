import logging
import yaml
import argparse
import sys
from graphql_processing.cds_graphql_processor import CDSGraphQLProcessor


parser = argparse.ArgumentParser()
# Add config file argument
parser.add_argument('--config_file', type=str, required=True, help='The name of the config file')
# Add queries file argument
parser.add_argument('--queries_file', type=str, required=True, help='The name of the queries file')
args = parser.parse_args()
config_file = args.config_file
queries_file= args.queries_file

# Load the configuration file
with open(config_file) as f:
    config = yaml.load(f, Loader = yaml.FullLoader)

# Load the queries file
with open(queries_file) as f:
    queries = yaml.load(f, Loader = yaml.FullLoader)


try:
    # Initalize the GraphQL Processor object
    graphql_processor = CDSGraphQLProcessor(config)
    # Query for number of studies
    response=graphql_processor.run_query(queries['STUDIES_QUERY'])
    print(response)
except Exception as e:
    logging.error(e)
    sys.exit(1)
