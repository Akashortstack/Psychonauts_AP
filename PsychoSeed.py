import logging

import yaml
import os
import Utils

from .Items import item_dictionary_table
from .Locations import all_locations
from worlds.Files import APContainer

class PSYContainer(APContainer):
    game: str = 'Psychonauts'

    def __init__(self, patch_data: dict, base_path: str, output_directory: str,
        player=None, player_name: str = "", server: str = ""):
        self.patch_data = patch_data
        self.file_path = base_path
        container_path = os.path.join(output_directory, base_path + ".lua")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, lua_file_path: str) -> None:
        with open(lua_file_path, 'w') as lua_file:
            for filename, yml in self.patch_data.items():
                lua_file.write(filename + "\n")
                lua_file.write(yml + "\n\n")
        super().write_contents(lua_file_path)



def gen_psy_seed(self, output_directory):

    mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"

    self.formattedSettings = []
    
