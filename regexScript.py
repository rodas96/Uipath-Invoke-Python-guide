import re
import json

def extract_invoice_data(text):
    # Initialize the dictionary to store the extracted data
    invoice_data = {}

    # Extract the vendor name
    match = re.search(r"Vendor:\s*(.+)", text)
    if match:
        invoice_data["Vendor"] = match.group(1)

    # Extract the item description
    match = re.search(r"\d+\s+(.+?)\s+\d+\s+[A-Z]{3}\s+\d+\s+[\d.]+\s+[A-Z]{3}", text)
    if match:
        invoice_data["Item Description"] = match.group(1)
        
    # Extract the untaxed amount
    match = re.search(r"Subtotal:\s*(\d+(?:\.\d+)?)", text)
    if match:
        invoice_data["Untaxed Amount"] = match.group(1)

    # Extract the taxed amount and total amount
    match = re.search(r"Tax:\s*(\d+(?:\.\d+)?)", text)
    if match:
        invoice_data["Taxed Amount"] = match.group(1)

    # Convert the dictionary to JSON as advised in uipath forum
    invoice_json = json.dumps(invoice_data)
    
    return invoice_json
