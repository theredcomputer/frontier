#!/usr/bin/env python3

import json
import requests
import sys

import pdb


class Agent:
    """
    """

    def __init__(self):
    
        # TODO: This dictionary is used for narrowing search results.
        # Certain common types of search terms exist (such as abstracts, titles, etc.), but the specific spelling and grammar a website uses ("abstract" vs "Abstract") can vary.
        # The key (on the left) is what we call it. The value (on the right) is what arXiv calls it.
        # You will need to discover what arXiv uses. This can be done through the Network Inspector.
        self.search_fields = {
            "abstract": '',
            "document_title": '',
            "publication_title": '',
            "index_terms": '',
            "authors": '',
            "search": '',
        }

    def run(self, args):

        search_terms = []

        # Filter unwanted arguments
        queries = set(vars(args).keys()).intersection(self.search_fields.keys())

        # Filter empty arguments
        query_types = {k: vars(args)[k] for k in queries if vars(args)[k]}

        # TODO: build your request to arXiv.
        # This step will require answering a few questions:
        #   1) When making the search query, do you need to make a POST or GET request?
        #   2) What headers will you need? 
        #   3) The query_types variable holds the information necessary to make the specific query. You'll need to massage that data into the form arXiv is expecting.
        url = ""
        headers = {}
        payload = {}
        #res = requests.post(url, headers=headers, json=payload)

        data = json.loads(res.content)

        # TODO: as a test to ensure query results are actually obtained, print out how many results were obtained. You'll need to explore the "data" variable to find where this information is stored.
        #print("Total records returned: {}".format(data["totalRecords"]))

        return data
