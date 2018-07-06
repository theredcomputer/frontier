#!/usr/bin/env python3

import json
import requests
import sys

import pdb


class Agent:
    """
    This class is the preferred version of the agent. It uses the official IEEE Xplore API. You'll need to provide an API key for usage.
    """

    def __init__(self):

        # The key must match a corresponding command line argument.
        self.search_fields = {
            "abstract": "abstract",
            "document_title": "article_title",
            "publication_title": "publication_title",
            "index_terms": "index_terms",
            "authors": "authors",
        }

    def run(self, args, api_key_location="apikeys/ieeexplore/api_key.txt"):

        request_values = {}
        queries = set(vars(args).keys()).intersection(self.search_fields.keys())
        query_types = {k: vars(args)[k] for k in queries if vars(args)[k]}
        for query_type in query_types:
            for term in query_types[query_type]:
                request_values[self.search_fields[query_type]] = term

        try:
            with open(api_key_location, "r") as f:
                request_values["apikey"] = f.readline().strip()
        except IOError:
            print(
                "ERROR: Unable to read API key at location '{}'".format(
                    api_key_location
                )
            )
            print("Exiting...")
            sys.exit()

        result_filters = {
            "max_records": "200",
            "start_record": "1",
            "sort_order": "asc",
            "sort_field": "publication_year",
        }
        request_values.update(result_filters)

        url = "http://ieeexploreapi.ieee.org/api/v1/search/articles"
        payload = request_values

        res = requests.get(url, params=payload)
        data = json.loads(res.content)

        print("Total records returned: {}".format(data["total_records"]))

        return data
