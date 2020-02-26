from Bio import SeqIO
import click
from crisprbact.predict import on_target_predict


class Config(object):
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)

OFF_TARGET_DETAILS = [
    "off_target_recid",
    "off_target_start",
    "off_target_end",
    "off_target_pampos",
    "off_target_strand",
    "off_target_feat_type",
    "off_target_feat_start",
    "off_target_feat_end",
    "off_target_feat_strand",
    "off_target_locus_tag",
    "off_target_gene",
    "off_target_note",
    "off_target_product",
    "off_target_protein_id",
]
HEADER = [
    "target_id",
    "target",
    "PAM position",
    "prediction",
    "target_seq_id",
    "seed_size",
] + OFF_TARGET_DETAILS
SEED_SIZE = 8
GENOME_FORMAT = "genbank"


@click.group()
@click.option("-v", "--verbose", is_flag=True)
@pass_config
def main(config, verbose):
    config.verbose = verbose


@main.group()
@pass_config
def predict(config):
    pass


@predict.command()
@click.option(
    "-t", "--target", type=str, required=True, help="Sequence file to target",
)
@click.option(
    "-s",
    "--off-target-sequence",
    type=click.File("rU"),
    help="Sequence in which you want to find off-targets",
)
@click.option(
    "-w",
    "--off-target-sequence-format",
    type=click.Choice(["fasta", "gb", "genbank"]),
    default=GENOME_FORMAT,
    show_default=True,
    help="Sequence in which you want to find off-targets format",
)
@click.argument("output-file", type=click.File("w"), default="-")
@pass_config
def from_str(
    config, target, off_target_sequence, off_target_sequence_format, output_file
):
    """
    Outputs candidate guide RNAs for the S. pyogenes dCas9 with predicted on-target
    activity from a target gene.

    [OUTPUT_FILE] file where the candidate guide RNAs are saved. Default = "stdout"

    """
    if config.verbose:
        print_parameters(target)
    if off_target_sequence:
        genome_fh = SeqIO.parse(off_target_sequence, off_target_sequence_format)
    else:
        genome_fh = None
    guide_rnas = on_target_predict(target, genome_fh)

    click.echo("\t".join(HEADER), file=output_file)
    write_guide_rnas(guide_rnas, output_file)


@predict.command()
@click.option(
    "-t",
    "--target",
    type=click.File("rU"),
    required=True,
    help="Sequence file to target",
)
@click.option(
    "-f",
    "--seq-format",
    type=click.Choice(["fasta", "gb", "genbank"]),
    help="Sequence file to target format",
    default="fasta",
    show_default=True,
)
# @click.option(
#     "-s", "--seed-size", type=click.IntRange(8, 15, clamp=True),
# )
@click.option(
    "-s",
    "--off-target-sequence",
    type=click.File("rU"),
    help="Sequence in which you want to find off-targets",
)
@click.option(
    "-w",
    "--off-target-sequence-format",
    type=click.Choice(["fasta", "gb", "genbank"]),
    default=GENOME_FORMAT,
    show_default=True,
    help="Sequence in which you want to find off-targets format",
)
@click.argument("output-file", type=click.File("w"), default="-")
@pass_config
def from_seq(
    config,
    target,
    seq_format,
    off_target_sequence,
    off_target_sequence_format,
    output_file,
):
    """
    Outputs candidate guide RNAs for the S. pyogenes dCas9 with predicted on-target
    activity from a target gene.

    [OUTPUT_FILE] file where the candidate guide RNAs are saved. Default = "stdout"

    """
    fg = "blue"
    if config.verbose:
        print_parameters(target.name, fg)
    click.echo("\t".join(HEADER), file=output_file)
    for record in SeqIO.parse(target, seq_format):
        if config.verbose:
            click.secho(" - search guide RNAs for %s " % record.id, fg=fg)
        if off_target_sequence:
            genome_fh = SeqIO.parse(off_target_sequence, off_target_sequence_format)
        else:
            genome_fh = None
        guide_rnas = on_target_predict(str(record.seq), genome_fh)
        # print(guide_rnas)
        write_guide_rnas(guide_rnas, output_file, record.id)


def print_parameters(target, fg="blue"):
    click.secho("[Verbose mode]", fg=fg)
    click.secho("Target sequence : %s" % target, fg=fg)


def write_guide_rnas(guide_rnas, output_file, seq_id="N/A"):
    for guide_rna in guide_rnas:
        row = [
            str(guide_rna["target_id"]),
            guide_rna["target"],
            str(guide_rna["pam"]),
            str(guide_rna["pred"]),
            seq_id,
        ]
        if len(guide_rna["off_targets_per_seed"]) > 0:
            for off_target_per_seed in guide_rna["off_targets_per_seed"]:
                for off_target in off_target_per_seed["off_targets"]:
                    seed_size = off_target_per_seed["seed_size"]

                    def extract_off_target_detail(key):
                        if key in off_target:
                            return str(off_target[key])
                        else:
                            return ""

                    details = map(extract_off_target_detail, OFF_TARGET_DETAILS)
                    click.echo(
                        "\t".join(row + [str(seed_size)] + list(details)),
                        file=output_file,
                    )
        else:
            click.echo(
                "\t".join(row + list(map(lambda x: "", OFF_TARGET_DETAILS))),
                file=output_file,
            )


if __name__ == "__main__":
    main()
