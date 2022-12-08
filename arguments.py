# A class to represent both positional and keyword arguments to a function

import attrs
import typing as t

@attrs.define
class Arguments:
    positional: t.List[t.Any]
    keyword: t.Dict[str, t.Any]
