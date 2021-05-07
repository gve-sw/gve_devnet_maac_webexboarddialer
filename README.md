# GVE_DevNet_MAAC_WebexBoardDialer
HTML Button for Webex Boards to dial a Webex Calling HuntGroup


## Contacts
* Max Acquatella

## Solution Components
*  xapi
*  python
*  flask
*  webex

## Prerequisites
Modify the variables.py script with the following values: 

* Access to a Webex Board (Username and Password). Create the base64 Authorization using publicly available tools like 
  https://www.base64encode.org/ and make sure to encode the username and password using this format: 
  username:password
  then modify the Authorization token like this: "Basic dXNlcm5hbWU6cGFzc3dvcmQ=" - the word Basic is added manually.
  Add the Authorization token to the variables.py script
  
* IP Address of the Webex Board, there is an ip variable. Add this value to the variables.py

Modify the webex_device_xapi.py script with the following value:

* Phone number to dial. This number should be hard coded in the webex_device_xapi.py script. This is the phone number the board will dial:
```html
<Number>YOUR HUNT GROUP NUMBER GOES HERE</Number>
```

## Installation/Configuration

Clone the repo to a folder:

``` git clone (link)```

Create Virtual Environment (recommended), and install requirements.txt:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Launch app.py
```
python app.py
```

## Usage

Take note of the IP address of the device (laptop or server) where the app.py script is running. 

Once app.py is launched, go to the Webex Board's Web Broser and navigate to the IP address from the previous step and add the :5000 port.
It should look like this: http://10.10.10.10:5000/ (10.10.10.10 is just an example, your IP address will be different)

You can also navigate to http://0.0.0.0:5000 directly from the laptop/server where the app.py script is running for testing. 

Click THE BIG GREEN BUTTON TO DIAL

Your board should dial the number of the Hunt Group

# Screenshots

![/IMAGES/click_to_dial.png](/IMAGES/click_to_dial.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.