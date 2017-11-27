local:
    heroku local

deploy:
    git push heroku master

setup:
    heroku apps:create k2app
