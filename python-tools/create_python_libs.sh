#!/bin/bash


mkdir -p ctr

for ksy in ../formats_specifications/*.ksy
do
  ksc $ksy \
	  --target python \
	  --import-path ../formats_specifications/ \
	  --outdir ctr \
	  --python-package ctr
done
