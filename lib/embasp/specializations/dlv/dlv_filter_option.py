from lib.embasp.languages.asp.asp_filter_option import ASPFilterOption


class DLVFilterOption(ASPFilterOption):
    """Represents a filter option that can be added to a DLV
    execution, for filtering output generated by the solver."""

    def __init__(self, initial_option):
        self._options += initial_option
