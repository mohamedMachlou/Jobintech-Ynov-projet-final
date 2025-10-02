from services.main import main_menu
import utils.data_loader as _ # keep loader before seeders
import seeders.main as _


def main():
    try:

        main_menu()
    except:
        pass


if __name__ == "__main__":
    main()
