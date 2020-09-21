# X-MHM UserBot

<p align="center">
<img src="https://telegra.ph/file/ed74fd6f6638f3c46e1f5.jpg" alt="X-MHM USERBOT">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



Best User Bot To Manage Your Telegram Account 
## Most PowerFul And Better And Secure

## © By Team #SᴛᴀʀᴋGᴀɴɢ™

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/MHMOFFICIAL"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/CyberProgram"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

## HOW TO DEPLOY 

<a href="https://youtu.be/xfHcm_e92eQ"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>


### Host Friday In Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Dev-MHM/X-MHM)

## Telegram-String

[![Run on Repl.it](https://session.DevMHM.repl.run)


### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Dev-MHM/X-MHM
cd X-MHM
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```



**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

## Credits 
```- https://t.me/CyberProgram
   - https://t.me/MHMOFFICIAL

Check More Contribution At https://github.com/Dev-MHM/graphs/contributors
