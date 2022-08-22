# QRadar API Client written in Python

This is a wrapper around the REST-API of QRadar. This includes some undocumented endpoints, that may not work as expected.  
All the information for the various endpoints were pulled from version `15.1`.  
If you find any bugs please open an issue or a pull request. 

## A word of warning

qradar4py is work in progress and should be treated as a software in beta, especially regarding the "undocumented" API endpoints.

## Installation
```bash
sudo pip3 install qradar4py
# OR
cd qradar4py && sudo python3 setup.py install
```

## Usage

Just a very basic sample on how to get the IDs of up to 10 offenses that are not closed.

```python
from qradar4py.api import QRadarApi

# Initalize the API with the URL, your API token and whether the certificate should be checked.
api = QRadarApi("<URL>", "<API_TOKEN>", version='13.1', verify=True)
# Get all offenses
status_code, response = api.siem.get_offenses(filter='status != CLOSED', 
                                              Range='items=0-50', 
                                              fields='id')

print(status_code, response)
# 200 [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}]

```

## Mapping

Check the "Interactive API" on QRadar to see what endpoints are available in your version.  
Check the [documentation](documentation.md) to get a mapping from endpoint to method.

### Disclaimer

I am in no way affiliated with IBM.  
QRadar is a registered trademark by IBM.
