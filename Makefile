
guni:
	gunicorn 'app.server:flsk'

guni-multi:
	gunicorn --workers=4 'app.server:flsk'

uvi:
	uvicorn 'app.server:fapi'
# By default it can handle 12 different sync requests Oo

combo:
	gunicorn --workers=4 -k uvicorn.workers.UvicornWorker 'app.server:fapi'

install:
	pipenv install