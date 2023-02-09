import json
import requests
import csv_reader
import fhir_server
from fhirclient.models import location as loc
from fhirclient.models import fhirreference
import constants
import fhirclient.models.identifier as location_identifier
import uuid


def post_location_to_server():
    # Use a breakpoint in the code line below to debug your script.

    my_location = csv_reader.read_csv_file()

    parent_location = ''
    location_list = []
    headers = fhir_server.post_header()
    for k in my_location.keys():
        parent_location = k
        for child_location in my_location[parent_location]:
            location = create_other_location(child_location, parent_location)
            location_list.append(location.as_json())

    for catchment in location_list:
        catchment_json = json.dumps(catchment)
        response = requests.post(
            url=f'http://192.168.100.4:8085/fhir/Location/',
            data=catchment_json,
            headers=headers
        )
        print(response.status_code)
        print(catchment_json)

    print(location_list)
    print(parent_location)


def create_root_location():
    root_location = loc.Location()
    root_location.name = " Root Location"
    root_location.status = 'active'
    root_location_identifier = location_identifier.Identifier()
    root_uuid = str(uuid.uuid4())
    root_location_identifier.value = root_uuid
    root_location_identifier.use = 'official'
    root_location.identifier = [root_location_identifier]
    root_location.physicalType = constants.catchment_codeable_concept
    headers = fhir_server.post_header()
    root_location_json = json.dumps(root_location.as_json())
    response = requests.post(
        url=f'http://192.168.100.4:8085/fhir/Location/',
        data=root_location_json,
        headers=headers
    )
    response_code = response.status_code
    print(response_code)


def create_other_location(child_location, parent_location):
    parent_location_id = child_location['parent_id']
    location = loc.Location()
    location.name = child_location['name']
    other_location_identifier = location_identifier.Identifier()
    location_uuid = str(uuid.uuid4())
    other_location_identifier.use = 'official'
    other_location_identifier.value = location_uuid
    location.identifier = [other_location_identifier]
    location.status = 'active'
    location.physicalType = constants.catchment_codeable_concept
    ref = fhirreference.FHIRReference()
    ref.reference = f'Location/{parent_location_id}'
    ref.display = parent_location
    location.partOf = ref

    return location


def delete_all_locations():
    headers = fhir_server.get_header()
    response = requests.delete(
        'http://192.168.100.4:8085/fhir/Location?_expunge=true',
        headers=headers
    )

    print(response.status_code)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    post_location_to_server()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
