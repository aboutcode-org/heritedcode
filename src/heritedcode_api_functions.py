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
    This class represents SWH API response data structure
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
        # represents diffrent type of checksums like sha1,sha1_git and their values
        self.checksums = checksums
        # URL to download content raw bytes
        # for example: https://archive.softwareheritage.org/api/1/content/sha1:0001c9f21990e5c61dd92f6a4a93d306987a1a31/raw/
        self.data_url = data_url
        # URL to get mime type of file like text etc.
        # for example: https://archive.softwareheritage.org/api/1/content/sha1:dc2830a9e72f23c1dfebef4413003221baa5fb62/filetype/
        self.filetype_url = filetype_url
        # URL to get language of file like text/c++/python etc.
        # for example: https://archive.softwareheritage.org//api/1/content/sha1:dc2830a9e72f23c1dfebef4413003221baa5fb62/language/
        self.language_url = language_url
        # represents length of the file
        self.length = length
        # URL to download license
        # for example: https://archive.softwareheritage.org//api/1/content/sha1:dc2830a9e72f23c1dfebef4413003221baa5fb62/license/
        self.license_url = license_url
        self.status = status

    def __eq__(self, second_class_obj):
        if isinstance(second_class_obj, ApiResponse):
            for key in vars(self):
                if getattr(self, key) != getattr(second_class_obj, key):
                    return False
            return True
        return False

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
        """
        Return an instance of ApiResponse class.
        """
        return cls(
            checksums=checksums,
            data_url=data_url,
            filetype_url=filetype_url,
            language_url=language_url,
            length=length,
            license_url=license_url,
            status=status,
        )


BASE_SWH_API_URL = "https://archive.softwareheritage.org/api/1/"


def get_content_information(checksum_type, checksum):
    """
    Return an ApiResponse object given a checksum_type and a cheksum value
    """
    assert (
        type(checksum_type) == str and type(checksum) == str
    ), f"checksum_type: {checksum_type!r} and {checksum!r} must be strings, not {type(checksum_type)!r} and {type(checksum)!r}"

    api = f"{BASE_SWH_API_URL}content/{checksum_type}:{checksum}/"
    response = requests.get(api)
    response = response.json()
    status_code = response.get("status_code")
    assert status_code != 400, "an invalid hash_type or hash has been provided"
    assert status_code != 404, "requested content can not be found in the archive"
    response_object = ApiResponse.from_swh(
        checksums=response["checksums"],
        data_url=response["data_url"],
        filetype_url=response["filetype_url"],
        language_url=response["language_url"],
        length=response["length"],
        license_url=response["license_url"],
        status=response["status"],
    )
    return response_object
