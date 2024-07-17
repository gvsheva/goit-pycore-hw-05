import argparse
import signal
from itertools import tee

from task3 import Level, filter_records, parse_log, stat_records, tail

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=argparse.FileType(),
                    default="-", help="Path to the file")
    ap.add_argument("--limit", type=int, default=100,
                    help="Limit the number of lines")
    ap.add_argument("--details", type=Level,
                    default=None, help="Filter the log level")
    ap.add_argument("--interval", type=int, default=1,
                    help="Interval between stats dumps")

    args = ap.parse_args()

    def sigint_handler(sig, frame):
        print()
        raise StopIteration()

    signal.signal(signal.SIGINT, sigint_handler)

    stream = parse_log(args.path)
    stats_stream, details_stram = tee(tail(args.limit, stream))

    stats = stat_records(stats_stream)
    print(f"+{'Stats':-^21}+")
    print(f"|{'Level':^10}|{'Count':^10}|")
    print(f"|{'-'*10}+{'-'*10}|")
    for l, c in sorted(stats.items()):
        print(f"|{l.name:^10}|{c:^10}|")
    print("+" + "-"*21 + "+")

    if args.details is not None:
        print()
        print(f"Details for {args.details.name}:")
        for record in filter_records(args.details, details_stram):
            print(
                f"{record.datetime.isoformat()} [{record.level.name}]: {record.message}")
