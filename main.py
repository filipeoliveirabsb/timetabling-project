import numpy as np
import pandas as pd
import random
from ruamel.yaml import YAML


def get_time_table(data, module_name):
    time_table = pd.DataFrame(index=data["agents"], columns=data["days"])

    modules = data["modules"]
    days = data["days"]
    agents = data["agents"]
    schedule = data["module_schedule"]

    shape = (len(modules) * len(days) * len(agents), len(schedule))
    genes = np.zeros(shape, dtype=np.int32)

    module_name = modules.index(module_name)

    team_safe = 1

    for day in range(len(days)):
        for agent in range(len(agents)):
            for sch in range(len(schedule)):
                # indx = agent + day * len(agents) + module_name * len(days) * len(agents)
                # print(sch)

                (module, _, team) = schedule[sch]

                if team == team_safe:
                    time_table.iloc[agent, day] = "{}".format(module)

    return time_table


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_file = "./raw_data.yaml"
    raw_data_file = open(data_file)
    data = YAML().load(raw_data_file.read())
    raw_data_file.close()

    print(data)

    for c in data["modules"]:
        print("module : {}".format(c))
        print(get_time_table(data, c))
