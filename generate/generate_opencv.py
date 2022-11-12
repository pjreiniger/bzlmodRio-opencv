
import sys
sys.path.append(r'C:\Users\PJ\Documents\GitHub\bazelRio\bazelrio_bzlmod_gentool')

from dependency_container import DependencyContainer
from generate_group import generate_group
from generate_json import generate_json
from platforms import default_all_platforms, default_native_shared_platforms
from cc_dependency import CcDependency
from platforms import default_all_platforms, default_native_shared_platforms


def get_opencv_dependencies():
    group = DependencyContainer("4.6.0-2", "https://frcmaven.wpi.edu/release")
    group.create_cc_dependency(f"opencv-cpp", parent_folder="opencv", group_id=f"edu.wpi.first.thirdparty.frc2023.opencv", headers="headers", resources=default_all_platforms(), has_jni=True)
    
    group.create_java_dependency(f"opencv-java", parent_folder="opencv", group_id=f"edu.wpi.first.thirdparty.frc2023.opencv", dependencies=["opencv-cpp"])

    return group

def main():
    output_dir = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazelrio_bzlmod-opencv\dependencies'
    registry_location = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazel-central-registry'

    group = get_opencv_dependencies()
    group.repository_url = "https://github.com/pjreiniger/bzlmodRio-opencv/archive/refs/heads/starting.zip"
    group.strip_prefix = "bzlmodRio-opencv-starting/dependencies/opencv"
    generate_group(output_dir, group)
    generate_json(registry_location, group)
    
if __name__ == "__main__":
    main()
