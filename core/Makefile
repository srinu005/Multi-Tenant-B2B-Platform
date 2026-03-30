test:
	docker-compose exec web pytest --cov=.

lint:
	docker-compose exec web ruff check .
	docker-compose exec web ruff format .

migrate:
	docker-compose exec web python manage.py migrate