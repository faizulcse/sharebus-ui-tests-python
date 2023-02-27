### Setup environment and install all dependencies

- Go to project root directory and run the following command
- `brew install virtualenv`
- `virtualenv -p python3 venv`
- `pip install -r requirements.txt`

### Run the test cases using following commands

- ` pytest src/tests/ -q`
- ` pytest src/tests/ -vq`
- ` pytest src/tests/ -m login -sv`
- ` pytest -m login -q`
- `allure generate allure-results --clean -o allure-report allure serve allure-results`
- ` pytest --cov-report html:cov_html --cov-branch --cov=test_login .`