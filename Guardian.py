from ParallelGrid import ParallelGrid
from WorkerProcess import WorkerProcess

class Guardian:

    def __init__(self, config_file=None):
        config_json = {}
        if config_file is None:
            config_json = {
                "resolution": 2048,
                "valueDict": {
                    [960, 960]: 200000,
                    [960, 860]: 200000,
                    [860, 960]: 200000,
                    [860, 860]: 200000,
                    [1060, 1060]: 200000,
                    [1060, 960]: 200000,
                    [960, 1060]: 200000,
                    [860, 1060]: 200000,
                    [1060, 860]: 200000,
                }
            }
        else:
            pass # read config file

        self.resolution = config_json["resolution"]
        self.value_dict = config_json["valueDict"]

        self.grid = ParallelGrid(config_json['resolution'], config_json['resolution'], config_json['valueDict'])

        self.spawn_processes()



    def spawn_processes(self):

        # Get dimensions of active region.
        ar_dimm = self.get_active_region_dimensions()

        # Decide how many processes should be spawned
        num_workers = self.determine_num_processes()

        for i in range(num_workers):


    def run(self):
        pass
