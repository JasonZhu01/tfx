# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Definition of execution_spec."""

from dataclasses import dataclass
from typing import Any


@dataclass
class ExecutionSpec:
  subgraph: Any
  input_names: set
  output_names: set
  is_remote_op: bool

  # Assist graph partition but not beam pipeline.
  body_node_names: set
  nodes_from_other_layers: set