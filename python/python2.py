import re

text = "My email is abcd@gmail.com"

match = re.search(r'[a-zA-Z0-9._%+-]+@gmail\.com', text)

if match:
    print("Found email:", match.group())  # Outputs: abcd@gmail.com
else:
    print("No email found.")