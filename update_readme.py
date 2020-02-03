import fileinput
import re
import sys

fn = "index.md"
regex = r"https:\/\/github\.com\/OneDayMac\/OneDayMac\.github\.io\S+\.tar\.gz"
new_content = sys.argv[-1]

f = open(fn, 'r')
old_content = f.read()
f.close()
output = re.sub(regex, new_content, old_content)

f = open(fn, 'w')
f.write(output)
f.close()
