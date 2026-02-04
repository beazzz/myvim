from model.Data import Data
import model.Command
import model.State as State
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Insert", State.InsertState(test))
    test.ChangeState("Insert")

    print(test)
    print()
    test.handleInput("r", "X")
    print(test)
    print()

if __name__ == '__main__':
    main()