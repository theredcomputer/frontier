#!/usr/bin/env python3

import json
import requests
import sys

import pdb


class Agent:
    """
    This class is the original version of the agent. It is indeed functional, but its use clearly violated the Terms of Use of IEEE Xplore for Institutional Subscribers (though, interestingly, not for Guests and IEEE Members). Consequently, it will sit in the back of the toolbox.
    """

    def __init__(self):

        self.search_fields = {
            "abstract": '"Abstract":',
            "document_title": '"Document Title":',
            "publication_title": '"Publication Title":',
            "index_terms": '"Index Terms":',
            "authors": '"Authors":',
            "search": "",
        }

    def run(self, args):

        search_terms = []

        # Filter unwanted arguments
        queries = set(vars(args).keys()).intersection(self.search_fields.keys())

        # Filter empty arguments
        query_types = {k: vars(args)[k] for k in queries if vars(args)[k]}

        for query_type in query_types:
            [
                search_terms.append(self.search_fields[query_type] + term)
                for term in query_types[query_type]
            ]

        def recursive_format(items, string=""):
            if not items:
                return "(" * string.count(")") + string
            if string:
                string = string + " AND " + "{})".format(items[-1])
            else:
                string = string + "{})".format(items[-1])
            return recursive_format(items[:-1], string)

        query_text = recursive_format(search_terms)

        url = "https://ieeexplore.ieee.org/rest/search"
        payload = {
            "matchBoolean": "true",
            "searchField": "Search_All",
            "newsearch": "true",
            "queryText": query_text,
        }

        referrer_url = url + "?" + "&".join([k + "=" + v for k, v in payload.items()])
        referrer_url = referrer_url.replace('"', "%22").replace(" ", "%20")
        headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json, text/plain, */*",
            "Referer": referrer_url,
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        res = requests.post(url, headers=headers, json=payload)
        data = json.loads(res.content)

        print("Total records returned: {}".format(data["totalRecords"]))

        return data
