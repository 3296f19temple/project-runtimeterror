#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("post.txt", sep="|", header=None, names=["CRN", "Course", "Campus", "Credits", "Class_name", "time", "Seats", "Professor", "Term"])

    print(df[:20])
