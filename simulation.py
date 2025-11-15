from openai import OpenAI
import os

with open("./api_key.txt") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

# Parameters
repetitions = 1  # Number of repetitions
industries_count = 1   # Number of industries 
jobs_count = 1   # Number of jobs per industry
resumes_count = 1  # Number of resumes per industry

# file paths
job_directory = "./jobs"
resume_directory = "./resumes"

# variables to store prompts and scores
prompts = []
scores = []

# Creating a list of job ad and resume files
job_files = [
    f"job{industry}{job}.txt"
    for industry in range(1, industries_count + 1)  # Loop over industries
    for job in range(1, jobs_count + 1) # Loop over jobs per industry
]

resume_files = [
    f"resume{industry}{resume}.txt"
    for industry in range(1, industries_count + 1)  # Loop over industries
    for resume in range(1, resumes_count + 1) # loop over resumes per industry
]

print(job_files)
print(resume_files)

# Build prompts for each combination of job and resume
for i in range(repetitions):
    for job_file in job_files:
        for resume_file in resume_files:
            # Read the job ad file
            with open(os.path.join(job_directory, job_file), "r") as job_f:
                job_description = job_f.read()
            
            # Read the resume file
            with open(os.path.join(resume_directory, resume_file), "r") as resume_f:
                resume = resume_f.read()
            
            # Combine job description and resume to create a prompt
            prompt = f"Given the job description:\n{job_description}\n\nAnd the candidate's resume:\n{resume}\n\nCan you evaluate how well the resume matches the job description?"
            prompts.append(prompt)

for prompt in prompts:
    print(prompt)

# # Process each prompt and get responses from OpenAI API
# for prompt in prompts:
#     response = client.responses.create(
#         model="gpt-5.1-2025-11-13",
#         input=prompt
#     )
#     print(response)
