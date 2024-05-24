# Plant Disease Detection API Server

This repository contains a Flask-based API server for plant disease detection. The server accepts images of plants, passes them to a machine learning model for prediction, and returns the prediction results to the client. The server is deployed on Digital Ocean, and Ansible is used for configuring the remote server.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)

## Overview

This project is an API server built with Flask, designed specifically for plant disease detection. It utilizes a machine learning model to predict the presence of diseases in plant images. The server provides a simple and efficient way to integrate plant disease detection into applications or systems.

## Features

- Plant disease detection using machine learning
- RESTful API built with Flask
- Deployed on Digital Ocean
- Remote server configuration with Ansible

## Requirements

- Python 3.11
- Flask
- TensorFlow
- Ansible
- Digital Ocean account

## Usage


1. **Clone the repository:**

   ```sh
   git clone https://github.com/](https://github.com/mena5800/Flask-api-Ai.git
   cd Flask-api-Ai
   ```

2. **Generate SSH keys:**

   If you don't have SSH keys set up, generate a new pair of SSH keys:

   ```sh
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

3. **Create a droplet on Digital Ocean:**

   - Sign in to your Digital Ocean account.
   - Create a new droplet, selecting your SSH key during the process.

4. **Add the droplet IP to the Ansible hosts file:**

   Update the `host` file with the IP address of your Digital Ocean droplet:

   ```ini
   [ml_deploy]
   your_droplet_ip ansible_user=root
   ```

5. **Deploy the server using Ansible:**

   Run the Ansible playbook to configure the server and deploy the Flask application:

   ```sh
   ansible-playbook deploy.yml
   ```


## API Endpoint

- `POST /api/v1/predict` - Accepts an image of a plant and returns the predicted disease.
