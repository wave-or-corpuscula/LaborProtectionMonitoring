from app import FormsController
from app.database.methods_test import test


def main():
    controller = FormsController()
    controller.run_app()
    

if __name__ == "__main__":
    # test()
    main()