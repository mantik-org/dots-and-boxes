.PHONY: all init clean

PORT 	?= 8080
RMTDIR 	?= $(PWD)/third-party/remote

all: init

init:
	pip3 install -r requirements.txt

run-server:
	@python3 $(RMTDIR)/dotsandboxesserver.py $(PORT)

run-agent:
	@python3 $(RMTDIR)/dotsandboxesagent.py $(PORT)

run:
	@python3 -m src