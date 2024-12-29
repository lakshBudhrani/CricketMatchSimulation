# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:27:57 2024

@author: budhrani
"""

import re
import os

def extract_lines_with_features(file_path):
    extracted_lines = []
    extracted_values = []

    if not os.path.isfile(file_path):
        raise ValueError(f"The path {file_path} is not a file or doesn't exist.")

    with open(file_path, 'r') as file:
        for line in file:
            if 'international' in line and 'Test' in line and not 'female' in line and ('India' in line or 'Australia' in line):
                extracted_lines.append(line.strip())
                match = re.search(r'\d{4}-\d{2}-\d{2} - international - Test - male - (\d+) -', line)
                if match:
                    extracted_values.append(match.group(1))
    return extracted_lines, extracted_values

# Specify the file path
file_path = 'D:\\USCB\\Sem 7\\Modeling and Simulation\\Project\\README.txt'

# Ensure the file exists and is readable
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    lines, values = extract_lines_with_features(file_path)

#     # Print the extracted lines and values
#     print("Extracted Lines:")
#     for line in lines:
#         print(line)

#     print("\nExtracted Values:")
#     print(values)

#     print()
#     print(len(lines))
#     print(len(values))
# else:
#     print(f"Error: The file {file_path} does not exist or is not readable.")
