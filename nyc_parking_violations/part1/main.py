from src.bigdata1.api import get_results, raise_for_status
from requests import get
import argparse
# import os
# import sys

# Construct the argument parser
ap = argparse.ArgumentParser()

if __name__ == "__main__":
    ap.add_argument("--page_size", type=int)
    ap.add_argument("--num_pages", type=int, default=False)
    ap.add_argument("--output", default=False)
    args = ap.parse_args()

    get_results(args.page_size, args.num_pages, args.output)




