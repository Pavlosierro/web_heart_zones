import gpxpy

def parse_gpx(file):
    gpx = gpxpy.parse(file)
    points = [pt for track in gpx.tracks for seg in track.segments for pt in seg.points]

    elevations = [p.elevation for p in points]
    lats = [p.latitude for p in points]
    lons = [p.longitude for p in points]

    return {
        "points": points,
        "elevations": elevations,
        "lats": lats,
        "lons": lons
    }
