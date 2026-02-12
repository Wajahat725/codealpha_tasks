import re

input_file = "data.txt"
output_file = "emails.txt"

# Read file content
with open(input_file, "r") as file:
    content = file.read()

# Regular expression for emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Write emails to another file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully.")
