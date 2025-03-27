import sqlite3
import xml.etree.ElementTree as ET

# Connect to your SQLite database
conn = sqlite3.connect("RealEstateProject.db")
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create the root XML element
root = ET.Element("database")

# Loop through each table
for table_name in tables:
    table = table_name[0]
    table_element = ET.SubElement(root, table)

    # Get table data
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    for row in rows:
        row_element = ET.SubElement(table_element, "record")
        for col_name, value in zip(column_names, row):
            field = ET.SubElement(row_element, col_name)
            field.text = str(value)

# Save to an XML file
tree = ET.ElementTree(root)
tree.write("RealEstateData.xml", encoding="utf-8", xml_declaration=True)

# Close the connection
conn.close()

print("✅ All tables exported to RealEstateData.xml")


