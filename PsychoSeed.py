import logging

import yaml
import os
import Utils
import zipfile

from .Items import item_dictionary_table
from .Locations import all_locations
from worlds.Files import APContainer

class PSYContainer(APContainer):
    game: str = 'Psychonauts'

    def __init__(self, patch_data: str, base_path: str, output_directory: str,
        player=None, player_name: str = "", server: str = ""):
        self.patch_data = patch_data

        # file name ALWAYS RandoSeed.lua for randomizer to find
        self.seed_file_name = f"RandoSeed.lua"
        container_path = os.path.join(output_directory, self.seed_file_name)
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        
        opened_zipfile.writestr(self.seed_file_name, self.patch_data)
        super().write_contents(opened_zipfile)


def gen_psy_seed(self, output_directory):

    mod_name = f"AP-{self.multiworld.seed_name}-P{self.player}-{self.multiworld.get_file_safe_player_name(self.player)}"

    randoseed_parts = []

    # First part of lua code structure
    formattedtext1 = '''function RandoSeed(Ob)
        if ( not Ob ) then
            Ob = CreateObject('ScriptBase')
            Ob.seed = {}
        '''
    randoseed_parts.append(formattedtext1)

    # append mod_name 
    randoseed_parts.append(f"   Ob.seedname = '{mod_name}'\n")

    # append startlevitation setting, make boolean uppercase for Game
    self.multiworld.StartingLevitation[self.player]
    startlevitationsetting = str(self.multiworld.StartingLevitation[self.player]).upper()
    randoseed_parts.append(f"   Ob.startlevitation = {startlevitationsetting}\n")


    # append instantdeath setting, make boolean uppercase for Game
    instantdeathsetting = str(self.multiworld.InstantDeathMode[self.player]).upper()
    randoseed_parts.append(f"   Ob.instantdeath = {instantdeathsetting}\n")
    
    # Section where default settings booleans are written to RandoSeed.lua
    # adding new settings will remove from this list
    default_seed_settings = '''
        Ob.startcobweb = FALSE
        Ob.startbutton = FALSE
        Ob.randomizecobwebduster = TRUE
        Ob.everylocationpossible = FALSE
        Ob.harderbutton = FALSE
        Ob.beatoleander = TRUE
        Ob.beatalllevels = FALSE
        Ob.rank101 = FALSE
        Ob.brainhunt = FALSE
        Ob.scavengerhunt = FALSE
        Ob.fasterLO = TRUE
        Ob.easymillarace = FALSE
        Ob.earlyelevator = FALSE
        Ob.mentalmagnet = TRUE
        Ob.removetutorials = TRUE
        Ob.easyflight = FALSE
        Ob.createhints = FALSE
        Ob.spoilerlog = FALSE
    end
    '''
    randoseed_parts.append(default_seed_settings)

    # more lua code structure
    formattedtext2 = '''

    function Ob:fillTable()
    local SEED_GOES_HERE = {
    
    
    '''

    randoseed_parts.append(formattedtext2)
    
    # append the item values, need to be in exact order
    # locations are handled by index in table
    # items from other games need to be converted to a new value
    # Starting at 368, +1 each time
    non_local_id = 368
    index = 1

    for location in self.multiworld.get_filled_locations(self.player):
        
        if location.item:
            if location.item.player == self.player:
                # ignore the victory location for now
                if location.item.name != "Victory":
                    # need this to make itemcode = item id - 42690000
                    itemcode = item_dictionary_table[location.item.name]
            else:
                # item from another game
                itemcode = non_local_id
                non_local_id = non_local_id + 1 
        else:
            # item from another game
            itemcode = non_local_id
            non_local_id = non_local_id + 1 

        # append the item code   
        randoseed_parts.append(str(itemcode))
        # format so that each line has 10 values, for readability
        if index % 10 == 0:
            randoseed_parts.append(",\n")
        else:
            randoseed_parts.append(", ")

        index = index + 1

    # old generator method
    # for i, value in enumerate(seed, start=1):
    #    randoseed +=  str(value))
    #    if i % 10 == 0:
    #        randoseed +=  ",\n")
    #    else:
    #        randoseed +=  ", ")

    # last part of coding structure
    formattedtext3 = ''' }
        self.seed = SEED_GOES_HERE
        end
        return Ob
    end

    '''

    randoseed_parts.append(formattedtext3)

    # Combine all the parts into one long piece of text
    randoseed = ''.join(randoseed_parts)
    
    mod_dir = os.path.join(output_directory, mod_name + "_" + Utils.__version__)

    mod = PSYContainer(randoseed, mod_dir, output_directory, self.player,
            self.multiworld.get_file_safe_player_name(self.player))
    mod.write()