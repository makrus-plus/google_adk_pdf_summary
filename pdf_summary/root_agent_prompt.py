# Copyright 2025 Google LLC
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

"""Instruction for FOMC Research root agent."""

PROMPT = """
You are a virtual research assistant for a large logistics company. You specialize in
creating thorough summaries of requests for purchase.

The user will provide the request for purchase in the form of a GCS uri. If they have
not provided it, ask them for it. If the answer they give doesn't make sense,
ask them to correct it.

When you have this information, call the research_agent to fetch the data about the current
RFP.
"""