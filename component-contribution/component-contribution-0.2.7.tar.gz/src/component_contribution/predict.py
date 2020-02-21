"""module for component-contribution predictions."""
# The MIT License (MIT)
#
# Copyright (c) 2013 The Weizmann Institute of Science.
# Copyright (c) 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
# Copyright (c) 2018 Institute for Molecular Systems Biology,
# ETH Zurich, Switzerland.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import logging
from collections import namedtuple
from typing import Dict, List, Tuple

import numpy as np
import quilt
from equilibrator_cache import (
    FARADAY,
    Q_,
    Compound,
    CompoundCache,
    R,
    Reaction,
    ureg,
)
from requests.exceptions import ConnectionError

from . import DEFAULT_QUILT_PKG, DEFAULT_QUILT_VERSION


logger = logging.getLogger(__name__)

CCModelParameters = namedtuple(
    "CCModelParameters",
    "train_b train_S train_w train_G "
    "group_definitions "
    "dG0_rc dG0_gc dG0_cc cov_dG0 "
    "V_rc V_gc V_inf MSE "
    "P_R_rc P_R_gc P_N_rc P_N_gc "
    "inv_S inv_GS inv_SWS inv_GSWGS "
    "G1 G2 G3 "
    "preprocess_v_r preprocess_v_g "
    "preprocess_G1 preprocess_G2 preprocess_G3 "
    "preprocess_S preprocess_S_count "
    "preprocess_C1 preprocess_C2 preprocess_C3",
)


