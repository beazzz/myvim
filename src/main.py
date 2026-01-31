from model.Data import Data
from model.Command import rightCommand
from model.State import NormalState
from view.View import View


def main():
    test = Data("test.txt")
    print()
    test.AddState("Normal", NormalState(test))
    print()
    test.ChangeState("Normal")
    test.handleInput("right")
    print()
    print(test.getPosCursor())

if __name__ == '__main__':
    main()