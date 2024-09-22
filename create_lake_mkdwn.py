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

    # Begin Markdown table with header row
    markdown_output = '| ' * 3 + '\n'  # First row with 3 empty headers
    markdown_output += '| :---: | :---: | :---: |\n'  # Second row as the separator

    # Process each row and format as Markdown
    for idx, (lake_name, image_name) in enumerate(lakes):
        # Create the cell Markdown
        cell_md = f'[![{lake_name}](/assets/img/{image_name})](/assets/img/{image_name}) ' \
                  f'<span style="font-weight:normal">{lake_name}</span>'
        
        # Add the opening bar at the start of a new row
        if idx % 3 == 0:
            markdown_output += '| '

        # Add the cell to the row
        markdown_output += f'{cell_md} | '

        # Add a newline after every 3 cells
        if (idx + 1) % 3 == 0:
            markdown_output += '\n'

    # If the last row has fewer than 3 cells, close the row
    if len(lakes) % 3 != 0:
        markdown_output += '\n'
    
    return markdown_output

# Path to your CSV file
csv_file_path = 'lakes.csv'

# Generate the Markdown
markdown_result = generate_markdown_table(csv_file_path)

# Print or save the Markdown output
print(markdown_result)
