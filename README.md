## Overview

This project runs a large-scale experiment designed to test bias in AI-generated resume evaluations.
The script:

1. Loads job descriptions
2. Loads multiple resumes
3. Inserts candidate names with different demographic attributes (gender, race)
4. Generates scoring prompts
5. Sends them to the OpenAI API
6. Collects the model’s numeric evaluations
7. Writes all results to a CSV file

Each resume is evaluated multiple times to measure variability and potential bias.

## Project Structure

```text
project/
├── jobs/
│   ├── job11.txt
│   ├── job12.txt
│   ├── job13.txt
│   └── ... (industry-job combinations)
├── resumes/
│   ├── resume11.txt
│   ├── resume12.txt
│   ├── resume13.txt
│   └── ... (industry-resume combinations)
├── names/
│   └── names.txt
├── api_key.txt 
├── run.py       
└── README.md

```
## File Naming Rules
# Job Ads
Files must be named: job<industry><job>.txt

### Resumes
Files must be named: resume<industry><resume>.txt

### The Names File
The names file is structured as a CSV: <name>,<gender_code>,<race_code>

## How the Script Works
1. Load API Key
Reads your OpenAI API key from api_key.txt

2. Build Prompt Combinations
For each:
- repetition
- candidate name
- job ad
- resume
The script inserts the candidate name and creates a scoring prompt asking the model to grade:
1. Relevant Experience
2. Relevant Skills & Qualifications
3. Achievements & Impact
4. Resume Quality
Each category is scored 0–25 and returned as a comma-separated string.

3. Send Prompts to the API

4. Rate Limit Throttling
The script tracks total tokens used and sleeps if it approaches ~25,000 tokens to avoid the API’s 30k/minute limit

5. Extract Numbers and Write CSV
Output CSV includes:
| name | gender | race | industry | job_file | resume_file | Experience | Skills | Achievements | Resume |
You can analyse this CSV in Excel, R, or Python.
