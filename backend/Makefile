.PHONY: docker up down recreate migrate-all-revision migrate-all-up migrate-% upgrade-% help

SERVICES = authn 
# authz user profile schedule chat TODO

msg ?= init

# =========================
# INFRA
# =========================

recreate:
	docker compose down -v
	docker compose up -d --build

docker:
	docker compose up -d --build

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