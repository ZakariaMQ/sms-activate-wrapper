# SMSActivate Email Verification API Wrapper

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![httpx](https://img.shields.io/badge/httpx-0.26.0-green)

A Python wrapper for the [SMSActivate.io](https://bit.ly/email-activation) Email Verification API. This library provides simple, user-friendly methods for interacting with the SMSActivate API, allowing you to purchase temporary email addresses, check for incoming verification codes, and manage email activations effortlessly.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)


## Installation

First, ensure you have Python 3.7 or later installed. Then, install the required dependencies using pip:

```bash
git clone https://github.com/ZakariaMQ/sms-activate-wrapper.git
cd sms-activate-wrapper
pip install -r requirements.txt
```

## Getting Started

### Obtain an API Key

To use this service, you'll need an API key from [SMSActivate.io](https://bit.ly/email-activation).

## Features

- **Get Available Domains**: Retrieve a list of available domains for a specific site.
- **Purchase Temporary Email**: Buy a temporary email address for verification purposes.
- **Check for Verification Codes**: Continuously check if a verification code has been received.
- **Cancel Email Activation**: Cancel an email activation if the verification code isn't received in time.
- **View Mail History**: Get a list of active email purchases with their statuses.

## Usage

### For detailed examples, see the file [main.py](https://github.com/ZakariaMQ/sms-activate-wrapper/blob/main/main.py).

## Final Thoughts

This wrapper simplifies the process of managing email verifications through the [SMSActivate.io](https://bit.ly/email-activation) API, making it easier for you to automate and manage their workflows. We hope you find it useful and look forward to any contributions or feedback you might have. Happy coding!

