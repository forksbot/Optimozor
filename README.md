# Optimozor
## Automatically summarize, correct and translate any text.

<br>
<p align="center">
<img src="logo.png" height="100">
</p>
<br>

### This is the source code for [Optimozor](https://www.producthunt.com/posts/optimozor), a free and open-source text summarizer, translator and corrector.

You can run the dev version by doing:
````bash
cd client

# Install dependencies
npm install

# Start dev server
npm run serve

# Open another terminal window and do:

# Go to server folder
cd server

# Start a pipenv shell
pipenv shell

# Install dependencies (using Pipenv)
sudo pipenv install --skip-lock

# Start server
python main.py

````

You can also run the prod version by doing:
````bash
cd server

# Start a pipenv shell
pipenv shell

# Install dependencies (using Pipenv)
sudo pipenv install --skip-lock

# Start server
python main.py

````
You can also us it as an API by starting the prod version and making post requests to [localhost:5000/api/](localhost:5000/api/) :

#### Params:
* text: string (required)
* title: string (required)
* correct: true / false
* translation: none / french / spanish / german

Please don't hesitate to contribute by doing a PR or by donating!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J3U6LA)