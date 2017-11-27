local:
	heroku local

setup:
	heroku apps:create k2app

deploy:
	git push heroku master

log:
	heroku logs --tail

