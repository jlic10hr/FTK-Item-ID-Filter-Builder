import xml.etree.ElementTree as ET

def create_filter(item_ids, filter_name="Generated Filter"):
    # Create the root element
    root = ET.Element("exportedFilter", xmlns="http://www.accessdata.com/ftk2/filters")

    # Create the filter element
    filter_elem = ET.SubElement(root, "filter", name=filter_name, matchCriterion="any", id="f_1000006", read_only="false", description="")

    # Create the rules based on the list of Item IDs
    for i, item_id in enumerate(item_ids):
        rule_elem = ET.SubElement(filter_elem, "rule", position=str(i), enabled="true", id="a_9000", operator="is")
        one_int_elem = ET.SubElement(rule_elem, "one_int", value=str(item_id))

    # Create the attribute element
    attribute_elem = ET.SubElement(root, "attribute", id="a_9000", type="int")
    table_elem = ET.SubElement(attribute_elem, "table")
    table_elem.text = "cmn_Objects"
    column_elem = ET.SubElement(attribute_elem, "column")
    column_elem.text = "ObjectID"

    # Create the XML tree and convert it to a string
    xml_tree = ET.ElementTree(root)
    xml_str = ET.tostring(root, encoding="utf-8").decode()

    # Add the XML declaration
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str

    return xml_str

def save_filter_to_file(xml_filter, filename):
    with open(filename, "w") as file:
        file.write(xml_filter)

def read_item_ids_from_file(filename):
    with open(filename, "r") as file:
        item_ids = [int(line.strip()) for line in file if line.strip()]
    return item_ids

if __name__ == "__main__":
    # Specify the filename containing Item IDs
    item_id_filename = "item_ids.txt"

    # Read Item IDs from the text file
    item_ids = read_item_ids_from_file(item_id_filename)

    if not item_ids:
        print("No Item IDs found in the input file.")
    else:
        # Generate the XML filter
        xml_filter = create_filter(item_ids)

        # Save the XML filter to a file
        filter_filename = "generated_filter.xml"
        save_filter_to_file(xml_filter, filter_filename)

        print(f"Filter saved to {filter_filename}")
