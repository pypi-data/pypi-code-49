def read_snps(snps):
    """
    Input SNP coordinates and bases
    Return list of chromosome, position, reference base, alternate base
    """
    data = []
    if snps.endswith(".gz"):
        infile = gzip.open(snps, "rb")
    else:
        infile = open(snps, "r")
    for line in infile:
        line = line.rsplit()
        chromosome = line[0].strip("chr")
        position = int(line[1])
        ref = line[2]
        alt = line[3]
        data.append([chromosome, position, ref, alt])
    infile.close()
    return data


def get_genotype(read, ref_position, snp_position, cigar_tuple):
    """
    Input read position, read sequence, SNP position, cigar
    Return the base in read that is aligned to the SNP position
    """
    cigar = {  # alignement code, ref shift, read shift
        0: ["M", 1, 1],  # match, progress both
        1: ["I", 0, 1],  # insertion, progress read not reference
        2: ["D", 1, 0],  # deletion, progress reference not read
        3: ["N", 1, 0],  # skipped, progress reference not read
        4: ["S", 0, 1],  # soft clipped, progress read not reference
        5: ["H", 0, 0],  # hard clipped, progress neither
        6: ["P", 0, 0],  # padded, do nothing (not used)
        7: ["=", 1, 1],  # match, progress both
        8: ["X", 1, 1],  # mismatch, progress both
    }
    read_position = 0
    for i in cigar_tuple:
        ref_bases = cigar[i[0]][1] * i[1]
        read_bases = cigar[i[0]][2] * i[1]
        if ref_bases == 0 and read_bases == 0:  # this shouldn't ever happen
            pass
        elif (
            ref_bases == 0 and read_bases > 0
        ):  # clipped bases or insertion relative to reference
            read_position += read_bases
            if (
                ref_position == snp_position
            ):  # only happens when first aligned base is the SNP
                return read[read_position - 1]
        elif read_bases == 0 and ref_bases > 0:
            ref_position += ref_bases
            if ref_position > snp_position:  # we've gone past the SNP
                return None
        else:
            if ref_position + ref_bases > snp_position:  # we pass snp
                shift = snp_position - ref_position
                return read[read_position + shift - 1]
            elif ref_position + ref_bases < snp_position:
                ref_position += ref_bases
                read_position += read_bases
            else:
                return read[read_position + read_bases - 1]
    return None


def add_genotype(cell_genotypes, cell_barcode, umi, genotype):
    """
    Append genotype information for cell and UMI to dictionary
    return modified cell_genotypes dictionary
    """
    try:
        cell_genotypes[cell_barcode]
    except KeyError:
        # haven't seen the cell, must be new UMI
        cell_genotypes[cell_barcode] = {umi: [genotype]}
    else:
        try:
            cell_genotypes[cell_barcode][umi]
        except KeyError:
            cell_genotypes[cell_barcode][umi] = [genotype]
        else:
            cell_genotypes[cell_barcode][umi].append(genotype)
    return cell_genotypes


def collapse_umi(cells):
    """
    Input set of genotypes for each read
    Return list with one entry for each UMI, per cell barcode
    """
    collapsed_data = {}
    for cell_barcode, umi_set in cells.items():
        for _, genotypes in umi_set.items():
            if len(set(genotypes)) > 1:
                pass
            else:
                try:
                    collapsed_data[cell_barcode]
                except KeyError:
                    collapsed_data[cell_barcode] = [genotypes[0]]
                else:
                    collapsed_data[cell_barcode].append(genotypes[0])
    # count total ref, total alt UMIs for each genotype
    for key, value in collapsed_data.items():
        collapsed_data[key] = [value.count("ref"), value.count("alt")]
        assert len(collapsed_data[key]) == 2
    return collapsed_data


def genotype_snps(snp_chunk, bam, known_cells):
    bamfile = pysam.AlignmentFile(bam, "rb")
    cell_genotypes = {}  # key = cell barcode, value = list of UMI-genotype pairs
    for i in snp_chunk:
        chromosome, position, ref, alt = i[0], i[1], i[2], i[3]
        # get all the reads that intersect with the snp from the bam file
        try:
            bamfile.fetch(chromosome, position, position + 1)
        except ValueError:
            pass
        else:
            for read in bamfile.fetch(chromosome, position, position + 1):
                cell_barcode, umi = scan_tags(read.tags)
                if known_cells is None or cell_barcode in known_cells:
                    genotype = get_genotype(
                        read.query_sequence, read.pos, position, read.cigar
                    )
                    if genotype == ref:
                        cell_genotypes = add_genotype(
                            cell_genotypes, cell_barcode, umi, "ref"
                        )
                    elif genotype == alt:
                        cell_genotypes = add_genotype(
                            cell_genotypes, cell_barcode, umi, "alt"
                        )
    collapsed_umi = collapse_umi(cell_genotypes)
    bamfile.close()
    if None in collapsed_umi.keys():
        collapsed_umi.pop(None)
    else:
        pass
    return collapsed_umi


