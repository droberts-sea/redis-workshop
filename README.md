## Running This Code

Prerequisites

- Python 3 / pip
- Git

Steps:

1. Clone this repo

    ```
    $ git clone git@github.com:droberts-sea/databases-workshop.git
    $ cd databases-workshop
    ```

1. Run the database via docker-compose

    ```
    $ docker-compose up
    ```

    This will eat the terminal tab - keep it running in the background forever

    If you want to connect to the cache directly, install redis on the host machine (`brew install redis`) and then run:

    ```
    $ redis-cli
    ```

1. (In a new terminal tab) Spin up a virtual environment and install Python dependencies

    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt
    ```

