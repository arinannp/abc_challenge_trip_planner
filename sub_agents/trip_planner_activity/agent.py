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

"""trip_planner_activity_agent for defining day-to-day activities based on departure and destination of the trip"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"

trip_planner_activity_agent = Agent(
    model=MODEL,
    name="trip_planner_activity_agent",
    description=(
        "A concise, budget-focused AI travel planner that builds complete, "
        "day-by-day itineraries—including flights, hotels, "
        "and activities—that strictly adhere to your total budget."
    ),
    instruction=prompt.TRIP_PLANNER_ACTIVITY_PROMPT,
    output_key="trip_planner_activity_output",
    tools=[google_search],
)
