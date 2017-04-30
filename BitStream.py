from ExtensibleStream import ExtensibleStream


class BitStream(ExtensibleStream):  # MAKE THIS INTO A FILE
    """
    Tested!
    """

    def extend(self):
        zero = self._make_child(True)
        one = self._make_child(False)
        return [zero, one]
