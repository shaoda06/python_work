# To get python version
# 1
import platform
print(platform.python_version())
# 3.7.3

# 2
import sys
print(sys.version)
# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
# [Clang 6.0 (clang-600.0.57)]

print(sys.version_info)
# sys.version_info(major=3, minor=7, micro=3, releaselevel='final', serial=0)

print(sys.version_info.major)
# 3