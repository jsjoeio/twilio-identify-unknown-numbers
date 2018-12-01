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

```bash
git clone https://github.com/jsjoeio/twilio-identify-unknown-numbers.git
```

2. Make a copy of `example.env` and call it `.env`. This is where you'll store your environment variables (auth token, phone number, etc).

```bash
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

3. Install the libraries necessary for this project. In this case, we need Twilio's helper library, and the python-dotenv library. 

```bash
pip install twilio python-dotenv
```
If you're developing on Windows and running into issues with the dotenv, try the following:
```bash
# Don't forget the period after target
pip3 install python-dotenv --target .
```

4. Deactivate the environment

```bash
deactivate
```

5. Move your `lambda_function.py` file into the `v-env/lib/python3.6/site-packages` directory.

6. Zip the contents of `/site-packages` directory. *NOTE* You _must_ zip the contents, and not the directory itself. I recommend doing this via the command line.

```bash
# From the root
cd v-env/lib/python3.6/site-packages
# This will zip the contents into a file called function.zip that will be in the parent directory
zip -r9 ../function.zip .
```

7. Upload that zipped directory `function.zip` to your AWS Lambda function via the AWS Lambda console.


## Authors

* **Ryan Kauffman** - [Rkauff](https://github.com/Rkauff)
* **Joe Previte** - [jsjoeio](https://github.com/jsjoeio)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

