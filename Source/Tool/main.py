from linguifiy_class import Linguify

def main():
    main_instance = Linguify(0)

    try:
        main_instance.file_name = 123
    except TypeError as ex:
        print(f"{type(ex)}: {ex}")
        raise TypeError("Program failed due to incorrect file_name type.") from ex
    except Exception as ex:
        print(f"An unexpected error occurred in file_name setter: {type(ex)}: {ex}")
        raise Exception("Program failed due to unexpected file_name setter error.") from ex

    try:
        main_instance.num_of_playlists = "string"
    except TypeError as ex:
        print(f"{type(ex)}: {ex}")
        raise TypeError("Program failed due to incorrect num_of_playlists type.") from ex
    except ValueError as ex:
        print(f"{type(ex)}: {ex}")
        raise ValueError("Program failed due to incorrect num_of_playlists value.") from ex
    except Exception as ex:
        print(f"An unexpected error occurred in num_of_playlists setter: {type(ex)}: {ex}")
        raise Exception("Program failed due to unexpected num_of_playlists setter error.") from ex

    try:
        main_instance.set_playlists(["1", "2"])
    except TypeError as ex:
        print(f"{type(ex)}: {ex}")
        raise TypeError("Program failed due to incorrect set_playlists type.") from ex
    except ValueError as ex:
        print(f"{type(ex)}: {ex}")
        raise ValueError("Program failed due to incorrect set_playlists value.") from ex
    except Exception as ex:
        print(f"An unexpected error occurred in set_playlists method: {type(ex)}: {ex}")
        raise Exception("Program failed due to unexpected set_playlists method error.") from ex

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f"An unhandled error occurred: {ex}")
    else:
        print("Program exited successfully.")