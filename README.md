## Preparing your environment

+ [Install Python 3.](https://www.python.org/downloads/)
+ Install virtualenv. See [here](https://virtualenv.pypa.io/en/stable/) for why it's useful.
```
pip install virtualenv
```

***

## Set-up for development

+ Clone this repository.
+ Run the following in the repository top-level directory:
```
virtualenv --python=python3 frontier
```
+ Activate the newly-created virtual environment by running the following:
```
source bin/activate
```
+ Install project dependencies by running the following:
```
pip install -r requirements.txt
```
***

## Notes for development

If you're feeling feisty, make the command to activate your virtual environment a useful alias such as `activate`. 

When you're finished coding, run `deactivate` to perform the obvious action.
