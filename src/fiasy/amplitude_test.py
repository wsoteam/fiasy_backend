# import requests
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': '*/*'
# }

# r = requests.get(
#     'https://amplitude.com/api/2/export?start=20190827T5&end=20190827T18',
#     data={
#         "API_Key": "b148a2e64cc862b4efb10865dfd4d579"
#     },
#     headers=headers
# )

# print(r.headers)
# print(r)

import amplitude	

# initialize amplitude logger
amplitude_logger = amplitude.AmplitudeLogger(api_key="b148a2e64cc862b4efb10865dfd4d579")

# example event
event_args = {"device_id":"b29bdd40-7a8e-4cdc-924e-775b8d2d7dd7R", "event_type":"justtesting_user_id_is_kek",
              "user_id":"lol",
              "event_properties":{"property1":"somevalue", "propertyN":"anothervalue"}
              }
event = amplitude_logger.create_event(**event_args)

# send event to amplitude
amplitude_logger.log_event(event)

# from pyamplitude.apiresources import ProjectsHandler
# from pyamplitude.exportapi import AmplitudeExportApi

# fiasy_connector = ProjectsHandler(
#   project_name='Fiasy',
#   api_key='b148a2e64cc862b4efb10865dfd4d579',
#   secret_key='115a722e4336d141626d680fc1cca21c'
# )

# apiconector = AmplitudeExportApi(
#   project_handler=fiasy_connector,
#   show_logs=False
# )
# data = apiconector.get_all_events_data(
#   start='20190826',
#   end='20190827'
# )

# print(data)
