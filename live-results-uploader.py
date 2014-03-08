import requests
from time import sleep
import os.path
from datetime import datetime
import glob
import getpass

class LiveResultsUploader:
    def __init__(self):
       self.results_path = None
       self.user_email = None
       self.user_password = None
       self.event_id = None
       self.needs_user_info = True
       self.last_meos_file_name = None
       self.upload_interval = 5

    def results_url(self):
        return "https://whyjustrun.ca/iof/3.0/events/" + str(self.event_id) + "/live_result_list.xml"

    def prompt_for_user_information(self):
        self.event_id = None
        while (self.event_id is None or self.event_id == 0):
            self.event_id = int(input("Enter the event ID (look for the number in the URL to the event page on WhyJustRun): "))
        self.user_email = input("Enter your WhyJustRun account email: ")
        self.user_password = getpass.getpass("Enter your WhyJustRun account password: ")
        while (self.results_path is None or (self.results_path.lower() != 'meos' and not os.path.isfile(self.results_path))):
            self.results_path = input("Enter the path to the IOF XML 3.0 results list file (if using MeOS, just type \"meos\"): ")

        print("Ok, that's all we need. Now go to the event page to start showing the uploaded results publicly.")

    def upload_results(self):
        f = None
        if (self.results_path.lower() == 'meos'):
            files = glob.glob('[0-9]*[0-9]*[0-9]*[0-9]*.xml')
            if (len(files) == 0):
                print("Error loading results. Didn't find any Meos result files matching format 0123.xml.")
                return
            else:
                sorter = lambda f: int(f.split('.')[0])
                files = sorted(files, key=sorter)
                name = files[-1]
                if not self.last_meos_file_name is None and self.last_meos_file_name == name:
                    return
                self.last_meos_file_name = name
                print("Uploading " + name)
                f = open(name, 'r')
        else:
            f = open(self.results_path, 'r')
        
        results = f.read()
        f.close()
        
        r = requests.post(self.results_url(), data=results, auth=(self.user_email, self.user_password))
        if (r.status_code != requests.codes.ok):
            print("Error uploading results.. Requesting new information.")
            self.needs_user_info = True
        else:
            print("Uploaded results at " + str(datetime.now()) + "!")

    def run(self):
        while True:
            while self.needs_user_info:
                print("We need some information before we can upload results..")
                self.needs_user_info = False
                self.prompt_for_user_information()

            self.upload_results()
            sleep(self.upload_interval)


        

# Prompt the user for the information we need to upload results

def main():
    uploader = LiveResultsUploader()
    uploader.run()

if __name__ == "__main__":
    main()
