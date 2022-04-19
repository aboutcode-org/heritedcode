#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import requests

class CustomApiResponse:
    """
    this class represents response data structure for returning response
    from functions.
    """

    def __init__(self, data):
        self.checksums = None
        self.data_url = None
        self.filetype_url = None
        self.language_url = None
        self.length = None
        self.license_url = None
        self.status = None

        for key in vars(self):
            if key in data:
                setattr(self, key, data[key])

    def __eq__(self, second_class_obj):
        if isinstance(second_class_obj, CustomApiResponse):
            for key in vars(self):
                if getattr(self, key) != getattr(second_class_obj, key):
                    return False
            return True
        return False

BASE_SWH_API_URL = "https://archive.softwareheritage.org/api/1/"

def get_content_information(checksum_type, checksum):
    """
    Makes call to Software Heritage api to fetch information like checksum, data_url
    file_url etc.
    """
    api = f"{BASE_SWH_API_URL}content/{checksum_type}:{checksum}/"
    response = requests.get(api)
    response = response.json()
    custom_response = CustomApiResponse(response)
    return custom_response
