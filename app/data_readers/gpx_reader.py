import gpxpy.gpx


def read_hr_from_gpx(gpx_file) -> list[int]:
    results = []

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                for extension in point.extensions:
                    hr = extension.find('{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr')
                    try:
                        hr = int(hr.text)
                    except:
                        hr = None
                        print(f"No HR found at point {point.time}")
                    else:
                        results.append(hr)
    return results
