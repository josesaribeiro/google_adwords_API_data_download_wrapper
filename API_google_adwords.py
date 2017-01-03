# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from googleads import adwords
import gzip

class GoogleAdwordsAPiDataDownloader:
    
    adwords_client=None;
    version="";
    google_ads_yaml_path="";
    
    def __init__(self,version="v201609",google_ads_yaml_path=None):
        self.adwords_client=adwords.AdWordsClient.LoadFromStorage(google_ads_yaml_path);
        self.version = version;
        self.google_ads_yaml_path=google_ads_yaml_path;
        
    def download_adwords_report(self,report_name,fields,dates_constant= None,start_date=None,end_date=None,where_clause="", destination_file_path="report",file_format="CSV",zip_file=False):
    
        report_downloader = self.adwords_client.GetReportDownloader(version=self.version);
        during_clause = "";
        
        report_name = report_name.upper();
        if dates_constant is not None:
            during_clause = ' DURING '+dates_constant;
        elif start_date is not None and end_date is not None:
            during_clause = ' DURING '+start_date+','+end_date;
        else:
            during_clause = ' DURING LAST_7_DAYS';
        
        report_query = ('SELECT '+fields+' FROM '
                            +report_name+" "+where_clause+during_clause);

        if zip_file:
            with gzip.open(destination_file_path+".gz",'w') as output_file:
                report_downloader.DownloadReportWithAwql(report_query,file_format,output_file,skip_report_header=True,
                skip_column_header=False, skip_report_summary=True)
        else:
            with open(destination_file_path,'w') as output_file:
                report_downloader.DownloadReportWithAwql(report_query,file_format,output_file,skip_report_header=True,
                skip_column_header=False, skip_report_summary=True);
