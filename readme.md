# Setup

You first need to install chromedriver.
This can be found here:
https://chromedriver.chromium.org/downloads

## Usage

After the installation of chromedriver, move it to the same directory with the python files. You also need to install python packages in order to use this script. The packages are mentioned below.

```bash
pip install selenium
pip install colorama
pip install termcolor
```

## Credentials
You need to configure the credentials.json file.
Please note that you have to be using bilkent mail instead of your phone for the starts code provider.

```json
{
    "bilkent_id": "YOUR BILKENT ID",
    "stars_password": "PASSWORD",
    "bilkent_mail": "BILKENT MAIL",
    "mail_password": "MAIL PASSWORD"
}

```

## Desktop shortcuts for mac users ### (Shortcuts for windows are on the way)

1. open stars.command and zoom.command using a text editor.
2. type in the folder path to the specified area.
```zsh
echo running bilkent...
clear
cd -PATH TO THE FOLDER CONTAINING PY FILES-
python3 bilkent.py stars
cd /Applications
killall chromedriver
killall Terminal
```
3. save the files and exit.

### 4. If you see an error saying “File could not be executed because you do not have appropriate access privileges” then try running the command below

```zsh
chmod u+x /Users/-YOUR USERNAME-/Desktop/stars.command
chmod u+x /Users/-YOUR USERNAME-/Desktop/zoom.command
```
You can then use the .command files to run the scripts

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
