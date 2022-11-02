# cds-etl-test
This repository contains code to test CDS data. A comparison is made between the data provided from the metadata with the data provided by the GraphQL endpoint. The code is run using the command
`python cds_etl_main.py --config_file .\config\cds_etl_test_config.yaml --queries_file .\config\cds_etl_test_queries.yaml`

### cds_etl_test_config.yaml
This file stores the configuration variables like the root URL of the commons and location of the raw metadata files.
###  cds_etl_test_queries.yaml: 
This file stores the GraphQL queries which are used for the tests.
