-- authn service
CREATE DATABASE authn_db;

CREATE USER authn_service WITH PASSWORD 'authn_pass';

ALTER DATABASE authn_db OWNER TO authn_service;

-- authz service
CREATE DATABASE authz_db;

CREATE USER authz_service WITH PASSWORD 'authz_pass';

ALTER DATABASE authz_db OWNER TO authz_service;