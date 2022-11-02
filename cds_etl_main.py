import logging
import yaml
import argparse
import sys
from graphql_processing.cds_graphql_processor import CDSGraphQLProcessor
from metadata_processing.cds_metadata_processor import CDSMetadataProcessor

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
    # Testing for Navbar items first
    graphql_processor = CDSGraphQLProcessor(config)
    # Query for number of studies
    total_num_studies_graphql=graphql_processor.run_query(queries['NUM_STUDIES_QUERY'])
    # Query for number of files
    total_num_files_graphql=graphql_processor.run_query(queries['NUM_FILES_QUERY'])
    # Query for number of samples
    total_num_samples_graphql=graphql_processor.run_query(queries['NUM_SAMPLES_QUERY'])

    # Initalize the Metadata Processor object
    metadata_processor = CDSMetadataProcessor(config)
    # Calculate the number of "files" specified in the metadata
    number_of_files_metadata = metadata_processor.get_metadata_files_count('*.xlsx')
    print(number_of_files_metadata)
except Exception as e:
    logging.error(e)
    sys.exit(1)
