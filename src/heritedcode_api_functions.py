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
        """represents diffrent type of checksums like sha1,sha1_git and their values"""
        self.checksums = checksums
        """represents data url for available raw data of any code"""
        self.data_url = data_url
        """represents url to get mime type of a file like text/x-c etc."""
        self.filetype_url = filetype_url
        """represents url to get language of a file like text/c/c++ etc."""
        self.language_url = language_url
        """represents length of the file"""
        self.length = length
        """represents url to get license of a file"""
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
    assert (
        type(checksum_type) == str and type(checksum) == str
    ), "checksum_type and checksum must be string"

    api = f"{BASE_SWH_API_URL}content/{checksum_type}:{checksum}/"
    response = requests.get(api)
    response = response.json()
    status_code = response.get("status_code")
    assert status_code != 400, "an invalid hash_type or hash has been provided"
    assert status_code != 404, "requested content can not be found in the archive"
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
