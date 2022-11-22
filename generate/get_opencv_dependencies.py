
import sys
import os
sys.path.append(r'C:\Users\PJ\Documents\GitHub\bazelrio_bzlmod\bazelrio_bzlmod_gentool')

from bazelrio_gentool.deps.dependency_container import DependencyContainer


def _default_native_shared_platforms():
    return ["windowsx86-64", "linuxx86-64", "osxx86-64"]

def _default_native_static_platforms():
    return ["windowsx86-64static", "linuxx86-64static", "osxx86-64static"]


def _default_all_platforms():
    return (
        ["linuxathena", "linuxathenastatic"]
        + _default_native_shared_platforms()
        + _default_native_static_platforms()
    )

def get_opencv_dependencies():
    year = "2023"
    version = "4.6.0-2"
    
    year = "2021"
    version = "3.4.7-4"

    group_id = f"edu.wpi.first.thirdparty.frc{year}.opencv"

    group = DependencyContainer("wpi-opencv", version, year, "https://frcmaven.wpi.edu/release")
    group.create_cc_dependency(f"opencv-cpp", parent_folder="opencv", group_id=group_id, headers="headers", resources=_default_all_platforms(), has_jni=True)
    
    group.create_java_dependency(f"opencv-java", parent_folder="opencv", group_id=group_id, dependencies=["opencv-cpp"])

    return group
    
if __name__ == "__main__":
    get_opencv_dependencies()