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
from contentmethods import methods

data_dir_path = os.path.join(os.path.dirname(__file__), "data")

#input test data
input_test_data = json.load(open(os.path.join(data_dir_path, "input.json")))
#output test data
expected_test_data = json.load(open(os.path.join(data_dir_path, "expected.json")))

def test_get_content_information():
    hash_type = input_test_data['hash_type']
    hash = input_test_data['hash']

    #format is 'output'+{method name}
    expected_output = expected_test_data['output_get_content_information'] 
    #json needs to do dumps to equate two jsons
    expected_output = json.dumps(expected_output, sort_keys=True)
    
    assert json.dumps(methods.get_content_information(hash_type, hash), sort_keys=True) == expected_output