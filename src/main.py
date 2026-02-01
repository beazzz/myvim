from model.Data import Data
import model.Command
from model.State import NormalState
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Normal", NormalState(test))
    test.ChangeState("Normal")

    #test.handleInput("w")
    for i in range(23):
        test.handleInput("right")
    
    print(test.getPosCursor(),test.getSymbol())

    test.handleInput("w")
    print(test.getPosCursor(),test.getSymbol())


if __name__ == '__main__':
    main()