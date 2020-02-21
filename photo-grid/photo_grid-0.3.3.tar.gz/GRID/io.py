# Basic imports
import io
import os
import numpy as np
import pandas as pd
from urllib.request import urlopen
from PIL import Image

# 3-rd party imports
from PyQt5.QtCore import QFile, QIODevice
import h5py
import rasterio

# self import
from .lib import initProgress, updateProgress, pltImShow, pltSegPlot
from .dir import Dir


def loadImg(path):
    """
    ----------
    Parameters
    ----------
    path : str
           path to the image file

    -------
    Returns
    -------
    npImg : 3-d ndarray encoded in UINT8

    """

    # rasObj = rasterio.open(path)
    # nCh = rasObj.count
    # obj = initProgress(nCh, "loading channel 1")
    # if nCh < 3:
    #     npImg = np.zeros((rasObj.height, rasObj.width, 3), dtype="uint8")
    #     for i in range(3):
    #         npImg[:, :, i] = rasObj.read(1)
    #         updateProgress(obj, 1, "loading channel %d" %
    #                        (i+2 if i != (nCh-1) else i+1))
    # else:
    #     npImg = np.zeros((rasObj.height, rasObj.width, nCh), dtype="uint8")
    #     for i in range(nCh):
    #         npImg[:, :, i] = rasObj.read(i + 1)
    #         updateProgress(obj, "loading channel %d" % (i+2) if i != (nCh-1)
    # e
    # lse "Done")

    # return npImg
    rasObj = rasterio.open(path)
    nCh = rasObj.count
    prog = initProgress(nCh, name="Loading channel 1")
    if nCh < 3:
        npImg = np.zeros((rasObj.height, rasObj.width, 3), dtype="uint8")
        for i in range(3):
            npImg[:, :, i] = rasObj.read(1)
            if i != nCh-1:
                updateProgress(prog, name="Loading channel %d" % (i+2))
            else:
                updateProgress(prog, name="Done")
    else:
        npImg = np.zeros((rasObj.height, rasObj.width, nCh), dtype="uint8")
        for i in range(nCh):
            npImg[:, :, i] = rasObj.read(i + 1)
            if i != nCh-1:
                updateProgress(prog, name="Loading channel %d" % (i+2))
            else:
                updateProgress(prog, name="Done")

    return npImg


def loadImgWeb(URL):
    """
    ----------
    Parameters
    ----------
    URL : str
          URL to the UINT8-encoded image file

    -------
    Returns
    -------
    npImg : 3-d ndarray encoded in UINT8

    """

    with urlopen(URL)as url:
        file = io.BytesIO(url.read())
        npImg = np.array(Image.open(file), dtype="uint8")

    return npImg


def loadMap(path):
    """
    ----------
    Parameters
    ----------
    path : str
           path to the csv file

    -------
    Returns
    -------
    pdMap : Pandas dataframe or None if path is empty

    """

    try:
        pdMap = pd.read_csv(path, header=None)
    except Exception:
        pdMap = None

    return pdMap


def saveQImg(qimg, path):
    """
    ----------
    Parameters
    ----------
    qimg : qimage

    path : str
           path to the destination
    -------
    Returns
    -------
    None

    """

    qfile = QFile(path + ".jpg")
    qfile.open(QIODevice.WriteOnly)
    qimg.save(qfile, "JPG")
    qfile.close()


