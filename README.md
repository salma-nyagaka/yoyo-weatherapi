[![Build Status](https://app.travis-ci.com/salma-nyagaka/yoyo-weatherapi.svg?branch=develop)](https://app.travis-ci.com/salma-nyagaka/yoyo-weatherapi)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/yoyo-weatherapi/badge.svg?branch=develop)](https://coveralls.io/github/salma-nyagaka/yoyo-weatherapi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/aacacb955f626b290395/maintainability)](https://codeclimate.com/github/salma-nyagaka/yoyo-weatherapi/maintainability)
## yoyo-weatherapi
A weather API.

### Description
A weather API that enables users to get the minimum, maximum, average and median temperature for a  given city and period of time.

### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.10
    ```

-   Clone the weatherapi repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/yoyo-weatherapi
    ```

- Access the project

    ```
    cd yoyo-weatherapi
    ```

- INstall virtualenv

    ```
    pip install virtualenv
    ```

-   Create the virtual environment:

    ```
    virtualenv venv
    ```

-   Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

-   Install dependencies:

    ```
    pip install -r requirements.txt 
    ```

-   Create a .env file and the following configurations

    ```
    export SECRET_KEY='stz-6*!-!vri1n$@hmx1h_n=o^gj$aj=mzzov@vc&6#(!=v6s9'
    export DJANGO_SETTINGS_MODULE=weatherapi.settings
    export API_KEY='80ce3cec537b476a86b161602210509'
    export API_URL='https://api.weatherapi.com/v1/forecast.json'
    ```

-   Get environment variable:

    ```
    source .env
    ```

-   Apply migrations:

    ```
    python manage.py migrate
    ```

-   Run the application with the command:

    ```
    python manage.py runserver 
    ```

 #### ENDPOINT
| REQUEST | DESCRIPTION  | URL  |
| :-----: | :-: | :-: |
| GET | Fetch computed data from the API|  http://127.0.0.1:8000/api/locations/{city}/?days={number_of_days} |
