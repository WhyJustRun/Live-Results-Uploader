Live-Results-Uploader
=====================

Python live results upload script

## Requirements

- [Python 3.x](http://www.python.org/download/)
- [Pip](http://www.pip-installer.org/en/latest/installing.html#install-or-upgrade-pip) (comes installed with Python in 3.4 and higher!)
- Requests library for Python 3 (do `pip install requests`)

## Running

For ease of use, copy the python script to the folder where your IOF XML 3.0 results list file is. Change to that directory, and run the script with Python 3:

`python3 live-results-uploader.py`

Follow the prompts to start uploading results data for your event.

## Using with MeOS

***You need to use MeOS 3.1 or newer*** - older versions don't have support for exporting IOF XML 3.0 results lists automatically.

1. Open the Services tab
2. Open "Results On-Line"
3. Change the export format to IOF XML 3.0
4. Uncheck "Compress large files"
5. Check "Save to disk"
6. Choose the folder where the live-results-uploader.py script is. (note: if there are old IOF XML live results files in that folder from a previous event, delete them first)
6. Leave everything else as the default
7. Run `python3 live-results-uploader.py` and follow the steps.
