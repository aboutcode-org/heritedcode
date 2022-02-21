#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import requests
import json


class ApiResponse:
    """
    this class represents response data structure for returning response
    from functions.
    """

    def __init__(
        self,
        checksums,
        data_url,
        filetype_url,
        language_url,
        length,
        license_url,
        status,
    ):
        self.checksums = checksums
        self.data_url = data_url
        self.filetype_url = filetype_url
        self.language_url = language_url
        self.length = length
        self.license_url = license_url
        self.status = status

    def __eq__(self, second_class_obj):
        if isinstance(second_class_obj, ApiResponse):
            for key in vars(self):
                if getattr(self, key) != getattr(second_class_obj, key):
                    return False
            return True
        return False

    """
    Returns an instance of ApiResponse class.
    """

    @classmethod
    def from_swh(
        cls,
        checksums,
        data_url,
        filetype_url,
        language_url,
        length,
        license_url,
        status,
    ):
        return cls(
            checksums, data_url, filetype_url, language_url, length, license_url, status
        )


BASE_SWH_API_URL = "https://archive.softwareheritage.org/api/1/"


def get_content_information(checksum_type, checksum):
    """
    Returns a class object with attributes like checksum, data_url, file_url etc. based on checksum_type and checksum.
    """
    if type(checksum_type) != str or type(checksum) != str:
        raise Exception("checksum_type and checksum must be string")

    api = f"{BASE_SWH_API_URL}content/{checksum_type}:{checksum}/"
    response = requests.get(api)
    response = response.json()
    response_object = ApiResponse.from_swh(
        response.get("checksums"),
        response.get("data_url"),
        response.get("filetype_url"),
        response.get("language_url"),
        response.get("length"),
        response.get("license_url"),
        response.get("status"),
    )
    return response_object
