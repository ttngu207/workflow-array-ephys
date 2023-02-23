import datajoint as dj

from workflow_array_ephys import db_prefix

schema = dj.schema(db_prefix + "reference")


# Declare table SkullReference for use in element-array-ephys

@schema
class SkullReference(dj.Lookup):
    definition = """
    skull_reference   : varchar(60)
    """
    contents = zip(['Bregma', 'Lambda'])
    