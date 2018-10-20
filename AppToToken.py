import sys
import json
import requests
from tkinter import *
from tkinter import messagebox
from requests.exceptions import ConnectionError

api_token_test = 'eyJleHBEYXRlIjoiMjAxOS0xMC0xN1QxMjo0MTo1NS0wNzAwIiwidG9rZW4iOiJtMHZMU0tqSnBEbzJMc1VDSFdweHN4UTdvcUJKVTg4WWgyUDhqUHc4TGxWcXlDdFFWWC9SMWVGTlJWbTV5TWMvWklVdXFNdDI5Lzc0YmFyVUxjWW1iY1lrN3NXZHBlR2xjRmthRDg4Q1c1eWNReGNRc2xQWVFGdVdxY3ljajNYUyIsIm9yZ05hbWUiOiJLZW5pbHdvcnRoIFNjaG9vbCBEaXN0cmljdCAzOCJ9'
adam_id = "360593530"


def get_token_info(api_token, adam_id):
    try:
        api_url = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + api_token + \
              '&includeLicenseCounts=' + adam_id
        response = requests.get(api_url)
        json_response = response.json()
        if response.status_code == 200:
            for all_assets in range(len(json_response['assets'])):
                adam_id_search = json_response['assets'][all_assets]['adamIdStr']
                if adam_id_search == adam_id:
                    total_count = json_response['assets'][all_assets]['totalCount']
                    return total_count
                else:
                    return None
        else:
            messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n "
                                                     "Please check your internet connection.")
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


print(get_token_info(api_token_test, adam_id))
