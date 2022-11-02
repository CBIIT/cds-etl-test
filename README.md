# cds-etl-test
This repository contains code to test CDS data. A comparison is made between the data provided from the metadata with the data provided by the GraphQL endpoint. The code is run using the command
`python cds_etl_main.py --config_file .\config\cds_etl_test_config.yaml --queries_file .\config\cds_etl_test_queries.yaml`

cds_etl_test_config.yaml: Stores the configuration variables
cds_etl_test_queries.yaml: Stores the GraphQL queries