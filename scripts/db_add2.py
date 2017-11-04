import requests
import json

import csv

from key import key


FILE = '../data/data.csv'

BASE_URL = 'https://hoot-mentor.appspot.com'
DB_ADD_URL = '%s/_ah/api/jobSearch/v1/jobSearch/dbAddNoc' % BASE_URL

def gather_data():
    with open(FILE) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        return [{
                    'noc': x[0],
                    'title': x[1]
                }
                for x in readCSV
        ]

def main():
    data = gather_data()
    print('Found %i data points' % (len(data,)))
    mutable_data = {
        'content': json.dumps({
            'password': key,
            'data': data
        })
    }

    request = requests.post(DB_ADD_URL, data=mutable_data)

    print(request.status_code)
    print(request.content)

if __name__ == "__main__":
    main()