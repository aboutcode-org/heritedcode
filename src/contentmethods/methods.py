#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


import requests as req

base_content_swh_api_url = "https://archive.softwareheritage.org/api/1/content/"

#this method is used to get information about content (aka a "blob") object. 
#In the archive, a content object is identified based on checksum values computed using various hashing algorithms.

def get_content_information(hash_type, hash):
    endpoint = f"{hash_type}:{hash}/"
    api = base_content_swh_api_url + endpoint
    res = req.get(api)

    if res.status_code == 404:
        return {"msg":"No data found"}
    elif res.status_code == 400:
        return {"msg":"Invalid hash or hash type"}
    return res.json()