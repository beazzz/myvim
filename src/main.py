from model.Data import Data
from model.Command import rightCommand
from model.State import NormalState
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Normal", NormalState(test))
    test.ChangeState("Normal")

    test.handleInput("right")
    test.handleInput("right")
    test.handleInput("right")

    test.handleInput("left")
    print()
    print(test.getPosCursor())

if __name__ == '__main__':
    main()