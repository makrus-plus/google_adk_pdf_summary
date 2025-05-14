# Agent Development Kit (ADK) Samples

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

<img src="https://github.com/google/adk-docs/blob/main/docs/assets/agent-development-kit.png" alt="Agent Development Kit Logo" width="150">

#  PDF Summary Agent

The PDF Summary agent displays how someone can reference a file within their GCS bucket and have the agent 
summarize the content either for a standalone output or as part of a multi-modal pipeline. 
This agent showcases a multi-stage, non-conversational agentic
workflow as opposed to a conversational user interaction.

## Overview

This agent shows how a multi-agent architecture might be used to generate
detailed summaries of documents such as a request for purchase. The
PDF Summary Agent is
largely non-conversational -- most of the agent's work takes place through
back-and-forth interactions between individual sub-agents. All the user will need to do is 
provide the agent with a link to the source document in GCS.

This is the high-level workflow the agent follows to generate its analysis.

## Agent Details
The key features of the PDF Summary Agent include:

| Feature | Description |
| --- | --- |
| *Interaction Type* | Summary |
| *Complexity* | Advanced |
| *Agent Type* | Multi Agent |
| *Components* | Tools, AgentTools |
| *Vertical* | Logistics |


### Key Features

##### Agents
* **root_agent:** Entry point for the agent workflow. Coordinates the activity of the other agents.
* **research_agent:** Coordinates the retrieval of individual research components.
* **summarize_meeting_agent:** Reads the request for purchase and generates a summary.

##### Tools
* **store_state_tool**: Stores specific information in the ToolContext.
* **fetch_transcript**: Retrieves the PDF (or relevant document provided) from GCS.

##### Callbacks
* **rate_limit_callback**: Implements request rate limiting to minimize `429: Resource Exhausted` errors.

## Setup and Installation
1.  **Prerequisites:**

    **Google Cloud SDK and GCP Project:**

    For the BigQuery setup and the Agent Engine deployment steps, you will need
    a Google Cloud Project. Once you have created your project,
    [install the Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
    Then run the following command to authenticate with your project:
    ```bash
    gcloud auth login
    ```
    You also need to enable certain APIs. Run the following command to enable
    the required APIs:
    ```bash
    gcloud services enable aiplatform.googleapis.com
    gcloud services enable bigquery.googleapis.com
    ```

2.  **Installation:**

    Clone this repository and change to the repo directory:
    ```
    git clone https://github.com/google/adk-samples.git
    cd adk-samples/agents/fomc-research
    ```

    Install [Poetry](https://python-poetry.org)

    If you have not installed poetry before, you can do so by running:
    ```bash
    pip install poetry
    ```

    Install the FOMC Research agent requirements:
    ```bash
    poetry install
    ```

    This will also install the released version of 'google-adk', the Google Agent Development Kit.

3.  **Configuration:**

    **Environment:**

    There is a `.env-example` file included in the repository. Update this file
    with the values appropriate to your project, and save it as `.env`. The values
    in this file will be read into the environment of your application.

    Once you have created your `.env` file, if you're using the `bash` shell,
    run the following command to export the variables from the `.env` file into your
    local shell environment:
    ```bash
    set -o allexport
    . .env
    set +o allexport
    ```
    If you aren't using `bash`, you may need to export the variables manually.


## Running the Agent

**Using the ADK command line:**

From the `google_adk_pdf_summary` directory, run this command:
```bash
adk run pdf_summary
```
The initial output will include a command you can use to tail the agent log
file. The command will be something like this:
```bash
tail -F /tmp/agents_log/agent.latest.log
```

**Using the ADK Dev UI:**

From the `google_adk_pdf_summary` directory, run this command:
```bash
adk web .
```
It will display a URL for the demo UI. Point your browser to that URL.

The logs from the agent will display on the console in real time as it runs. However,
if you want to store a log of the interaction and also tail the interaction in real
time, use the following commands:

```bash
adk web . > pdf_summary_log.txt 2>&1 &
tail -f pdf_summary_log.txt
```

### Example Interaction

Begin the interaction by typing "Hello". After
the first prompt, provide the agent with the GCS uri you are interested in summarizing (Example: "gs://my-doc-bucket/docs/meeting_notes.pdf").

The interaction will look something like this:
```
$ adk run pdf_summary
Log setup complete: /var/folders/tf/j89nm4nj38l_q1l2m320js7001bxx3/T/agents_log/agent.20250514_140458.log
To access latest log: tail -F /var/folders/tf/j89nm4nj38l_q1l2m320js7001bxx3/T/agents_log/agent.latest.log
Running agent root_agent, type exit to exit.
[user]: hello
[root_agent]: Hello! I'm a virtual research assistant for our logistics company. I can help you create a thorough summary of a request for purchase (RFP).

To get started, please provide the GCS URI of the RFP you'd like me to summarize.
[user]: "gs://my-doc-bucket/docs/meeting_notes.pdf"
[research_agent]: Okay, I will start by retrieving the transcript for the RFP.

Bucket: <Bucket: my-doc-bucket>
[research_agent]: Okay, I have retrieved the transcript. Now I will ask the summarize_rfp_agent to summarize it.
...
```
If the agent stops before completing the analysis, try asking it to continue.


## Troubleshooting

### "Malformed function call"

Occasionally the agent returns the error "Malformed function call". This is a
Gemini model error which should be addressed in future model versions. Simply
restart the UI and the agent will reset.

### Agent stops mid-workflow

Sometimes the agent will stop mid-workflow, after completing one of the
intermediate steps. When this happens, it frequently works just to tell the agent
to continue, or another instruction to continue its operation.