def saveDT(grid, path, prefix="GRID"):
    # get path
    pathDT = os.path.join(path, prefix+"_data.csv")

    # progress bar
    nD = grid.imgs.depth
    lsK = grid.imgs.paramKMs["lsSelect"]

    # grab info from GRID obj
    img = grid.imgs.get("crop").copy().astype(np.int)
    ch1Sub = 1 if img.shape[2] == 3 else 3  # replace NIR with Gr if it's RGB

    # intialize dataframe
    df = pd.DataFrame(columns=['var', 'row', 'col',
                               'area_all', 'area_veg'])

    # calculate index imgs
    dicIdx = dict({
        "NDVI": (img[:, :, ch1Sub] - img[:, :, 0]) /
                (img[:, :, ch1Sub] + img[:, :, 0] + 1e-8),
        "GNDVI": (img[:, :, ch1Sub] - img[:, :, 1]) /
                (img[:, :, ch1Sub] + img[:, :, 1] + 1e-8),
        "CNDVI": (2 * img[:, :, ch1Sub] - img[:, :, 0] - img[:, :, 1]) /
                (img[:, :, ch1Sub] + img[:, :, 0] + img[:, :, 1] + 1e-8),
        "RVI": img[:, :, ch1Sub] / (img[:, :, 0] + 1e-8),
        "GRVI": img[:, :, ch1Sub] / (img[:, :, 1] + 1e-8),
        "NDGI": (img[:, :, 1] - img[:, :, 0]) /
                (img[:, :, 1] + img[:, :, 0] + 1e-8)
    })

    # channel values
    for i in range(nD):
        name = "ch_%d" % i
        dicIdx[name] = img[:, :, i]

    # ratio of each cluster (k)
    cluster = 0
    for k in lsK:
        name = "cluster_%d" % cluster
        dicIdx[name] = (np.isin(grid.imgs.get("kmean"), i))*1
        cluster += 1
        
    # append columns based on the dict
    for key, _ in dicIdx.items():
        df[key] = None
        df[key + "_std"] = None

    # index data frame
    for row in range(grid.agents.nRow):
        for col in range(grid.agents.nCol):
            agent = grid.agents.get(row, col)
            if not agent or agent.isFake():
                continue
            entry = dict(var=agent.name, row=row, col=col)

            # get ROI region
            rg_row = range(agent.getBorder(Dir.NORTH),
                           agent.getBorder(Dir.SOUTH))
            rg_col = range(agent.getBorder(Dir.WEST),
                           agent.getBorder(Dir.EAST))

            # get selected pixels info
            imgBinAgent = grid.imgs.get('bin')[rg_row, :][:, rg_col]
            n_veg = imgBinAgent.sum()

            # load area info
            entry["area_all"] = len(rg_row)*len(rg_col)
            entry["area_veg"] = n_veg

            # append temp entry
            for key, imgIdx in dicIdx.items():
                imgIdxAgent = imgIdx[rg_row, :][:, rg_col]
                img_out = np.multiply(imgBinAgent, imgIdxAgent)
                vec_out = img_out[img_out != 0].flatten()
                entry[key] = vec_out.mean()
                entry[key + "_std"] = vec_out.std()

            df.loc[len(df)] = entry

    df = df[~df['var'].isnull()]

    # export
    df.to_csv(pathDT, index=False)


def savePlot(grid, path, prefix="GRID"):
    pltImShow(grid.imgs.get("crop")[:, :, :3],
              path=path, prefix=prefix, filename="_raw.png")

    pltSegPlot(grid.agents, grid.imgs.get("crop")[:, :, :3],
               isRect=True,
               path=path, prefix=prefix, filename="_rgb.png")

    pltImShow(grid.imgs.get("kmean"),
              path=path, prefix=prefix, filename="_kmeans.png")

    pltSegPlot(grid.agents, grid.imgs.get("visSeg"),
               isRect=True,
               path=path, prefix=prefix, filename="_seg.png")

    pltSegPlot(grid.agents, grid.imgs.get("bin"),
               isRect=True,
               path=path, prefix=prefix, filename="_bin.png")


def saveH5(grid, path, prefix="GRID"):
    # get path
    pathH5 = os.path.join(path, prefix+".h5")

    # create file
    with h5py.File(pathH5, "w"):
        None  # create file

    # index data frame
    img = grid.imgs.get("crop").copy()
    for row in range(grid.agents.nRow):
        for col in range(grid.agents.nCol):
            agent = grid.agents.get(row, col)
            if not agent or agent.isFake():
                continue
            key = agent.name

            # get ROI region
            rgY = range(agent.getBorder(Dir.NORTH),
                        agent.getBorder(Dir.SOUTH))
            rgX = range(agent.getBorder(Dir.WEST),
                        agent.getBorder(Dir.EAST))

            # compute kernel
            imgAll = img[:, rgX, :][rgY, :, :]
            imgBin = grid.imgs.get("bin")[:, rgX][rgY, :]
            imgFin = np.multiply(imgAll, np.expand_dims(imgBin, 2))

            # export image
            try:
                with h5py.File(pathH5, "a") as f:
                    f.create_dataset(key, data=imgFin, compression="gzip")
            except Exception:
                print("Failed to save %s" % key)

