#
# Copyright (C) 2020 GreenWaves Technologies
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
#

import gsystree as st

class Memory(st.Component):
    """
    Memory array

    Attributes
    ----------
    size : int
        The size of the memory.
    stim_file: str
        The path to a binary file which should be preloaded at beginning of the memory.
    power_trigger: bool
        True if the memory should trigger power report generation based on dedicated accesses
    
    """

    def __init__(self, parent, name, size: int, stim_file: str=None, power_trigger: bool=False):

        super(Memory, self).__init__(parent, name)

        self.add_properties({
            'vp_component': 'memory.memory_impl',
            'size': size,
            'stim_file': stim_file,
            'power_trigger': power_trigger
        })