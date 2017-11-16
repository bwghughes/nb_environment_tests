envcheck:
	export ENVSTATUS_BASE_URL=http://127.0.0.1:8080 && \
	py.test environment_tests.py

test:
	py.test --cov=utils --cov-report=term-missing