 install:
	pip install --upgrade pip  &&\
	pip install -r requirements.txt &&\
	pip install ruff &&\
	pip install nbqa &&\
	pip install nbval &&\
	pip install pytest pytest-cov

format:
	black *.py #format all files	

lint:
	ruff check test_*.py && ruff check *.py

test:
	python -m pytest -vv --cov=main test_*.py

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add .
	git commit -m "rerun push" --allow-empty
	git push
