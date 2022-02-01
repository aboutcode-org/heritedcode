#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os
import json
import pytest
from src import swh_api_functions

base_swh_api_url = "https://archive.softwareheritage.org/api/1/"

def test_get_content_information(requests_mock):
    #input data
    hash_type = "sha1_git"
    hash = "fe95a46679d128ff167b7c55df5d02356c5a1ae1"
    #output data
    expected_output = {
        "checksums": {
            "blake2s256": "791e07fcea240ade6dccd0a9309141673c31242cae9c237cf3855e151abc78e9",
            "sha1": "dc2830a9e72f23c1dfebef4413003221baa5fb62",
            "sha1_git": "fe95a46679d128ff167b7c55df5d02356c5a1ae1",
            "sha256": "b5c7fe0536f44ef60c8780b6065d30bca74a5cd06d78a4a71ba1ad064770f0c9"
        },
        "data_url": "https://archive.softwareheritage.org/api/1/content/sha1_git:fe95a46679d128ff167b7c55df5d02356c5a1ae1/raw/",
        "filetype_url": "https://archive.softwareheritage.org/api/1/content/sha1_git:fe95a46679d128ff167b7c55df5d02356c5a1ae1/filetype/",
        "language_url": "https://archive.softwareheritage.org/api/1/content/sha1_git:fe95a46679d128ff167b7c55df5d02356c5a1ae1/language/",
        "length": 151810,
        "license_url": "https://archive.softwareheritage.org/api/1/content/sha1_git:fe95a46679d128ff167b7c55df5d02356c5a1ae1/license/",
        "status": "visible"
    }

    
    api = f"{base_swh_api_url}content/{hash_type}:{hash}/"
    requests_mock.get(api, json=expected_output)    

    #json needs to do dumps to equate two jsons
    expected_output = json.dumps(expected_output, sort_keys=False)
    assert json.dumps(swh_api_functions.get_content_information(hash_type, hash), sort_keys=False) == expected_output