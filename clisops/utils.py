import xarray as xr


def get_coord_by_attr(dset, attr, value):
    coords = dset.coords

    for coord in coords.values():
        if coord.attrs.get(attr, None) == value:
            return coord

    return None 


def get_latitude(dset):
    return get_coord_by_attr(dset, 'standard_name', 'latitude')


def get_longitude(dset):
    return get_coord_by_attr(dset, 'standard_name', 'longitude')


def _get_xy(dset, space):
    """
    NOTE: 
    The order of the values in a bounding box does not seem to be consistent.

    http://wiki.openstreetmap.org/wiki/Bounding_Box 

    ...says the order is "left,bottom,right,top", or:

    "min Longitude, min Latitude, max Longitude, max Latitude".

    """
    if not space:
        return {}

    lat = get_latitude(dset)
    lon = get_longitude(dset)

    xy = {}

    if hasattr(lat, 'name'):
        xy[lat.name] = slice(space[1], space[3])
    if hasattr(lon, 'name'):
        xy[lon.name] = slice(space[0], space[2])

    return xy 


def map_args(dset, **kwargs):
    args = {}

    for key, value in kwargs.items():
        
        if value == None:
            pass
        elif key == 'space':
            args.update(_get_xy(dset, value))
        elif key == 'level':
            pass
        else:
            args[key] = slice(value[0], value[1])

    return args 