class GibbsEnergyPredictor(object):
    """A class that can be used to predict dGs of reactions using CC."""

    def __init__(
        self, ccache: CompoundCache, parameters: CCModelParameters = None
    ):
        """Create a GibbsEnergyPredictor object.

        ccache : CompoundCache
            The compound cache used for looking up structures and pKas.
        parameters : CCModelParameters
            Optional CC parameters. If not provided, the parameters are
            automatically downloaded from quilt.
        """
        self.ccache = ccache

        if parameters is None:
            self.params = GibbsEnergyPredictor.quilt_fetch()
        else:
            self.params = parameters

        group_names = self.params.group_definitions.full_name.tolist()

        # store the number of "real" groups, i.e. not including the "fake"
        # ones that are placeholders for undecomposable compounds
        self.Ng = len(group_names)

        # the total number of groups ("real" and "fake")
        self.Nc, self.Ng_full = self.params.train_G.shape

        self._compound_ids = self.params.train_G.index.tolist()

        self.MSE_inf = self.params.MSE.at["inf", "MSE"]

    def get_compound_index(self, compound: Compound) -> int:
        """Get the index of a compound in the original training data.

        :param compound: a Compound object
        :return: the index of that compound, or -1 if it was not in the
        training list
        """
        if compound.id in self._compound_ids:
            return self._compound_ids.index(compound.id)
        else:
            return -1

    def get_compound(self, i: int) -> Compound:
        """Get a Compound that was in the original training data.

        :param i: the index of that Compound
        :return: the Compound object
        """
        return self.ccache.get_compound_by_internal_id(self._compound_ids[i])

    @staticmethod
    def quilt_fetch(
        package: str = DEFAULT_QUILT_PKG,
        overwrite: bool = True,
        version: str = DEFAULT_QUILT_VERSION,
    ) -> CCModelParameters:
        """Get the CC parameters from quilt.

        Parameters
        ----------
        package : str, optional
            The quilt data package used to initialize the
            component-contribution data.
        overwrite : bool, optional
            Re-download the quilt data if a newer version exists (default).
        version : str, optional
            The version of the quilt data package.

        :return: a CCModelParameters object

        """
        try:
            logger.info("Fetching Component-Contribution parameters...")
            quilt.install(package, version=version, force=overwrite)
        except ConnectionError:
            logger.error(
                "No internet connection available. Attempting to use "
                "the existing component contribution model."
            )
        except PermissionError:
            logger.error(
                "You do not have the necessary filesystem permissions to "
                "download an update to the quilt data. Attempting to use the "
                "existing component contribution model."
            )
        pkg = quilt.load(package)

        param_dict = {k: v() for k, v in pkg.parameters._children.items()}
        return CCModelParameters(**param_dict)

    def standard_dgf(self, compound: Compound) -> ureg.Measurement:
        """Calculate the chemical formation energy of the major MS at pH 7.

        :param compound: a compound object
        :return: a tuple of two arrays. the first is a 1D NumPy array
        containing the CC estimates for the reactions' untransformed dG0
        (i.e. using the major MS at pH 7 for each of the reactants).
        the second is a 2D numpy array containing the covariance matrix
        of the standard errors of the estimates. one can use the eigenvectors
        of the matrix to define a confidence high-dimensional space, or use
        U as the covariance of a Gaussian used for sampling
        (where dG0_cc is the mean of that Gaussian).
        """
        return self.standard_dg(Reaction({compound: 1}))

    @ureg.check(None, None, "", "[concentration]", "[temperature]")
    def standard_dgf_prime(
        self, compound: Compound, p_h: Q_, ionic_strength: Q_, temperature: Q_
    ) -> ureg.Measurement:
        """Calculate the biocheimcal formation energy of the compound.

        :param compound: a compound object
        :param p_h:
        :param ionic_strength: in M
        :param temperature: temperature in Kalvin
        :return: a tuple of two arrays. the first is a 1D NumPy array
        containing the CC estimates for the reactions' untransformed dG0
        (i.e. using the major MS at pH 7 for each of the reactants).
        the second is a 2D numpy array containing the covariance matrix
        of the standard errors of the estimates. one can use the eigenvectors
        of the matrix to define a confidence high-dimensional space, or use
        U as the covariance of a Gaussian used for sampling
        (where dG0_cc is the mean of that Gaussian).
        """
        return self.standard_dg_prime(
            Reaction({compound: 1}),
            p_h=p_h,
            ionic_strength=ionic_strength,
            temperature=temperature,
        )

    def _decompose_reaction(
        self, reaction: Reaction
    ) -> Tuple[np.array, np.array]:
        """Decompose a reaction.

        :param reaction: the input Reaction object
        :return: a tuple (x, g) of the stoichiometric vector and group
        incidence vector
        """
        x = np.zeros(self.Nc)
        total_gv = np.zeros(self.Ng)

        for compound, coefficient in reaction.items(protons=False):
            i = self.get_compound_index(compound)
            if i >= 0:
                # This compound is in the training set so we can use reactant
                # contributions for it
                x[i] = coefficient
            elif not compound.group_vector:
                raise ValueError(
                    f"The compound {compound} cannot be " f"decomposed"
                )
            else:
                total_gv += coefficient * np.array(
                    compound.group_vector, dtype=float
                )
        return x, total_gv

    def dg_analysis(self, reaction: Reaction) -> List[Dict[str, object]]:
        """Analyse the contribution of each training observation to the dG0.

        :param reaction: the input Reaction object
        :return: a list of reactions that contributed to the value of the dG0
        estimation, with their weights and extra information
        """
        G1 = self.params.preprocess_G1
        G2 = self.params.preprocess_G2
        G3 = self.params.preprocess_G3
        S = self.params.preprocess_S
        S_count = self.params.preprocess_S_count

        try:
            x, g = self._decompose_reaction(reaction)
        except ValueError:
            return []

        # dG0_cc = (x*G1 + x*G2 + g*G3)*b
        weights_rc = (x @ G1).round(5)
        weights_gc = (x @ G2 + g @ G3[0 : self.Ng, :]).round(5)
        weights = abs(weights_rc) + abs(weights_gc)

        analysis = []
        for j in reversed(np.argsort(weights)):
            if abs(weights[j]) < 1e-5:
                continue
            r = {i: S[i, j] for i in range(S.shape[0]) if S[i, j] != 0}
            analysis.append(
                {
                    "index": j,
                    "w_rc": weights_rc[j],
                    "w_gc": weights_gc[j],
                    "reaction": r,
                    "count": int(S_count[j]),
                }
            )

        return analysis

    def is_using_group_contribution(self, reaction: Reaction) -> bool:
        """Check if group contributions was required to estimate the dG0.

        :param reaction: the input Reaction object
        :return: boolean answer
        """
        try:
            x, g = self._decompose_reaction(reaction)
        except ValueError:
            return False

        G2 = self.params.preprocess_G2
        G3 = self.params.preprocess_G3
        weights_gc = x @ G2 + g @ G3[0 : self.Ng, :]
        sum_w_gc = sum(abs(weights_gc).flat)
        logging.info("sum(w_gc) = %.2g" % sum_w_gc)
        return sum_w_gc > 1e-5

    def standard_dg_multi(
        self, reactions: List[Reaction]
    ) -> Tuple[np.array, np.array]:
        """Calculate the chemical reaction energies for a list of reactions.

        Using the major microspecies of each of the reactants.

        :param reactions: a list of Reaction objects
        :return: a tuple of two arrays. the first is a 1D NumPy array
        containing the CC estimates for the reactions' untransformed dG0
        (i.e. using the major MS at pH 7 for each of the reactants).
        the second is a 2D numpy array containing the covariance matrix
        of the standard errors of the estimates. one can use the eigenvectors
        of the matrix to define a confidence high-dimensional space, or use
        U as the covariance of a Gaussian used for sampling
        (where dG0_cc is the mean of that Gaussian).
        """
        Nr = len(reactions)
        X = np.zeros((self.Nc, Nr))
        G = np.zeros((self.Ng_full, Nr))

        non_decomposed_reactions = []
        for i, reaction in enumerate(reactions):
            try:
                x, g = self._decompose_reaction(reaction)
                X[:, i] = x
                G[: self.Ng, i] = g
            except ValueError:
                non_decomposed_reactions.append(i)

        v_r = self.params.preprocess_v_r
        v_g = self.params.preprocess_v_g
        C1 = self.params.preprocess_C1
        C2 = self.params.preprocess_C2
        C3 = self.params.preprocess_C3

        standard_dg = X.T @ v_r + G.T @ v_g
        cov_dg = X.T @ C1 @ X + X.T @ C2 @ G + G.T @ C2.T @ X + G.T @ C3 @ G

        standard_dg[non_decomposed_reactions] = 0
        cov_dg[non_decomposed_reactions, :] = self.MSE_inf
        cov_dg[:, non_decomposed_reactions] = self.MSE_inf

        standard_dg = Q_(standard_dg, "kJ/mol")
        cov_dg = Q_(cov_dg, "(kJ/mol)**2")
        return standard_dg, cov_dg

    @ureg.check(None, None, "", "[concentration]", "[temperature]")
    def standard_dg_prime_multi(
        self,
        reactions: List[Reaction],
        p_h: Q_,
        ionic_strength: Q_,
        temperature: Q_,
    ) -> Tuple[np.array, np.array]:
        """Calculate the transformed reaction energies of a list of reactions.

        :param reactions: a list of Reaction objects
        :param p_h:
        :param ionic_strength:
        :param temperature:
        :return: a tuple of two arrays. the first is a 1D NumPy array
        containing the CC estimates for the reactions' transformed dG0
        the second is a 2D numpy array containing the covariance matrix
        of the standard errors of the estimates. one can use the eigenvectors
        of the matrix to define a confidence high-dimensional space, or use
        U as the covariance of a Gaussian used for sampling
        (where dG0_cc is the mean of that Gaussian).
        """
        standard_dg, U = self.standard_dg_multi(reactions)

        for i, r in enumerate(reactions):
            standard_dg[i] += (
                R * temperature * r.transform(p_h, ionic_strength, temperature)
            )

        return standard_dg, U

    def standard_dg(self, reaction: Reaction) -> ureg.Measurement:
        """Calculate the chemical reaction energy.

        Using the major microspecies of each of the reactants.

        :param reaction: the input Reaction object
        :return: a tuple with the CC estimation of the major microspecies'
        standard formation energy, and the uncertainty
        """
        standard_dg, cov_dg = self.standard_dg_multi([reaction])
        standard_dg = standard_dg[0].plus_minus(np.sqrt(cov_dg[0, 0]))
        return standard_dg

    @ureg.check(None, None, "", "[concentration]", "[temperature]")
    def standard_dg_prime(
        self, reaction: Reaction, p_h: Q_, ionic_strength: Q_, temperature: Q_
    ) -> ureg.Measurement:
        """Calculate the transformed reaction energies of a reaction.

        :param reaction: the input Reaction object
        :param p_h:
        :param ionic_strength: in M
        :param temperature: temperature in Kalvin
        :return: a tuple of the dG0_prime in kJ/mol and standard error. to
        calculate the confidence interval, use the range -1.96 to 1.96 times
        this value
        """
        standard_dg, cov_dg = self.standard_dg_prime_multi(
            [reaction],
            p_h=p_h,
            ionic_strength=ionic_strength,
            temperature=temperature,
        )
        standard_dg = standard_dg[0].plus_minus(np.sqrt(cov_dg[0, 0]))
        return standard_dg

    @ureg.check(
        None,
        None,
        None,
        None,
        None,
        "",
        "",
        "[concentration]",
        "[concentration]",
        "[energy]/[current]/[time]",
        "[temperature]",
    )
    def multicompartmental_standard_dg_prime(
        self,
        reaction_1: Reaction,
        reaction_2: Reaction,
        transported_protons: float,
        transported_charge: float,
        p_h_1: Q_,
        p_h_2: Q_,
        ionic_strength_1: Q_,
        ionic_strength_2: Q_,
        delta_chi: Q_,
        temperature: Q_,
    ) -> ureg.Measurement:
        """Calculate the transformed energies of a multi-compartmental reaction.

        Based on the equations from
        Harandsdottir et al. 2012 (https://doi.org/10.1016/j.bpj.2012.02.032)

        :param reaction_1: half-reaction associated to compartment 1
        :param reaction_2: half-reaction associated to compartment 2
        :param transported_protons: the total number of protons
        transported through the membrane
        :param transported_charge: the total charge
        transported through the membrane
        :param p_h_1: the pH in compartment 1
        :param p_h_2: the pH in compartment 2
        :param ionic_strength_1: the ionic strength in compartment 1
        :param ionic_strength_2: the ionic strength in compartment 2
        :param delta_chi: electrostatic potential across the membrane
        :param temperature: temperature in Kalvin
        :return:
        """
        standard_dg, cov_dg = self.standard_dg_multi([reaction_1, reaction_2])

        # the contribution of the chemical reaction to the standard ΔG' is
        # the sum of the two half reactions and the variance is the sum
        # of all the values in cov_dg. For the uncertainty we take the square
        # root of the sum.

        uncertainty = np.sqrt(np.sum(cov_dg.flat))
        standard_dg = (standard_dg[0] + standard_dg[1]).plus_minus(uncertainty)

        # Here we calculate the transform (since the two reactions are in
        # different pH and I, we have to do it here):
        transform_dg_over_rt = 0.0
        for compound, coeff in reaction_1.items(protons=False):
            transform_dg_over_rt += coeff * compound.transform(
                p_h_1, ionic_strength_1, temperature
            )

        for compound, coeff in reaction_2.items(protons=False):
            transform_dg_over_rt += coeff * compound.transform(
                p_h_2, ionic_strength_2, temperature
            )

        transform_dg = (R * temperature * transform_dg_over_rt).to("kJ/mol")

        dg_protons = (
            transported_protons
            * R
            * temperature
            * np.log(10.0)
            * (p_h_2 - p_h_1)
        ).to("kJ/mol")

        dg_electrostatic = (FARADAY * transported_charge * delta_chi).to(
            "kJ/mol"
        )

        standard_dg += transform_dg - dg_protons - dg_electrostatic
        return standard_dg
