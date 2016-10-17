# gaia_astero
Catalogues of Gaia stars with asteroseismic parameters.

Installation
------------

>>> git clone https://github.com/RuthAngus/gaia_astero.git
>>> cd gaia_astero
>>> python setup.py install

To get the Gaia-astero catalogues as a pandas dataframe:

    >>> import gaia_astero
    >>> ga = gaia_astero.gaia_astero()

    >>> solar_like_star_df = ga.solarlike  # just the solar-like stars
    >>> red_giant_star_df = ga.redgiant  # just the red giants
    >>> all_star_df = ga.all_stars  # all the stars

To get the properties of a single star, use the star function with the Kepler
id, e.g.:

    >>> properties_df = ga.star("757137")

or its 2MASS designation:

    >>> properties_df = ga.star("2MASS J19241341+3633358")

If you want, say, the age of a star, do:

    >>> age = properties_df.age

Column headings:

kepid, nu_max, delta_nu, tm_designation, teff, teff_err1, teff_err2, logg,
logg_err1, logg_err2, feh, feh_err1, feh_err2, mass, mass_err1, mass_err2,
radius, radius_err1, radius_err2, dens, dens_err1, dens_err2, prov_sec,
kepmag, dist, dist_err1, dist_err2, nconfp, nkoi, ntce, datalink_dvr,
st_delivname, st_vet_date_str, ra, dec, st_quarters, teff_prov, logg_prov,
feh_prov, jmag, jmag_err, hmag, hmag_err, kmag, kmag_err, dutycycle, dataspan,
mesthres01p5, mesthres02p0, mesthres02p5, mesthres03p0, mesthres03p5,
mesthres04p5, mesthres05p0, mesthres06p0, mesthres07p5, mesthres09p0,
mesthres10p5, mesthres12p0, mesthres12p5, mesthres15p0, rrmscdpp01p5,
rrmscdpp02p0, rrmscdpp02p5, rrmscdpp03p0, rrmscdpp03p5, rrmscdpp04p5,
rrmscdpp05p0, rrmscdpp06p0, rrmscdpp07p5, rrmscdpp09p0, rrmscdpp10p5,
rrmscdpp12p0, rrmscdpp12p5, rrmscdpp15p0, av, av_err1, av_err2, tgas_hip,
tgas_tycho2_id, tgas_solution_id, tgas_source_id, tgas_random_index,
tgas_ref_epoch, tgas_ra, tgas_ra_error, tgas_dec, tgas_dec_error,
tgas_parallax, tgas_parallax_error, tgas_pmra, tgas_pmra_error, tgas_pmdec,
tgas_pmdec_error, tgas_ra_dec_corr, tgas_ra_parallax_corr, tgas_ra_pmra_corr,
tgas_ra_pmdec_corr, tgas_dec_parallax_corr, tgas_dec_pmra_corr,
tgas_dec_pmdec_corr, tgas_parallax_pmra_corr, tgas_parallax_pmdec_corr,
tgas_pmra_pmdec_corr, tgas_astrometric_n_obs_al, tgas_astrometric_n_obs_ac,
tgas_astrometric_n_good_obs_al, tgas_astrometric_n_good_obs_ac,
tgas_astrometric_n_bad_obs_al, tgas_astrometric_n_bad_obs_ac,
tgas_astrometric_delta_q, tgas_astrometric_excess_noise,
tgas_astrometric_excess_noise_sig, tgas_astrometric_primary_flag,
tgas_astrometric_relegation_factor, tgas_astrometric_weight_al,
tgas_astrometric_weight_ac, tgas_astrometric_priors_used,
tgas_matched_observations, tgas_duplicated_source,
tgas_scan_direction_strength_k1, tgas_scan_direction_strength_k2,
tgas_scan_direction_strength_k3, tgas_scan_direction_strength_k4,
tgas_scan_direction_mean_k1, tgas_scan_direction_mean_k2,
tgas_scan_direction_mean_k3, tgas_scan_direction_mean_k4,
tgas_phot_g_n_obs, tgas_phot_g_mean_flux, tgas_phot_g_mean_flux_error,
tgas_phot_g_mean_mag, tgas_phot_variable_flag, tgas_l, tgas_b, tgas_ecl_lon,
tgas_ecl_lat, tgas_match_distance
