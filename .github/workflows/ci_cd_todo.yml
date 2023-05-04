name: CI/CD todo

on:
  push:
    branches: [ main ]
    paths:
      - src/**
  pull_request:
    branches: [ main ]
    paths:
      - src/**

jobs:

  flake8-lint:
    name: Lint with flake8
    runs-on: ubuntu-latest
    steps:
      - name: Check out source repository
        uses: actions/checkout@v3
      - name: Set up Python environment
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: flake8 Lint
        uses: py-actions/flake8@v2

  build:
    name: build and push Docker image
    needs: flake8-lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
          
      - name: Login to DockerHub
        uses: docker/login-action@v2 
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          
      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true 
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/galeria:latest
      # - name: Sleep for 60 seconds
      #   run: sleep 60s
      #   shell: bash

  aws:
    name: Deploy image to aws
    needs: build
    runs-on: ubuntu-latest
    steps:
    - name: multiple command
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOSTNAME }}
        username: ${{ secrets.USER_NAME }}
        key: ${{ secrets.AWS_PRIVATE_KEY }}
        port: 22  # ${{ secrets.PORT }}
        script: |
            sleep 30
            docker stop web && docker rm web
            docker rmi angoies/galeria
            docker run -d -p 80:5000 --name web angoies/galeria
            sleep 30
  curl:
    name: Test URL con curl
    needs: aws
    runs-on: ubuntu-latest
    steps:
    - name: curl
      uses: wei/curl@master
      with:
        args: http://${{ secrets.HOSTNAME }}
