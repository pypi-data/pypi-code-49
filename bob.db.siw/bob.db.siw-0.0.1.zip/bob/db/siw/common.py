import os


def siw_file_metadata(path):
    """Returns the metadata associated with a SIW file

    All the video files are named as SubjectID_SensorID_TypeID_MediumID_SessionID.mov
    (or *.mp4). SubjectID ranges from 001 to 165. SensorID represents the capture
    device. TypeID represents the spoof type of the video. MediumID and SessionID record
    additional details of the video, shown in the Figure 2
    (http://cvlab.cse.msu.edu/siw-spoof-in-the-wild-database.html)

    Parameters
    ----------
    path : str
        The path of the SIW file.

    Returns
    -------
    client_id : str
    attack_type : str
    sensor_id : str
    type_id : str
    medium_id : str
    session_id : str
    """
    # For example:
    # path: Train/live/003/003-1-1-1-1.mov
    # path: Train/spoof/003/003-1-2-1-1.mov
    fldr, path = os.path.split(path)
    # live_spoof = os.path.split(os.path.split(fldr)[0])[1]
    path, extension = os.path.splitext(path)
    client_id, sensor_id, type_id, medium_id, session_id = path.split("_")[0].split("-")
    attack_type = {"1": None, "2": "print", "3": "replay"}[type_id]
    if attack_type is not None:
        attack_type = f"{attack_type}/{medium_id}"
    return client_id, attack_type, sensor_id, type_id, medium_id, session_id
