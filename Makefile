build:
	docker-compose build
	docker-compose up -d 

stop:
	docker-compose down

kill:
	docker-compose down
	docker system prune -a