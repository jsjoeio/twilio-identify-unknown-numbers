# twilio-identify-unknown-numbers

A project to help you identify unknown phone numbers with Python, AWS Lambda, Twilio Lookup and SMS.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this project, you'll need the following software installed locally:

```
python 3.6.5
```

### Installing

A step by step series of examples that tell you have to get a development env running

1. Clone the project locally

```
git clone https://github.com/jsjoeio/twilio-identify-unknown-numbers.git
```

2. Make a copy of `example.env` and call it `.env`. This is where you'll store your environment variables (auth token, phone number, etc).

```
cp example.env .env
```

Inisde of your .env file, fill out all the variables so you're able to use the Twilio client.

* TODO * - add further steps when ready.

## Deployment

In order to deploy and use with AWS Lambda Functions, you need to create an AWS Lambda Deployment Package in Python. You can do it by following this process:

1. From the root directory, run

```python
# Create a directory called 'v-env'
python3 -m venv v-env
```

2. While you're still at the root directory, run to activate the environment

```python
source v-env/bin/activate
```

3. Install the libraries necessary for this project. In this case, we only need Twilio's helper library.

```python
pip install twilio
```

4. Deactive the environment

```python
deactivate
```

5. Move your `lambda_function.py` file into the `v-env/lib/python3.6/site-packages` directory.

6. Zip the `/site-packages` directory

7. Upload that zipped directory to your AWS Lambda function via the AWS Lambda console.


## Authors

* **Ryan Kauffman** - [Rkauff](https://github.com/Rkauff)
* **Joe Previte** - [jsjoeio](https://github.com/jsjoeio)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

