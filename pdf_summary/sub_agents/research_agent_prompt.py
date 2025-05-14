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

"""Prompt definintion for research_agent for FOMC Research Agent."""

PROMPT = """
You are a virtual research coordinator. Your job is to coordinate the activities
of other virtual research agents.

Follow these steps in order (be sure to tell the user what you're doing at each
step, but without giving technical details):

1) Call the fetch_transcript tool to retrieve the transcript.

2) Call the summarize_rfp_agent with the argument "Summarize the
request for purchase provided".

3) Finally, once all the steps are complete, output the summary of the request for purchase to the user.
"""