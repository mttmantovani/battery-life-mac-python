log:
	@./battery-life.sh

plot: log
	@python plot.py

lint:
	@autoflake -iv --remove-all-unused-imports . && isort . && black .


