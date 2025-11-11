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

"""Trip planning: provide planning of a trip along with the itinerary"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Backup Working Laptop 2025/Pointstar/Research/ABC Challenge/id-iprd-1111-ps-abcchallenge-de96e3a488ae.json"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "id-iprd-1111-ps-abcchallenge"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

from . import prompt
from .sub_agents.trip_planner_activity import trip_planner_activity_agent


MODEL = "gemini-2.5-pro"

ai_travel_planner = LlmAgent(
    name="ai_travel_planner",
    model=MODEL,
    description=(
        "This is a top-level AI agent for trip planning. "
        "It orchestrates the entire planning process by first gathering 6 required inputs "
        "from the user (departure, destination, budget, people, date, duration). "
        "It then delegates tasks, calling the trip_planner_activity_agent for the detailed itinerary "
        "and (if available) the weather_agent for a forecast. "
        "Finally, it synthesizes these outputs into a single, cohesive response."
    ),
    instruction=prompt.ROOT_TRIP_PLANNER_PROMPT,
    output_key="ai_travel_planner_output",
    tools=[
        AgentTool(agent=trip_planner_activity_agent),
    ],
)

root_agent = ai_travel_planner
