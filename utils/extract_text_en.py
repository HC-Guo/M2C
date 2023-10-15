import json

# Provide the path to your text file
file_path = ''

# Read the JSON data from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

# Parse the JSON data
data = json.loads(text_data)

# Create an empty list to store 'text_en' values
text_en_list = []

# Iterate through the pages and text segments to extract 'text_en' values
for page in data:
    text_segments = page['page']['text']

    for segment in text_segments:
        text_en = segment['text_en']
        text_en_list.append(text_en)

# Print the extracted 'text_en' content
for text_en in text_en_list:
    print(text_en)

# Specify the desired output file path for 'text_en' values
output_file_path = 'results/text_en_output_sep.txt'

# Write 'text_en' values to the output file with '[SEP]' delimiter
with open(output_file_path, 'w', encoding='utf-8') as file:
    for text_en in text_en_list:
        file.write(text_en + '[SEP]')

# Print a success message with the file path
print(f"Text data successfully written to {output_file_path}.")
