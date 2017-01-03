# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from googleads import adwords
import gzip
from API_google_adwords import APIGoogleAdwords
import sys
import logging
logging.basicConfig()
        
if __name__ == '__main__':

    report_name = sys.argv[1];
    data_fields =  sys.argv[2];
    start_date = sys.argv[3];
    end_date  = sys.argv[4];
    destination_file_path = sys.argv[5];
    
    adwords = GoogleAdwordsAPiDataDownloader(google_ads_yaml_path="googleads.yaml");

    adwords.download_adwords_report(report_name=report_name,
        fields=data_fields,start_date=start_date,end_date=end_date, 
        destination_file_path=destination_file_path,zip_file=True);
