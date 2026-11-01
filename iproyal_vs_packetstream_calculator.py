#!/usr/bin/env python3
"""IPRoyal vs PacketStream Scraping Bandwidth TCO Calculator 2026."""
import argparse

def calculate(bandwidth_gb=250):
    # IPRoyal Residential: ~$2.45/GB standard, drops to ~$1.75/GB at 250 GB tier.
    iproyal_rate = 1.75
    iproyal_total = bandwidth_gb * iproyal_rate

    # PacketStream: $1.00/GB flat rate regardless of volume.
    ps_rate = 1.00
    ps_total = bandwidth_gb * ps_rate

    savings = iproyal_total - ps_total

    print("=" * 65)
    print(f"IPRoyal vs PacketStream: {bandwidth_gb} GB Enterprise TCO")
    print("=" * 65)
    print(f"IPRoyal 250 GB Tier:       ${iproyal_total:.2f} (@${iproyal_rate:.2f}/GB)")
    print(f"PacketStream Flat Rate:    ${ps_total:.2f} (@${ps_rate:.2f}/GB)")
    print(f"Direct Capital Savings:    ${savings:.2f} with PacketStream (42.8% lower)")
    print("=" * 65)
    return ps_total, iproyal_total, savings

if __name__ == "__main__":
    calculate()
