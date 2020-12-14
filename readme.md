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

## Recommended commands (For zsh users)
1. open ~/.zshrc file with a code editor. (nano)
2. type in following command.
```zsh
nano ~/.zshrc

bilkent() {
	echo running bilkent...
	clear
	cd -PATH TO THE FOLDER CONTAINING PY FILES-
	python3 $1.py
	cd /Applications
	killall chromedriver
}

```
3. save the file and exit.

This command will allow you to run the script directly from terminal by simply typing "bilkent zoom" or "bilkent stars" depending on what you want to do.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
