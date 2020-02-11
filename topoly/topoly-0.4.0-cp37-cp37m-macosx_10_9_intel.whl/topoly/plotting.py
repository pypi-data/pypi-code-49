# plotting the matrix from the data given
# !/usr/bin/env python
# Copyright Michal Jamroz, 2014, jamroz@chem.uw.edu.pl

from matplotlib import gridspec, cm
import matplotlib as mpl
from .params import TopolyException

mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, LocatableAxes, Size, mpl_axes

plt.rcParams['svg.image_inline'] = True
plt.rcParams['font.size'] = 8


class KnotMap:
    def __init__(self, protlen, protstart=0, patches=1, missing_residues=[], broken_chain=[], rasterized=True,
                 arrows=True, matrix_type="knot"):
        if patches == 0:
            raise TopolyException('No patches')
        self.protlen = protlen
        self.rast = rasterized
        self.protend = protlen
        self.protstart = protstart
        self.fig = plt.figure(figsize=(5, 5))

        h = [Size.Fixed(0.64), Size.Fixed(3.12)]
        v = [Size.Fixed(1.2), Size.Fixed(3.12)]

        divider = Divider(self.fig, (0.0, 0.0, 1., 1.), h, v, aspect=False)
        self.minoraxe = mpl_axes.Axes(self.fig, divider.get_position())
        self.minoraxe.set_axes_locator(divider.new_locator(nx=1, ny=1))

        self.fig.add_axes(self.minoraxe)

        self.axes = []
        self.minoraxe.grid(True, linewidth=0.1)
        self.minoraxe.set_ylim(protstart - 0.5, protlen + 0.5)
        self.minoraxe.set_xlabel('Residue index', fontsize=11)
        # self.minoraxe.set_axis_bgcolor('#f0f0d6')
        # TODO new API in Matplotlib!!!
        self.minoraxe.set_facecolor('#f0f0d6')
        self.minoraxe.set_ylabel('Residue index', fontsize=11)
        self.minoraxe.set_xlim(protstart - 0.5, protlen + 0.5)
        self.arrows = arrows
        self.gids = []
        self.knot_ranges_for_gid = {}
        self.slipknot_ranges_for_gid = []

        tn = int((self.protend - self.protstart) / 5)

        ticks = [i for i in range(self.protstart, self.protend, tn)]
        if ticks[-1] + 30 > self.protend:
            ticks[-1] = self.protend

        mL = mpl.ticker.FixedLocator(
            list(ticks))  # [self.protstart]+[i for i in range(self.protstart,self.protend,50)]+[self.protend])
        self.minoraxe.xaxis.set_major_locator(mL)
        self.minoraxe.yaxis.set_major_locator(mL)

        if len(missing_residues) > 0:  # add spans for missing residues
            colorr = '#336666'
            alf = 0.05
            for r in missing_residues:
                d = r.split("-")
                if len(d) == 2:
                    self.minoraxe.axhspan(float(d[0]), float(d[1]), facecolor=colorr, alpha=alf, edgecolor='none')
                    self.minoraxe.axvspan(float(d[0]), float(d[1]), facecolor=colorr, alpha=alf, edgecolor='none')
                elif len(d) == 1:
                    self.minoraxe.axhline(y=float(d[0]), color=colorr, alpha=alf, linewidth=1)
                    self.minoraxe.axvline(x=float(d[0]), color=colorr, alpha=alf, linewidth=1)
        if len(broken_chain) > 0:  # add spans for missing residues
            colorr = 'red'
            alf = 0.2
            for r in broken_chain:
                self.minoraxe.axhline(y=float(r), color=colorr, alpha=alf, linewidth=0.5, linestyle='-')
                self.minoraxe.axvline(x=float(r), color=colorr, alpha=alf, linewidth=0.5, linestyle='-')
        self.knot_gids = []
        self.minoraxe.invert_yaxis()
        self.minoraxe.plot([protstart, protlen], [protstart, protlen], 'k:', lw=0.1, gid='diagonal')
        self.colors = {'51':'Reds', '61':'Blues', '31':'Greens', '52':'Purples', '41':'Oranges', '00':'binary'}           # Knot colors
        self.patches_counter = 0
        self.legend_gs = gridspec.GridSpec(nrows=patches, ncols=1, left=0.85, right=0.90, bottom=0.19, top=0.9,
                                           wspace=0.2)

        for i in range(patches):
            ax = self.fig.add_subplot(self.legend_gs[i, 0])
            self.axes.append(ax)

    def getGids(self):
        return self.knot_gids

    def _addarrow(self, label, xy, xytext, gid, gidl):
        if self.arrows:
            if label == "knot core":
                ms = 25  # wieksza strzalka
                fc = "#428bca"
            elif label == "slipknot loop":
                ms = 15
                fc = "#fbb450"
            elif label == "slipknot tail":
                ms = 15
                fc = "#62c462"
            else:
                ms = 15
                fc = "gray"
            self.minoraxe.annotate(label, xy=xy, size='medium', xycoords='data', xytext=xytext, \
                                   arrowprops=dict(arrowstyle="fancy", color='none', fc=fc, alpha=0.8,
                                                   mutation_scale=ms, \
                                                   connectionstyle="angle3,angleA=0,angleB=-90", gid=gid), gid=gidl)

    def add_patch_new(self, WRdata):
        x, y, z = WRdata["coordinates"]
        knot_name = WRdata["knot_name"]
        sk_type = WRdata["knot_type"]
        knot_range = WRdata["knot_range"]
        knot_tails = WRdata["knot_tails"]
        sknotloop = WRdata["sknot_loop"]
        sknottails = WRdata["sknot_tails"]

        gid = "knot_" + knot_name
        label_name = "knot " + knot_name[0] + "." + knot_name[1]
        if knot_name in self.colors.keys():
            colormap = cm.get_cmap(self.colors[knot_name], 10)
        else:
            colormap = cm.get_cmap(self.colors['00'], 10)

        gridsize = 100
        if self.protlen > 100:
            gridsize = self.protlen
        t = self.minoraxe.hexbin(x, y, C=z, cmap=colormap, rasterized=self.rast, alpha=1, gridsize=gridsize)
        self.knot_gids.append(gid)
        #       self.minoraxe.add_patch(Rectangle((min(x),min(y)),max(x)-min(x),max(y)-min(y),facecolor='white',alpha=0.001,gid=gid))
        t.set_clim([0, 1])
        cbar = self.fig.colorbar(t, cax=self.axes[self.patches_counter], ticks=[0.0, 0.5, 1.0])  # ,cmap=cm.spring)
        self.patches_counter += 1
        cbar.set_label(label_name)

        # add annotations
        x1 = min(x)
        x2 = max(x)
        y1 = min(y)
        y2 = max(y)
        gid = gid + "_annotate"
        self.gids.append(gid)
        knot_1, knot_N = knot_range

        scale = int(self.protend - self.protstart) / 20

        px = self.protstart + 6 * scale
        py = self.protstart + 2 * scale

        # unique v/h-lines
        htuples = []
        vtuples = []
        labtuple = []
        labtuple2 = []

        if self.arrows:

            for i in range(len(knot_tails)):
                v = knot_tails[i]
                self.minoraxe.plot(v, v, lw=1.0, color='gray', linestyle='-', gid=gid + "_diag_KT_1" + str(i),
                                   marker='o', ms=0)
                mid = v[0] + (v[1] - v[0]) / 2
                self._addarrow("knot tail", (mid, mid - 15), (px + 2 * scale, py + 1 * scale), gid + "_ll2",
                               gid + "_l2")

            for i in range(len(sknotloop)):
                v = sknotloop[i]
                mid = v[0] + (v[1] - v[0]) / 2
                self._addarrow("slipknot loop", (mid, mid - 15), (px + 4 * scale, py + 2 * scale), gid + "_ll3",
                               gid + "_l3")
                # if i==0: # skip if the same are for knot vlines (show onlu for first sliploop
                #    vtuples.append( (v[0],v[0],self.protend,gid) )
                labtuple.append((v[1], gid))
                labtuple.append((v[0], gid))
                self.minoraxe.plot(v, v, lw=1.0, color='#fbb450', linestyle='-', gid=gid + "_diag_SL_1" + str(i),
                                   marker='o', ms=0)
            for i in range(len(sknottails)):
                v = sknottails[i]
                mid = v[0] + (v[1] - v[0]) / 2
                self._addarrow("slipknot tail", (mid, mid - 15), (px + 4 * scale, py + 5 * scale), gid + "_ll4",
                               gid + "_l4")
                labtuple.append((v[1], gid))
                labtuple.append((v[0], gid))
                self.minoraxe.plot(v, v, lw=1.0, color='#62c462', linestyle='-', gid=gid + "_diag_ST_1" + str(i),
                                   marker='o', ms=0)
                # htuples.append( (v[0],0,v[0],gid) )

            # labels, lines, resnumbers for knot area
            v = knot_range
            mid = v[0] + (v[1] - v[0]) / 2
            vtuples.append((v[0], v[0], self.protend, gid))
            htuples.append((v[1], 0, v[1], gid))
            labtuple2.append((v[1], gid))
            labtuple2.append((v[0], gid))
            # add arrow for knot area
            self._addarrow("knot core", (mid, mid - 15), (px + 6 * scale, py), gid + "_ll1", gid + "_l1")

            for h in set(htuples):
                self.minoraxe.hlines(h[0], h[1], h[2], lw=0.1, color='black', linestyles='-', gid=h[3] + "_hkr2")

            for h in set(vtuples):
                self.minoraxe.vlines(h[0], h[1], h[2], lw=0.1, color='black', linestyles='-', gid=h[3] + "_hkr2")

            tmp = []
            for h in set(labtuple2):
                if h[0] not in tmp and h[0] + 1 not in tmp and h[
                    0] - 1 not in tmp:  # skip if labels would be too close
                    self.minoraxe.text(h[0] + 4, h[0], h[0], fontsize='small', gid=h[1] + '_textK1')
                    tmp.append(h[0])
            for h in set(labtuple):
                if h[0] not in tmp and h[0] + 1 not in tmp and h[0] - 1 not in tmp:
                    self.minoraxe.text(h[0] + 4, h[0], h[0], fontsize='small', gid=h[1] + '_textK1')
                    tmp.append(h[0])

            self.minoraxe.plot([knot_1, knot_N], [knot_1, knot_N], lw=2.8, color='#428bca', \
                               linestyle='-', gid=gid + "_diag1", marker='o', ms=5)  # knot core

    def close(self):
        plt.close(self.fig)

    def saveFilePng(self, filename):
        self.fig.savefig(filename, format='png', transparent=True)

    # def saveFile(self, filename):
    #     """
    #         save svg with updated image tag id's
    #     """
    #     data = StringIO()
    #     self.fig.savefig(data, format='svg', transparent=True)
    #     data.seek(0)
    #     img = minidom.parse(data)
    #     it = 0
    #     for i in img.getElementsByTagName('image'):
    #         i.setAttribute('id', 'img_' + self.knot_gids[it])
    #         it += 1
    #     fw = open(filename, "w")
    #     img.writexml(fw)
    #     fw.close()
    #     data.close()
    #     img.unlink()
    #     # plt.close(self.fig)


