"""Defines workflow routing methods, to be used by route_strategy."""
# NOTE: Change these functions to perform custom routing to your workflows and
# steps in your environment. wf_steps.WF_STEPS must also be updated.

import logging
from ua_project_transfer import wf_steps

LOGGER = logging.getLogger("project_creation.next_steps")


def agena(payload):
    """Routes samples to different steps in the Agena workflow."""
    if payload["form"].field_to_values[
            "Sample_Type_each_sample"] == "cells":
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["agena"]["cells"],
            payload["art_uris"])
    else:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["agena"]["gdna"],
            payload["art_uris"])


def bioanalyzer(payload):
    """Routes samples to different steps in the Bioanalyzer workflow."""
    if payload["form"].field_to_values["Sample_Type_each_sample"] == "DNA":
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["bioanalyzer"]["DNA"],
            payload["art_uris"])
    else:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["bioanalyzer"]["RNA"],
            payload["art_uris"])


def cla(payload):
    """Routes samples to different steps in the CLA workflow."""
    if payload["form"].field_to_values[
            "Sample_Type_each_sample"] == "cells":
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["cla"]["cells"],
            payload["art_uris"])
    else:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["cla"]["gdna"],
            payload["art_uris"])


def extraction(payload):
    """Routes samples to the sort steps in the Extraction workflows."""
    if "DNA" in payload["form"].name:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["extraction"]["DNA"],
            payload["art_uris"])
    else:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["extraction"]["RNA"],
            payload["art_uris"])


def frag(payload):
    """Routes samples to different steps in the Frag workflow."""
    # Route to the 4-dye workflow.
    if (payload["form"].field_to_values[
            "DYE_Set_each_sample"] == "D (4-dye)"):
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["frag"]["4dye"],
            payload["art_uris"])
    # Route to the 5-dye worklow.
    elif (payload["form"].field_to_values[
            "DYE_Set_each_sample"] == "G5 (5-dye)"):
        if (payload["form"].field_to_values[
                "size_standard_5dye"] == "GS1200"):
            payload["lims_api"].tools.step_router(
                *wf_steps.WF_STEPS[payload["env"]]["frag"]["GS1200"],
                payload["art_uris"])
        else:
            payload["lims_api"].tools.step_router(
                *wf_steps.WF_STEPS[payload["env"]]["frag"]["5dye"],
                payload["art_uris"])
    else:
        LOGGER.warning({
            "template": "route_warning.html",
            "content": (
                f"The request {payload['form'].req_id} has been completed"
                f" incorrectly; it must have one of the preset values for the"
                f" dye set.")
        })


def hvs(payload):
    """Routes samples to different steps in the HVS workflow."""
    if payload["form"].field_to_values["clean_pcr"] == "true":
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["hvs"]["clean_pcr"],
            payload["art_uris"])
    else:
        if payload["form"].field_to_values["quant_norm"] == "true":
            payload["lims_api"].tools.step_router(
                *wf_steps.WF_STEPS[
                    payload["env"]]["hvs"]["quant_norm"],
                payload["art_uris"])
        else:
            if (payload["form"].field_to_values[
                    "Template_in_multi_each_sample"] is True):
                payload["lims_api"].tools.step_router(
                    *wf_steps.WF_STEPS[
                        payload["env"]]["hvs"]["multi"],
                    payload["art_uris"])
            else:
                payload["lims_api"].tools.step_router(
                    *wf_steps.WF_STEPS[
                        payload["env"]]["hvs"]["default"],
                    payload["art_uris"])


def nanostring(payload):
    """Routes samples to the first step in the Nanostring workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["nanostring"],
        payload["art_uris"])


def lvs(payload):
    """Routes samples to the first step in the LVS workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["lvs"],
        payload["art_uris"])


def quant(payload):
    """Routes samples to different steps in the Quant workflow."""
    if payload["form"].field_to_values[
            "Sample_Type"] == "gDNA":
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["quant"]["gdna"],
            payload["art_uris"])
    else:
        payload["lims_api"].tools.step_router(
            *wf_steps.WF_STEPS[payload["env"]]["quant"]["post"],
            payload["art_uris"])


def ribotyping(payload):
    """Routes samples to the first step in the DNAExtraction workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["ribotyping"],
        payload["art_uris"])


def tgm(payload):
    """Routes samples to the first step of the TGM workflow."""
    payload["lims_api"].tools.step_router(
        *wf_steps.WF_STEPS[payload["env"]]["tgm"],
        payload["art_uris"])
