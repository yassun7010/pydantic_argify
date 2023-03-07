from pydantic import BaseModel

from pydantic_argparse_builder import command, main


class Config(BaseModel):
    name: str
    age: int
    is_active: bool


@command
def launch(config: Config):
    print(config)


if __name__ == "__main__":
    launch()
