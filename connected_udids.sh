#!/bin/bash
for line in $(system_profiler SPUSBDataType | sed -n -e '/iPad/,/Serial/p' -e '/iPhone/,/Serial/p' -e '/iPod/,/Serial/p' | grep "Serial Number:" | awk -F ": " '{print $2}'); do
  UDID=${line}
  echo ${UDID}
done
