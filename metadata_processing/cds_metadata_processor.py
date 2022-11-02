from distutils.command.config import config
from pathlib import Path
import logging
import glob,os
import pandas as pd

class CDSMetadataProcessor():
    EXCEL_FORMAT = "*.xlsx"

    def __init__(self, config):
        logging.info('Instantiating the Metadata Processor Class')
        logging.info(config)
        self.config = config

    def get_file_list(self,extension):
        '''
        This function returns a list of files the files specified in the confif directory with specified extension
        '''
        path=self.config['RAW_FILES_ROOT_DIR']
        matched_files = Path(path).rglob(extension)
        return matched_files

    def get_metadata_files_count(self,extension):
        '''
        This function returns the number of genomic file rows present in the metadata. The format of the files
        to be read is specified in the extension
        '''   
       # Get the list of files to be read for the calculation
        matched_files = self.get_file_list(extension)
        # Create an empty dataframe
        df = pd.DataFrame()
        # If the files have the .xlsx extension, read them in a dataframe with the openpyxl engine
        if extension == self.EXCEL_FORMAT:
            df = pd.concat((pd.read_excel(f,engine='openpyxl') for f in matched_files), ignore_index=True)
        count = len(df.index)
        return count
            