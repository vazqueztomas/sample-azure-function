# Sample Azure Function

This is a sample Azure Function project that includes a simple health check endpoint.

## Prerequisites

- Python 3.6 or later
- Azure Functions Core Tools
- Azure CLI

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/sample-azure-function.git
    cd sample-azure-function
    ```

2. Create a virtual environment, activate it and download dependencies:
    ```sh
    pipenv install --dev
    ```

## Running the Function Locally

1. Start the Azure Functions runtime:
    ```sh
    func host start
    ```

2. The function should now be running at `http://localhost:7071`. You can test the health check endpoint by navigating to `http://localhost:7071/api/healthcheck`.

## License

This project is licensed under the MIT License.