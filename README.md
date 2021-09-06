[![CircleCI](https://circleci.com/gh/salma-nyagaka/yoyo-weatherapi.svg?style=svg&circle-token=58c9525164497938d1301973f227259422fcb138)](https://circleci.com/gh/salma-nyagaka/yoyo-weatherapi)

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

-   Install pipenv:

    ```
    brew install pipenv
    ```

-   Check pipenv is installed:

    ```
    pipenv --version
    >> pipenv, version 2018.11.26
    ```
    

-   Clone the weatherapi repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/yoyo-weatherapi
    ```

-   Activate the virtual environment:

    ```
    pipenv shell
    ```


-   Install dependencies:

    ```
    pipenv install
    ```

-   Make a copy of the .env.sample file  and rename it to .env and update the variables accordingly:

    ```
    SECRET_KEY='stz-6*!-!vri1n$@hmx1h_n=o^gj$aj=mzzov@vc&6#(!=v6s9'
    DJANGO_SETTINGS_MODULE=weatherapi.settings
    API_KEY='80ce3cec537b476a86b161602210509'
    API_URL='https://api.weatherapi.com/v1/forecast.json'
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
