
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
    group.create_cc_dependency(f"opencv-cpp", parent_folder="opencv", group_id=f"edu.wpi.first", headers="headers", resources=default_all_platforms(), has_jni=True)
    
    group.create_java_dependency(f"opencv-java", parent_folder="opencv", group_id=f"edu.wpi.first.thirdparty.frc2023.opencv", dependencies=["opencv-cpp"])

    # _java_dependency(group, "wpiutil", dependencies=["wpiutil-cpp"], maven_deps=[
    #     ("com.fasterxml.jackson.core:jackson-annotations", "2.12.4"),
    #     ("com.fasterxml.jackson.core:jackson-core", "2.12.4"),
    #     ("com.fasterxml.jackson.core:jackson-databind", "2.12.4")])
    # _java_dependency(group, "wpinet", dependencies=["wpiutil-java", "wpiutil-cpp", "wpinet-cpp"])
    # _java_dependency(group, "wpimath", dependencies=["wpiutil-java", "wpiutil-cpp", "wpimath-cpp"], maven_deps=[("org.ejml:ejml-simple", "0.41")])
    # _java_dependency(group, "hal", dependencies=["wpiutil-java", "wpiutil-cpp", "hal-cpp"])
    # _java_dependency(group, "ntcore", dependencies=["wpiutil-java", "wpiutil-cpp", "wpinet-java", "wpinet-cpp", "ntcore-cpp"])
    # _java_dependency(group, "cscore", dependencies=["wpiutil-java", "wpiutil-cpp", "wpinet-java", "wpinet-cpp", "cscore-cpp", "opencv-cpp"])
    # _java_dependency(group, "cameraserver", dependencies=["wpiutil-java", "wpiutil-cpp", "cscore-cpp", "cscore-java", "ntcore-java", "ntcore-cpp", "wpinet-java", "wpinet-cpp", "opencv-cpp"])
    # _java_dependency(group, "wpilibj", dependencies=["wpiutil-cpp", "wpiutil-java", "wpimath-cpp", "wpimath-java", "wpinet-cpp", "wpinet-java", "cscore-cpp", "cscore-java", "ntcore-cpp", "ntcore-java", "hal-cpp", "hal-java", "cameraserver-cpp", "cameraserver-java", "opencv-cpp"])
    # _java_dependency(group, "wpilibNewCommands", dependencies=["wpiutil-cpp", "wpiutil-java", "wpimath-cpp", "wpimath-java", "wpinet-cpp", "wpinet-java", "cscore-cpp", "cscore-java", "ntcore-cpp", "ntcore-java", "hal-cpp", "hal-java", "cameraserver-cpp", "cameraserver-java", "opencv-cpp", "wpilibj-java"])

    # _halsim_dependency(group, "halsim_ds_socket", dependencies=["hal-cpp", "wpiutil-cpp", "wpinet-cpp"])
    # _halsim_dependency(group, "halsim_gui", dependencies=["hal-cpp", "wpiutil-cpp", "wpinet-cpp", "ntcore-cpp"])
    # _halsim_dependency(group, "halsim_ws_client", dependencies=["hal-cpp", "wpiutil-cpp", "wpinet-cpp"])
    # _halsim_dependency(group, "halsim_ws_server", dependencies=["hal-cpp", "wpiutil-cpp", "wpinet-cpp"])

    return group

def main():
    output_dir = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazelrio_bzlmod-opencv\dependencies'
    registry_location = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazel-central-registry'

    group = get_opencv_dependencies()
    generate_group(output_dir, group)
    # generate_json(registry_location, group)
    
if __name__ == "__main__":
    main()
