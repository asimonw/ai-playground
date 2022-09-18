from __future__ import annotations

class Tensor():
    def __init__(self, array: list[float]) -> None:
        self._array = array
    
    @property
    def shape(self) -> tuple[int]:
        return (len(self._array), 1)

    def __repr__(self) -> str:
        return repr(self._array)

    def __add__(self, other: Tensor) -> Tensor:
        return Tensor([x + y for x, y in zip(self._array, other._array)])


if __name__ == '__main__':
    a = Tensor([1, 2, 3])
    print(a.shape)
    print(a)
    b = Tensor([4, 5, 6])
    print(a + b)
