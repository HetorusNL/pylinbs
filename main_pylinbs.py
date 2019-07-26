from pylinbs import PyLinBS


def main():
    plbs = PyLinBS()

    plbs.select_plugins()
    plbs.initialize_plugins()
    plbs.configure_plugins()
    plbs.execute_plugins()


if __name__ == "__main__":
    main()
