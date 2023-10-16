import re
import json


import json
import re

class OcflInventory():
    """
    A class representing an OCFL inventory.

    Attributes:
    - inventory (dict): The inventory represented as a dictionary.
    """

    def __init__(self, file):
        """
        Initializes an OcflInventory object.

        Args:
        - file (file): The file object containing the inventory data.
        """
        self.inventory = json.load(file)
        

    def get_descriptor_path(self):
        """
        Returns the path to the descriptor file for the object.

        Returns:
        - str: The path to the descriptor file.

        Raises:
        - Exception: If the descriptor file is not found.
        """
        path_regex = r'^v[0-9]{5}/content/descriptor/.*_mets.xml'
        manifest_files = self._get_manifest_files(path_regex)

        if len(manifest_files) > 0:
            return sorted(manifest_files, reverse=True)[0]

        raise Exception("not-found, descriptor")


    def get_data_path(self, file_id):
        """
        Returns the path to the data file for the given file ID.

        Args:
        - file_id (str): The ID of the file.

        Returns:
        - str: The path to the data file.

        Raises:
        - Exception: If the data file is not found.
        """
        path_regex = r'^v[0-9]{5}/content/data/' + file_id + r'.*'
        manifest_files = self._get_manifest_files(path_regex)

        if len(manifest_files) > 0:
            return sorted(manifest_files, reverse=True)[0]

        raise Exception("not-found, data file for: {}".format(file_id))


    def _get_manifest_files(self, path_regex):
        """
        Returns a set of file paths that match the given regular expression.

        Args:
        - path_regex (str): The regular expression to match.

        Returns:
        - set: A set of file paths that match the regular expression.

        Raises:
        - Exception: If the manifest is invalid.
        """
        manifest = self.inventory['manifest']

        if not isinstance(manifest, dict):
            raise Exception('Invalid manifest')
    
        manifest_files = set() 
        for digest in manifest:
            for file in manifest[digest]:
                if (re.search(path_regex, file)):
                    manifest_files.add(file)

        return manifest_files
