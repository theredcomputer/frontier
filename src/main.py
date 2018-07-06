#!/usr/bin/env python3

"""
Frontier: find your field.

When beginning a new research thrust, significant effort is undertaken to 
understand how much prior literature exists. This tool is designed to 
expedite this process by searching across publications and gathering
results.
"""

import argparse
import importlib
import requests

import json
import time

import pdb


"""
TODO: Break clients into separate files.

File structure should be as the following:

<project_root>
|
|---src
    |
    |---databases
        |
        |---ieee
        |   |
        |   |---web.py
        |   |---api.py
        |
        |---acm
            |
            |---api.py

Each file will have single class named "Agent".
For the time being, the Agent will parse fields and return requested statistics.

Workflow in main:
    1) Parse command line arguments
    2) Instantiate desired agent
    3) Make request.
    4) Provide statistics for user.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search across online publications for prior literature.\n\nFor now, please only search a MAXIMUM of three (3) terms."
    )
    parser.add_argument(
        "--database", type=str, nargs='+', help="Choose the database(s) to search in. Default value: \'ieeexplore.api\'"
    )
    parser.add_argument(
        "--search", type=str, nargs="+", help="a term to generically search by"
    )
    parser.add_argument(
        "--document_title", type=str, nargs="+", help="search for term in titles"
    )
    parser.add_argument(
        "--abstract", type=str, nargs="+", help="search for term in abstracts"
    )
    parser.add_argument(
        "--publication_title",
        type=str,
        nargs="+",
        help="search in specific publications",
    )
    args = parser.parse_args()

    # Format search terms

    # Note: key is our parser's variable name, value is actual URL key
    agent_lib = ['databases.' + db for db in args.database]
    agent_pkgs = [importlib.import_module(lib) for lib in agent_lib]
    for agent_pkg in agent_pkgs:
        agent = agent_pkg.Agent()
        data = agent.run(args)
    #pdb.set_trace()
