VENV = venv

run:
	docker build -t infragen:lastest .
	docker run infragen:lastest

# Crie um ambiente virtual 
cav:
	python3 -m venv venv

# Ative o ambiente virtual
aav:
	source venv/bin/activate

dav:# Desative o ambiente virtual
	deactivate
