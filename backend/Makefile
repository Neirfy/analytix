.PHONY: docker up down recreate migrate-all-revision migrate-all-up migrate-% upgrade-% help

SERVICES = authn users
# authz  profile schedule chat TODO

msg ?= init

# =========================
# INFRA
# =========================

recreate:
	docker compose down -v
	docker compose up -d --build

docker:
	docker compose up -d --build

dev:
	docker compose -f docker-compose.dev.yml up -d --build

tests:
	docker compose -f docker-compose.test.yml up --build --abort-on-container-exit

# =========================
# MIGRATIONS ALL
# =========================

migrate-all-revision:
	@for s in $(SERVICES); do \
		echo "==> $$s"; \
		docker compose run --rm $$s alembic revision --autogenerate -m "$(msg)" || exit 1; \
	done

migrate-all-up:
	@for s in $(SERVICES); do \
		echo "==> $$s"; \
		docker compose run --rm $$s alembic upgrade head || exit 1; \
	done

# =========================
# MIGRATIONS SINGLE
# =========================

migrate-%:
	docker compose run --rm $* alembic revision --autogenerate -m "$(msg)"

upgrade-%:
	docker compose run --rm $* alembic upgrade head

# =========================
# HELP
# =========================

help:
	@echo "recreate"
	@echo "docker"
	@echo "migrate-all-revision msg=init"
	@echo "migrate-all-up"
	@echo "migrate-SERVICE msg=init"
	@echo "upgrade-SERVICE"



# curl http://localhost:8000/users/me \
#   -H "X-User-Id: c28e1131-6a70-4f6c-8480-70d1b058ef55" \
#   -H "X-Roles: admin" \
#   -H "Authorization: Bearer test"
