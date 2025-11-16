##Overview

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
