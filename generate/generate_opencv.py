
import sys
sys.path.append(r'C:\Users\PJ\Documents\GitHub\bazelRio\bazelrio_bzlmod_gentool')

from dependency_container import DependencyContainer
from generate_group import generate_group
from generate_json import generate_json
from platforms import default_all_platforms, default_native_shared_platforms
from cc_dependency import CcDependency


def get_opencv_dependencies():

    opencv_group = DependencyContainer("4.6.0-2", "")
    opencv_group.cc_deps.append(CcDependency(
        name="opencv-cpp", 
        maven_url = "",
        group_id = "",
        version="4.6.0-2", 
        parent_folder="opencv", 
        dependencies=[], 
        resources=[], 
        headers=None, 
        has_jni=False))
    opencv_group.dep_lookup["opencv-cpp"] = opencv_group.cc_deps[-1]

    group = DependencyContainer("2023.1.1-beta-3", "https://frcmaven.wpi.edu/release")
    group.dep_lookup.update(opencv_group.dep_lookup)


    # _cc_dependency(group, "wpiutil", has_jni=True)
    # _cc_dependency(group, "wpinet", has_jni=True, dependencies=["wpiutil-cpp"])
    # _cc_dependency(group, "wpimath", has_jni=True, dependencies=["wpiutil-cpp"])
    # _cc_dependency(group, "hal", has_jni=True, dependencies=["wpiutil-cpp"])
    # _cc_dependency(group, "ntcore", has_jni=True, dependencies=["wpiutil-cpp", "wpinet-cpp"])
    # _cc_dependency(group, "cscore", has_jni=True, dependencies=["wpiutil-cpp", "wpinet-cpp", "opencv-cpp"])
    # _cc_dependency(group, "cameraserver", has_jni=False, dependencies=["wpiutil-cpp", "cscore-cpp", "ntcore-cpp", "wpinet-cpp", "opencv-cpp"])
    # _cc_dependency(group, "wpilibc", has_jni=False, dependencies=["wpiutil-cpp", "wpimath-cpp", "wpinet-cpp", "cscore-cpp", "ntcore-cpp", "hal-cpp", "cameraserver-cpp", "opencv-cpp"])
    # _cc_dependency(group, "wpilibNewCommands", has_jni=False, dependencies=["wpiutil-cpp", "wpimath-cpp", "wpinet-cpp", "cscore-cpp", "ntcore-cpp", "hal-cpp", "cameraserver-cpp", "opencv-cpp", "wpilibc-cpp"])
    
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
    output_dir = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazelrio_bzlmod\dependencies'
    registry_location = r'C:\Users\PJ\Documents\GitHub\bazelRio\bazel-central-registry'

    group = get_allwpilib_dependencies()
    generate_group(output_dir, group)
    generate_json(registry_location, group)
    
if __name__ == "__main__":
    main()
