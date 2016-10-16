import numpy as np
import pandas as pd
import astropy.constants as const
import astropy.units as u
import matplotlib.pyplot as plt


def match(id1, id2):
    """
    Returns the positions of matching id1s in the id1 and id2 arrays.
    """
    inds1, inds2 = [], []
    for i, id in enumerate(id1):
        m = id2 == id
        if len(id2[m]):
            inds1.append(i)
            inds2.append(np.where(m)[0][0])
    return inds1, inds2


def replace(id1, id2, table1, table2):
    """
    Match tables by ids and replace rows in table2 with rows in table1.
    Table1 is a subset of table2.
    """
    inds1, inds2 = match(id1, id2)
    for i, ind in enumerate(inds2):
        table2[inds2[i], :] = table1[inds1[i], :]
    return table2


def err_prop(mass, rad, mass_err, rad_err, func):
    errs = np.empty_like(mass)
    for i, err in enumerate(mass_err):
        mass_samps = err * np.random.randn(1e4) + mass[i]
        rad_samps = rad_err[i] * np.random.randn(1e4) + rad[i]
        x_samps = func(mass_samps, rad_samps)
        errs[i] = np.std(x_samps)
    return errs


def convert(mass, mass_err, rad, rad_err):
    """
    Convert masses and radii to densities, loggs, delta nus and nu maxs.
    """
    logg_f = lambda mass, rad: - np.log10((const.G * mass * u.kg /
                                 (rad * u.m)**2).cgs.value)
    rho_f = lambda mass, rad: mass / (4/3. * np.pi * rad**3)
    delta_nu_f = lambda mass, rad: mass**.5 / rad**(3./2) * 139  # uHz
    # nu_max_f = lambda mass, rad, teff: mass / (rad**2 * (teff/5777)**.5) * \
    #     3.05*1e3
    logg = logg_f(mass, rad)
    logg_err = err_prop(mass, rad, mass_err, rad_err, logg_f)
    rho = rho_f(mass, rad)
    rho_err = err_prop(mass, rad, mass_err, rad_err, rho_f)
    dnu = delta_nu_f(mass, rad)
    dnu_err = err_prop(mass, rad, mass_err, rad_err, delta_nu_f)
    return logg, logg_err, rho, rho_err, dnu, dnu_err


def get_all_astero():
    """
    Load all Solar-like oscillators (short-cadence targets).
    The Metcalfe values take precedence, followed by the Silva-Aguirre values,
    then Chaplin table 6, Chaplin table 5 then Chaplin table 4.
    """
    met = pd.read_csv("met.csv")
    sag = pd.read_csv("sag.csv")
    ct1 = pd.read_csv("chaplin_table1.csv")
    ct2 = pd.read_csv("chaplin_table2.csv")
    ct4 = pd.read_csv("chaplin_table4.csv")
    ct5 = pd.read_csv("chaplin_table5.csv")
    ct6 = pd.read_csv("chaplin_table6.csv")

    # table = replace(ct4["kepid"], ct5["kepid"], np.array(ct4), table)
    # table = replace(ct6["kepid"], table[:, 0], np.array(ct6), table)

    # table = replace(met["kepid"], table[:, 0], np.array(met), table)
    # table = replace(sag["kepid"], table[:, 0], sag, table)

    # table2 = pd.merge(ct5, ct4, how="left", on="kepid", suffixes=["", "_2"])
    # m = table2["age_2"].isnull()
    # table2[~m]["age"] = table2[~m]["age_2"]
    # print(table2)

    m = ct4.kepid.isin(ct5.kepid)
    table = pd.concat([ct5, ct4[~m]])
    m = table.kepid.isin(ct6.kepid)
    table = pd.concat([ct6, table[~m]])
    chap_ref = ["Chaplin et al. (2014)" for i in range(len(table))]
    table["ref"] = chap_ref

    cols = table.columns.tolist()
    met = met[cols]
    m = table.kepid.isin(met.kepid)
    table = pd.concat([met, table[~m]])
    sag = sag[cols]
    m = table.kepid.isin(sag.kepid)
    table = pd.concat([sag, table[~m]])
    table.to_csv("solar-like.csv", index=False)


def format():
    # get the metcalfe and s-a cats in the right format.

    met = pd.read_csv("metcalfe2014.txt")
    logg, logg_err, rho, rho_err, dnu, dnu_err = convert(met["mass"],
                                                         met["mass_err"],
                                                         met["radius"],
                                                         met["radius_err"])
    met_ref = ["Metcalfe et al. (2014)" for i in range(len(met))]

    del met["Z"]
    del met["Z_err"]
    del met["Y"]
    del met["Y_err"]
    del met["alpha"]
    del met["alpha_err"]
    del met["a_0"]
    del met["f"]
    del met["AMP_b"]

    met["mass_errp"] = met["mass_err"]
    met["mass_errm"] = met["mass_err"]
    met["radius_errp"] = met["radius_err"]
    met["radius_errm"] = met["radius_err"]
    met["age_errp"] = met["age_err"]
    met["age_errm"] = met["age_err"]

    del met["mass_err"]
    del met["radius_err"]
    del met["age_err"]

    met['density'] = rho
    met['density_errp'] = rho_err
    met['density_errm'] = rho_err
    met['logg'] = logg
    met['logg_errp'] = logg_err
    met['logg_errm'] = logg_err
    met['ref'] = met_ref

    ct6 = pd.read_csv("chaplin_table6.csv")
    cols = ct6.columns.tolist()
    cols.append("ref")
    met = met[cols]
    met.to_csv("met.csv")

    sag = pd.read_csv("silva-aguirre.txt")
    sag_ref = ["Silva-Aguirre et al. (2014)" for i in range(len(sag))]
    del sag["koi"]
    del sag["teff"]
    del sag["feh"]
    del sag["feh_err"]
    del sag["luminosity"]
    del sag["luminosity_errp"]
    del sag["luminosity_errm"]
    del sag["distance"]
    del sag["distance_errp"]
    del sag["distance_errm"]

    sag["ref"] = sag_ref
    sag = sag[cols]
    sag.to_csv("sag.csv")


if __name__ == "__main__":
    get_all_astero()
    # format()
