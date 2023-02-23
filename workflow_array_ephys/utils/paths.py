import datajoint as dj
import pathlib


def get_ephys_root_data_dir():
    data_dir = dj.config.get("custom", {}).get("ephys_root_data_dir", None)
    return pathlib.Path(data_dir) if data_dir else None


def get_processed_root_data_dir():
    data_dir = dj.config.get("custom", {}).get("ephys_processed_data_dir", None)
    return pathlib.Path(data_dir) if data_dir else None


def get_session_directory(session_key: dict) -> str:
    from ..pipeline import session

    data_dir = get_ephys_root_data_dir()
    if not (session.SessionDirectory & session_key):
        raise FileNotFoundError(f"No session data directory defined for {session_key}")

    sess_dir = data_dir / (session.SessionDirectory & session_key).fetch1("session_dir")

    return sess_dir.as_posix()