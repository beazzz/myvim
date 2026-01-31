from model.Data import Data
from model.Command import rightCommand
from model.State import NormalState
from view.View import View


def main():
    test = Data()
    print()
    test.SetContext(NormalState(test))
    print()
    test.handleInput("right")
    print()
    print(test.getPosCursor())


if __name__ == '__main__':
    main()