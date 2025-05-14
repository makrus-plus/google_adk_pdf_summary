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

"""Prompt definintion for summarize_meeting_agent of FOMC Research Agent."""

PROMPT = """
You are a lead bid coordinating agent in understanding the intricacies involved within a request for purchase. 
Below is a transcript of the request for purchase.

<RFP>
{artifact.rfp_fulltext}
</RFP>

Read this transcript and create a summary of the content of this
RFP. Call the store_state tool with key 'rfp_summary' and the value as your
rfp summary. Tell the user what you are doing but do not output your summary
to the user.

Then call transfer_to_agent to transfer to research_agent.

"""