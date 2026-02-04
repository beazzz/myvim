from model.Data import Data
import model.Command
import model.State as State
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Search", State.SearchState(test))
    test.ChangeState("Search")

    print(test)
    print()
    test.handleInput("/text", "now")
    # print("!!!", test.getPosCursor())

if __name__ == '__main__':
    main()