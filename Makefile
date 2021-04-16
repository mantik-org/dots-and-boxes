.PHONY: all init clean

PORT 		?= 8080
AGENT_PORT 	?= 8089
RMTDIR 		?= $(PWD)/lib/remote

all: init

init:
	chmod +x lib/executable/dlv2linux
	@pip3 install -r requirements.txt

run-server:
	@python3 $(RMTDIR)/dotsandboxesserver.py $(PORT)

run-agent:
	@python3 $(RMTDIR)/dotsandboxescompete.py $(AGENT_PORT)

run:
	@python3 -m src