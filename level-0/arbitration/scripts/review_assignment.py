#!/usr/bin/env python3
"""Two-step assignment review over UTF-8 JSON on stdin and stdout.

show:   {"source": "...", "amendments": [], "recipient": "...", "assignment": "..."}
decide: {"packet": <show.packet>, "digest": <show.digest>,
         "comparison": "...", "reason": "...", "decision": "send"|"revise"}

A digest binds the fields; it does not prove a person reviewed them or prevent forgery.
"""
import argparse
import hashlib
import json
import sys


FIELDS = {'source', 'amendments', 'recipient', 'assignment'}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def packet_valid(packet):
    if not isinstance(packet, dict) or set(packet) != FIELDS:
        raise ValueError('packet must contain exactly source, amendments, recipient, assignment')
    if not all(nonempty(packet[key]) for key in ('source', 'recipient', 'assignment')):
        raise ValueError('source, recipient and assignment must be nonempty strings')
    if not isinstance(packet['amendments'], list) or not all(nonempty(x) for x in packet['amendments']):
        raise ValueError('amendments must be an ordered array of nonempty strings (or [])')
    return packet


def digest(packet):
    serialized = json.dumps(packet, ensure_ascii=True, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(serialized.encode('ascii')).hexdigest()


def run(mode, data):
    if mode == 'show':
        packet = packet_valid(data)
        return {'packet': packet, 'digest': digest(packet),
                'instruction': 'Compare source and each amendment with the recipient and exact assignment; then decide.'}
    if not isinstance(data, dict) or set(data) != {'packet', 'digest', 'comparison', 'reason', 'decision'}:
        raise ValueError('decide requires exactly packet, digest, comparison, reason, decision')
    packet = packet_valid(data['packet'])
    if not isinstance(data['digest'], str) or digest(packet) != data['digest']:
        raise ValueError('packet changed or digest does not match; review again')
    if not nonempty(data['comparison']) or not nonempty(data['reason']):
        raise ValueError('comparison and reason must be nonempty strings')
    if data['decision'] not in ('send', 'revise'):
        raise ValueError('decision must be send or revise')
    return {'packet': packet, 'digest': data['digest'], 'comparison': data['comparison'],
            'reason': data['reason'], 'decision': data['decision'],
            'ready': data['decision'] == 'send',
            'notice': 'Review is advisory: this tool does not verify semantics or send an assignment.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mode', choices=('show', 'decide'))
    args = parser.parse_args()
    try:
        data = json.loads(sys.stdin.buffer.read().decode('utf-8'))
        result = run(args.mode, data)
        out = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
        sys.stdout.buffer.write(out.encode('utf-8'))
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
