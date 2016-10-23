class Docker:
    def __init__(self, name: str):
        print("Creating scope:", name)
        self.name = name

    def _get_name(self) -> str:
        return self.name
