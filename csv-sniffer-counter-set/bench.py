import csv, pathlib, pyperf
def sniff(s): csv.Sniffer()._guess_delimiter(s, None)
r = pyperf.Runner()
sizes = [1024, 2048, 4096]
for file in pathlib.Path("/home/maurycy/CSVsniffer/CSV/").glob("*.csv"):
    for s in sizes:
        with file.open() as f:
            try:
                r.bench_func(f"csv_sniff({file.name}, {s})", sniff, f.read(s))
            except UnicodeDecodeError:
                pass