def count_edit_percent_at_postion(edit_chunk, bam, known_cells):
    bamfile = pysam.AlignmentFile(bam, "rb")
    edit_counts = {}  # key = cell barcode and position, value  = UMI counts
    for i in edit_chunk:
        chromosome, position, ref, alt = i[0], i[1], i[2], i[3]
        # get all the reads that intersect with the snp from the bam file
        try:
            bamfile.fetch(chromosome, position, position + 1)
        except ValueError:
            pass
        else:
            for read in bamfile.fetch(chromosome, position, position + 1):
                cell_barcode, umi = scan_tags(read.tags)
                position_cell_index = (
                    str(cell_barcode) + ":" + str(chromosome) + "," + str(position)
                )
                if known_cells is None or cell_barcode in known_cells:
                    transcript_base = get_genotype(
                        read.query_sequence, read.pos, position, read.cigar
                    )
                    if transcript_base == ref:
                        edit_counts = add_genotype(
                            edit_counts, position_cell_index, umi, "ref"
                        )
                    elif transcript_base == alt:
                        edit_counts = add_genotype(
                            edit_counts, position_cell_index, umi, "alt"
                        )
    collapsed_umi = collapse_umi(edit_counts)
    bamfile.close()
    if None in collapsed_umi.keys():
        collapsed_umi.pop(None)
    else:
        pass
    return collapsed_umi


def save_data(data, filename):
    """
    Save table of snp counts
    """
    with open(filename, "w+") as outfile:
        outfile.write("cell_barcode\treference_count\talternate_count\n")
        for key, value in data.items():
            outfile.write(key + "\t" + str(value[0]) + "\t" + str(value[1]) + "\n")


def edited_transcripts(bam, edit_base, cells, nproc):
    """
    Input 10x bam file and SNP coordinates with ref/alt base
    Return each cell barcode with genotype prediction
    """
    edit_set = read_snps(edit_base)
    if cells is not None:
        if cells.endswith(".gz"):
            known_cells = [line.strip("\n") for line in gzip.open(cells, "b")]
        else:
            known_cells = [line.strip("\n") for line in open(cells, "r")]
    else:
        known_cells = None
    p = Pool(int(nproc))
    edit_chunks = chunk(edit_set, nproc)
    data = p.map_async(
        functools.partial(
            count_edit_percent_at_postion, bam=bam, known_cells=known_cells
        ),
        edit_chunks,
    ).get(9999999)
    merged_data = merge_thread_output(data)
    return merged_data


def countedited(bam, edit, cells=None, nproc=1):
    """Count edited RNA bases per transcript per cell in single-cell RNA data

    Search through BAM file and count the number of UMIs for each RNA editing site

    Parameters
    ----------
    bam : str
        Input BAM file. Must be indexed.
    edit : str
        File with edited base coordinates. Needs chromosome, position,
        reference, alternate as first four columns
    cells : str, optional
        File containing cell barcodes to count edited bases for. Can be gzip compressed.
    nproc : int, optional
        Number of processors. Default is 1.

    Returns
    -------
    pandas.DataFrame
        A pandas dataframe containing UMI counts for each edit position in each cell.
    """
    bamfile = pysam.AlignmentFile(bam)
    if bamfile.has_index() is True:
        bamfile.close()
        data = edited_transcripts(bam, edit, cells, nproc)
        return data
    else:
        bamfile.close()
        print("bam file not indexed")
        exit()


def countsnps(bam, snp, cells=None, nproc=1):
    """Count reference and alternate SNPs per cell in single-cell RNA data

    Look through a BAM file with CB and UB tags for cell barcodes and UMIs (as for
    10x Genomics single-cell RNA-seq data) and count the UMIs supporting one of two
    possible alleles at a list of known SNP positions.

    Parameters
    ----------
    bam : str
        Path to BAM file. Must be indexed.
    snp : str
        Path to file containing SNP information. Needs chromosome, position, reference, alternate as first four columns
    cells : str, optional
        Path to file containing cell barcodes to count SNPs for. Can be gzip compressed.
    nproc : int, optional
        Number of processors. Default is 1.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing SNP counts for each cell barcode
    """
    bamfile = pysam.AlignmentFile(bam)
    if bamfile.has_index() is True:
        bamfile.close()
        data = genotype_cells(bam, snp, cells, nproc)
        return data
    else:
        bamfile.close()
        print("bam file not indexed")
        exit()
