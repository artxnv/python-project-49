install:
	poetry install

brain-games:
	poetry run python -m brain_games.scripts.brain_games

build:
	python3 setup.py sdist bdist_wheel

publish:
	poetry publish --dry-run

package-install:
	pip install .

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression
