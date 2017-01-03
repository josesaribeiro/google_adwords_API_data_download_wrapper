# google_adwords_API_data_download_wrapper
A python object oriented wrapper for google adwords API to make data consuption easier and cleaner.
Its designed to be used in 2 steps:
- Create and instance of the data downloader class. It receives as optional parameter the locaton of the googleads.yaml configuration file
  if no parameter is sent, it uses the default location(user home directory) 
- Call download_adwords_report senting the parameters : report_name, fields, start_date, end_date, destination_file_path,zip_file

See data_download_example.py as an example of how to use this wrapper.
