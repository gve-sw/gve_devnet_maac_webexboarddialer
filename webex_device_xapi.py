"""
Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import requests

# Calling function used in app.py
def dial(ip, Authorization):
    # Change this IP address for the IP address of the Board
    url = "https://"+ip+"/putxml"

    # The value of <Number> SHOULD BE FIXED TO THE HUNT GROUP NUMBER
    payload = """
                <Command>
                    <Dial>
                        <Number>YOUR HUNT GROUP PHONE NUMBER GOES HERE</Number>
                    </Dial>
                </Command>"""

    # Authorization is a Base64 value, obtained from the username and password of the board
    headers = {
      'Authorization': Authorization,
      'Content-Type': 'application/xml'
    }

    # REST call to the board which makes the phone call to the number
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.text)
