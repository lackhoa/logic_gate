class ExtensibleStream:
    """
    You can think of a stream as a list that can expand into
    a bigger list. The expansion of the list is defined in the
    extend() method.This is not bad use of OOP. If you try to strip out the layer
    of object, you will only get a list with no distinct behavior
    Each time the stream extend, the list (the value) will receive a new node
    A node can actually be anything
    """

    def __init__(self, value: list):
        """
        value is the list of nodes
        """
        self.value = value

    def extend(self):
        """
        Returns the streams that can be created from this stream
        """
        pass

    # Extend as many times as you want
    def extend_count(self, count: int) -> list:
        """

        :param count: The number of times to extend (not 0)
        :return: The streams that are created
        """
        if count == 0:
            raise ValueError('Hey, you cannot extend 0 times')

        current_streams = [self]
        for _ in range(count):
            next_streams = []
            for stream in current_streams:
                next_streams.extend(stream.extend())
            current_streams = next_streams
        return current_streams

    # use this in 'extend(self)'
    def _make_child(self, new_node):
        """
        Why should the new node value be a list?
        """
        # Put the the value of the parent before the child
        tmp = []
        tmp.extend(self.value)
        tmp.append(new_node)
        child = type(self)(tmp)

        return child
