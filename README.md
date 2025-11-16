## Credit 
Special mention to the authors Marianne Bertrand & Sendhil Mullainathan of the 2003 working paper 'Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination.'
The names and name categories used in this study are based on their original research conducted in 2003.

## Racial Name Categories
This project uses name lists derived from the classic résumé discrimination experiment by Bertrand and Mullainathan (2003). In their study, certain names were statistically associated with African-American applicants and others with White American applicants in the United States labour market.

To avoid incorrectly applying US racial categories to an Australian context, this project labels the two groups as:
1. AA_US — Names used in the 2003 study that signalled African-American applicants in the US context
2. White_US — Names used in the 2003 study that signalled White applicants in the US context

These labels are used only as experimental signalling variables to reproduce the methodological structure of the original study. They do not imply that these name–race associations generalise to Australia, nor do they represent Australian racial or cultural categories.

Reference:
Bertrand, M., & Mullainathan, S. (2003). Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination. Cambridge, MA: National Bureau of Economic Research. Retrieved from https://doi.org/10.3386/w9873

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
├── results
│   ├── evaluation_results.csv
│   └── ... (further results files)
├── api_key.txt 
├── run.py
├── requirements.txt       
└── README.md

```
## File Naming Rules
### Job Ads
Files must be named: job<industry><job>.txt

### Resumes
Files must be named: resume<industry><resume>.txt

### The Names File
The names file is structured as a CSV: <name>,<gender_code>,<race_code>

## How the Script Works

### 1. Load API Key
Reads your OpenAI API key from `api_key.txt`.

### 2. Build Prompt Combinations
For each:

- repetition  
- candidate name  
- job ad  
- resume  

The script inserts the candidate name and creates a scoring prompt asking the model to grade:

- **Relevant Experience**  
- **Relevant Skills & Qualifications**  
- **Achievements & Impact**  
- **Resume Quality**  

Each category is scored **0–25** and returned as a comma-separated string.

### 3. Send Prompts to the API
Uses `client.responses.create()` to submit each prompt for scoring.

### 4. Rate Limit Throttling
The script tracks total tokens used and sleeps if it approaches **~25,000 tokens** to avoid exceeding the API’s **30k/minute** limit.

### 5. Extract Numbers and Write CSV
The output CSV includes the columns:

| name | gender | race | industry | job_file | resume_file | Experience | Skills | Achievements | Resume |

You can analyse this CSV using Excel, R, or Python.

## Running the Script
### 1. Install dependencies
Make sure you have Python 3.10+ installed, then run:
```bash
pip install -r requirements.txt
```
### 2. Add your OpenAI API Key
Create a file named: api_key.txt
Place your key inside (no quotes, no spaces).

### 3. Add job ads, resumes and names
Put job files in the jobs/ folder
Put resumes in the resumes/ folder
Put the names list in names/names.txt

### 4. Run the experiment
```bash
python run.py
```
### 5. View results
The script will generate evaluation_results.csv
