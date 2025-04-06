import os
import io

"""
To do:

"""
from typing import List

class Linguify:
    """
    A class that will collect playlist artist data for select playlists from spotify data
    Statistics will then be performed on the data to indicate countries of origin for the artist

    Globals:
        playlists: A List of type str used to store what playlist names will be used to acquire artist names

    Privates:
        _instance_ID: An integer from range [0:] that states what instance of Linguify this is
        _file_name: A str that contains the folder path
        _num_of_playlists: An integer from range [0:] that provides the number of playlists that will be contained in global var playlists
    """
    playlists: List[str]

    #instance is an integer of range 0 and above
    def __init__(self, instance: int = 0, fileName: str = "", numOfPlaylists: int = 1) -> None:
        self._instance_ID = instance
        self._file_name = fileName
        self._num_of_playlists = numOfPlaylists
        self.file: io.TextIOWrapper


    def run(self) -> None:
        """
        Orchestrates the full pipeline:
        1. Reads playlist data, extracting unique artists and mapping them to their occurrence counts.
        2. Makes an API call to ChatGPT to deduce each artist's country of origin.
        3. Maps countries of origin to total occurrence counts.
        4. Performs statistical analysis on the resulting data.
        """
        self.readPlaylistData()

    def readPlaylistData(self) -> None:
        """
        Opens the playlist file, extracts artist information, and builds:
        1. A list of unique artists.
        2. A mapping of each artist to the number of times they appear in the playlist.
        """
        try:
            self.openFile()
            # get artist names function
        finally:
            self.file.close()

    def openFile(self) -> None:
        """
        Opens the playlist file and assigns the file object to self.file.

        Raises:
            FileNotFoundError: If the file cannot be found.
            IOError: If an I/O error occurs while opening the file.
            Exception: For any other unknown errors.
        """
        try:
            self.file = open(self._file_name, "r")
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find the file named {self._file_name}")
        except IOError:
            raise IOError("An IO error occurred trying to read the file")
        except Exception as ex:
            raise Exception(f"An unknown exception occurred: {ex}")

    def extractArtistData(self) -> None:
        pass

    #basic getters and setters
    @property
    def instance_ID(self) -> int:
        """Gets the Instance ID"""
        return self._instance_ID
    
    @instance_ID.setter
    def instance_ID(self, id: int) -> None:
        """Sets the instance id while checking for TypeError and ValueError"""
        if not isinstance(id, int):
            raise TypeError(f"Type of parameter 'id' is not valid {type(id)} was given instead of int")
        if id < 0:
            raise ValueError("instance_ID must be a non-negative integer.")
        self._instance_ID = id
    
    @property
    def file_name(self):
        """Gets the file name"""
        return self._file_name
    
    @file_name.setter
    def file_name(self, fileName: str) -> None:
        """Sets the file name while checking for TypeError"""
        if not isinstance(fileName, str):
            raise TypeError(f"Type of parameter 'fileName' is not valid {type(fileName)} was given instead of str")
        self._file_name = fileName


    @property
    def num_of_playlists(self):
        """Gets the number of playlists that will be checked for artist data"""
        return self._num_of_playlists
    
    @num_of_playlists.setter
    def num_of_playlists(self, num: int) -> None:
        """
        Sets the number of playlists that will be checked for artist data and checks for 
        TypeError and ValueError
        """
        if not isinstance(num, int):
            raise TypeError(f"Type of parameter 'num' is not valid {type(num)} was given instead of int")
        if num < 0:
            raise ValueError("num_of_playlists must be a non-negative integer.")
        self._num_of_playlists = num


    def set_playlists(self, playlists: list) -> None:
        """
        sets the playlist list within the Linguify class

        Raises:
            ValueError: If the length of the playlist provided is not equal to the declared length of the playlist in the Linguify class
        """
        if len(playlists) != self._num_of_playlists:
            raise ValueError(f"Size of 'playlists'[set value: {self._num_of_playlists}] provided as a parameter does not match size of playlist "
                                f"set in class Linguify[expected size of playlists: {len(playlists)}]...")
        self.playlists = playlists
     