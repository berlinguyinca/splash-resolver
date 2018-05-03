#!/usr/bin/env python

from __future__ import print_function
import argparse
import requests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='number of spectra to upload')
    args = parser.parse_args()

    size = 25
    page = 1

    while (page - 1) * size < args.n:
        # Get page of data from MoNA
        data = requests.get('http://mona.fiehnlab.ucdavis.edu/rest/spectra?size=%d&page=%d' % (size, page)).json()

        for spectrum in data:
            # Extract all InChIKeys
            compound_metadata = sum([x['metaData'] for x in spectrum['compound']], [])
            inchikeys = set(x['value'] for x in compound_metadata if x['name'] == 'InChIKey')

            # Check that the record has an InChIKey and a SPLASH
            if inchikeys and 'splash' in spectrum and 'splash' in spectrum['splash']:
                for inchikey in inchikeys:
                    request = {}
                    request['origin'] = 'MoNA'
                    request['record'] = 'http://mona.fiehnlab.ucdavis.edu/rest/spectra/'+ spectrum['id']
                    request['inchiKey'] = inchikey
                    request['splash'] = spectrum['splash']['splash']

                    print('Posting %s+%s' % (request['splash'], request['inchiKey']))

                    r = requests.post('https://api.metabolomics.us/splash/resolve', json=request)

                    if r.status_code != 200:
                        print('\tError', r.status_code)
            else:
                print('No InChIKey or SPLASH available for', spectrum['id'])

        page += 1