class Reader:
    def __init__(self, input_data, cutoff=0.48, minknotted=21):

        # print cutoff, filename
        self.header = []
        self.data = {}
        self.hdr = {}
        self.cutoff = cutoff
        self.cutoff_column = 0
        self.hdr_r = {}
        self.seq_start = -1
        self.seq_end = -1
        self.unknot = False
        self.pierwsza_linijka = []
        self.unique_knots = set()
        self.overall_type = "S"

        if type(input_data) is str:
            fff = input_data.split('\n')
            if len(fff) <= minknotted:
                self.unknot = True

            for line_index in range(len(fff)):
                line = fff[line_index]
                if len(line) < 2 or self.unknot:
                    continue
                if "HEAD" in line:
                    self.header.append(line)
                elif line[0] == '#':
                    self.seq_start, self.seq_end = int(line.split()[1]), int(line.split()[2])
                    print(self.seq_start, self.seq_end)
                    d = line.strip().split()[3:-3]  # data - without first three and last three columns
                    for i in range(3,len(d)-2):
                        if float(d[i].replace(">", ""))/100 < self.cutoff:
                            self.cutoff_column = i
                            break
                else:
                    if "UNKNOT" in line:
                        self.unknot = True
                        continue
                    d = line.strip().split()
                    unique_knots = set(' '.join(d[2:self.cutoff_column + 1]).replace(',',' ').replace('0','').split())
                    for i in range(2,self.cutoff_column + 1):
                        for knot in d[i].split(','):
                            if knot == '0':
                                continue
                            if knot not in self.data:
                                self.data[knot] = []
                            probability = 0.9 - (i-2)*0.03
                            self.data[knot].append((int(d[0]), int(d[1]), probability))
                            if (int(d[0]), int(d[1])) == (self.seq_start, self.seq_end):
                                self.pierwsza_linijka.append(knot)
                                self.overall_type = 'K'
                    self.unique_knots |= unique_knots

            print(self.unique_knots, self.seq_end, self.seq_start)
            print(self.data)
            print(self.overall_type, self.unknot)

        # producing self.data, self.unique_knots, self.overall_type, self.pierwsza_linijka, self.seq_start, self.seq_end, self.unknot

        elif type(input_data) is dict:
            indices = []
            for key in input_data.keys():
                indices += [key[0], key[1]]
                knots = input_data[key].keys()
                for knot in knots:
                    if knot == '0_1' or input_data[key][knot] < self.cutoff:
                        continue
                    if knot not in self.data.keys():
                        self.data[knot] = []
                    self.data[knot].append((key[0], key[1], input_data[key][knot]))
            self.unique_knots = list(self.data.keys())
            self.seq_start = min(indices)
            self.seq_end = max(indices)
            if not self.unique_knots:
                self.unknot = True

        self.clean_data()

    def clean_data(self):
        to_remove = []
        for k in self.unique_knots:
            if not self._checkIfManyPoints(self.data[k]):  # pierwszy warunek, zeby wyswietlaly sie tez wezly przez mostki i jony
                to_remove.append(k)
        # delete empty
        for k in self.data.keys():
            if len(self.data[k]) < 2:
                to_remove.append(k)
        for k in list(set(to_remove)):
            self.data.pop(k, None)
        self.unique_knots = list(self.data.keys())
        return

    def isValidKnot(self, kn):
        try:
            if kn != "0" and kn != "01" and (
                    (kn.find('m') > 0 and float(kn.replace("m", "")) > 0) or float(kn) > 0):
                return True
            else:
                return False
        except ValueError as e:
            # print "Found a strange knot: " + str(e.message)
            return True

    def empty(self):
        if not self.unknot and len(self.data) != 0:
            return False
        return True

    def isKnot(self, knottype):
        if knottype in self.pierwsza_linijka:
            return True
        else:
            return False

    def getOverallType(self):
        return self.overall_type

    def getCutoffsList(self):
        t = self.hdr
        del t['IN']
        return t

    def chainStart(self):
        return self.seq_start

    def chainEnd(self):
        return self.seq_end

    def getUniqueKnots(self):
        return self.unique_knots

    def _checkIfManyPoints(self, knot_array):
        setx = []
        sety = []
        for e in knot_array:
            setx.append(e[0])
            sety.append(e[1])
        if len(set(setx)) < 2 or len(set(sety)) < 2:
            # print(len(set(setx)), len(set(sety)))
            return False
        else:
            return True

    def _getForCutoff(self):
        out = {}
        to_index = self.cutoff_column + 1
        for knot in self.unique_knots:
            out[knot] = []

        for l in self.data:
            res_i = int(l[0])  # first two columns (was -2
            res_j = int(l[1])  # first two columns (was -1 -- last columns
            # res_i = int(l[-2]) # first two columns (was -2
            # res_j = int(l[-1]) # first two columns (was -1 -- last columns
            for i in range(len(l[2:to_index])):
                # e = l[2:-3][i] # now scan for whole data array (we checked existing knots >cutoff, but plot is created with all data)
                e = l[2:to_index][i]  # now scan for 100-cutoff block
                for f in e.split(","):
                    try:
                        if not self.isValidKnot(f) or f not in self.unique_knots:
                            continue
                    except ValueError as e:
                        print(e.message)
                        if f not in self.unique_knots:
                            continue
                    # percentage = self.hdr_r[2+i]
                    percentage = 1.0 - float(i) / (to_index + 10)  # TODO .oszukalem skale dla ciemnieszych kolorow..
                    # ma byc to_index-2
                    g = (res_i, res_j, percentage)
                    out[f].append(g)
        # check how many points:



    def getKnot(self, knot_type):
        """
             Get knots within range 100-cutoff (skip less than cutoff) - it is in _getForCutoff() method

        """
        if knot_type not in self.data.keys():
            return None
        x = []
        y = []
        z = []

        for xx, yy, zz in self.data[knot_type]:
            x.append(xx)
            y.append(yy)
            z.append(zz)
        maxx = max(x)
        maxy = max(y)
        minx = min(x)
        miny = min(y)
        protstart = self.seq_start
        protend = self.seq_end
        sknot = "S"
        knot_range = (maxx + 1, miny - 1)

        slipknotloop = []
        slipknottails = []
        knottails = []
        if protstart == minx and protend == maxy:
            knottails.append((protstart, maxx))
            knottails.append((miny, protend))
        if protstart < minx:
            if maxx >= minx:
                slipknotloop.append((minx, maxx))
            slipknottails.append((protstart, minx - 1))
            if protend == maxy:
                knottails.append((miny, protend))
        if protend > maxy:
            if maxy >= miny:
                slipknotloop.append((miny, maxy))

            slipknottails.append((maxy + 1, protend))
            if protstart == minx:
                knottails.append((protstart, maxx))

        knot_length = miny - 1 - (maxx + 1) + 1
        if self.isKnot(knot_type):
            sknot = "K"
            C_cut = self.seq_end - miny + 1
            N_cut = maxx
        else:
            sknot = "S"
            if maxy == protend:
                C_cut = self.seq_end - miny
            else:
                C_cut = self.seq_end - maxy
            if minx == protstart:
                N_cut = maxx
            else:
                N_cut = minx - 1

        out = {"coordinates": (x, y, z), "knot_name": knot_type.replace('_',''), \
               "knot_type": sknot, "knot_range": knot_range, \
               "knot_tails": knottails, "sknot_loop": slipknotloop, \
               "sknot_tails": slipknottails, \
               "knot_length": knot_length, \
               "C_cut": C_cut, \
               "N_cut": N_cut}
        return out


def colorFromGLN(gln):
    if (gln<-1): return (int(255*1/(gln*gln)), 0, 0) 
    elif (gln<=0): return (255, int(255*(1+gln)), int(255*(1+gln)))
    elif (gln<=1): return (int(255*(1-gln)), int(255*(1-gln)), 255)
    else: return (0, 0, int(255*1/(gln*gln)))



