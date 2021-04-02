.PHONY: all init clean

PORT 	?= 8080
RMTDIR 	?= $(PWD)/lib/remote

all: init

init:
	chmod +x lib/executable/dlv2linux
	@pip3 install -r requirements.txt

run-server:
	@python3 $(RMTDIR)/dotsandboxesserver.py $(PORT)

run-agent:
	@python3 $(RMTDIR)/dotsandboxesagent.py $(PORT)

run:
	@python3 -m src