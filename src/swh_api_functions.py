#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


import requests

base_swh_api_url = "https://archive.softwareheritage.org/api/1/"

def get_content_information(hash_type, hash):

    """
    this function returns information like checksums, data_url, file_url, license_url
    based on hash_type and hash as a json object
    """
    api = f"{base_swh_api_url}content/{hash_type}:{hash}/"
    response = requests.get(api)
    return response.json()