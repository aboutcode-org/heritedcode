#
# Copyright (c) nexB Inc. and others. All rights reserved.
# heritedcode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/heritedcode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


class CustomApiResponse:
    """
    this class represents response data structure for returning response
    from functions.
    """

    def __init__(self, data):
        for key in data:
            self.key = data[key]

    """
    this function check if two obj of this claa are equal in
    context of attributes and their values
    """

    def __eq__(self, second_class_obj):
        if isinstance(second_class_obj, CustomApiResponse):
            for key in vars(self):
                if self.key != second_class_obj.key:
                    return False
            return True
        return False
