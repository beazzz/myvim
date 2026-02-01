from model.Data import Data
import model.Command
from model.State import NormalState
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Normal", NormalState(test))
    test.ChangeState("Normal")

    print(test)
    print()
    test.handleInput("yy")
    test.handleInput("NG", 2)
    test.handleInput("p")

    #test.handleInput("dd")

    print(test)
    print()

if __name__ == '__main__':
    main()