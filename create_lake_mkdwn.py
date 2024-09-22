import csv

# Function to generate the Markdown table
def generate_markdown_table(csv_file):
    lakes = []

    # Read the CSV file and store the data
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lake_name, image_name = row
            lakes.append((lake_name, image_name))
    
    # Sort lakes by lake name
    lakes.sort(key=lambda x: x[0])

    # Begin Markdown table
    markdown_output = ''

    # Process each row and format as Markdown
    for idx, (lake_name, image_name) in enumerate(lakes):
        # Create the cell Markdown
        cell_md = f'[![{lake_name}](/assets/img/{image_name})](/assets/img/{image_name}) ' \
                  f'<span style="font-weight:normal">{lake_name}</span>'
        
        # Add the cell to the row
        markdown_output += f'{cell_md} | '

        # Start a new row every 3 cells
        if (idx + 1) % 3 == 0:
            markdown_output = markdown_output.rstrip(' | ') + '\n\n'
    
    # Close any open row
    if len(lakes) % 3 != 0:
        markdown_output = markdown_output.rstrip(' | ') + '\n\n'
    
    return markdown_output

# Path to your CSV file
csv_file_path = 'lakes.csv'

# Generate the Markdown
markdown_result = generate_markdown_table(csv_file_path)

# Print or save the Markdown output
print(markdown_result)
