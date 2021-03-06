import numpy as np
import pandas as pd
from pkg_resources import resource_filename


class gaia_astero(object):
        """
        Method for querying a star to see if has any asteroseismic data.
        The star object has KIC, 2MASS and tycho ids, stellar parameters,
        asteroseismic parameters and gaia parameters.

        get_all_astero() returns a database of all gaia stars with
        asteroseismology.
        """

        def __init__(self):

            rgs = pd.read_csv(resource_filename(__name__,
                                                "apokasc-tgas.csv")
                              )
            self.redgiant = rgs

            sls = pd.read_csv(resource_filename(__name__,
                                                "solar-like-TGAS.csv"))
            self.solarlike = sls

            # self.all_stars = pd.concat([sls, rgs])

        def star(self, id):
            """
            Return the properties of a single star.
            id should be a Kepler id.
            """
            if len(str(id)) > 9:
                id_type = "tm_designation"
                id = str(id)
            else:
                id = int(id)
                id_type = "kepid"

            m = id == self.solarlike[id_type]
            sl = self.solarlike.kepid[m]
            if len(sl[m]):
                print("Solar-like star")
                return self.solarlike.iloc[np.where(m)[0][0]]

            m = id == self.redgiant[id_type]
            rg = self.redgiant[id_type][m]
            print(rg)
            print(id)
            if len(rg[m]):
                print("Red Giant")
                return self.redgiant.iloc[np.where(m)[0][0]]
            else:
                return "Object not found in catalogue. It's either not an " \
                    "asteroseismic target or not in TGAS."


if __name__ == "__main__":
    ga = gaia_astero()
    properties_df = ga.star("J18583782+4822494")
