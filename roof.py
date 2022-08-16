import dimensions


class Roof:
    def __init__(self, dims: dimensions.Dimensions):
        self._dimensions = dims

    def __str__(self):
        return self._dimensions.__str__()

    def __repr__(self):
        return f'Width: {self._dimensions.Width} Height: {self._dimensions.Height}'
