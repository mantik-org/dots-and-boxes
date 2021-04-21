.PHONY: all init clean

OUTPUT 		?= dots-and-boxes
PORT 		?= 8080
AGENT_PORT 	?= 8089
RMTDIR 		?= $(PWD)/lib/remote

all: init

init:
	@chmod +x lib/executable/dlv2linux
	@pip3 install -r requirements.txt

run-server:
	@python3 $(RMTDIR)/dotsandboxesserver.py $(PORT)

run-interp:
	@python3 -OO -m src $(AGENT_PORT)

build: $(OUTPUT)

run: build
	@chmod +x $(OUTPUT)
	@./$(OUTPUT) $(AGENT_PORT)

clean:
	@$(RM) -f $(OUTPUT)
	@$(RM) -rf __main__.build


$(OUTPUT): src/__main__.py
	@python3 -m nuitka $< --follow-imports --include-package=lib.embasp --include-package=src -o $(OUTPUT)