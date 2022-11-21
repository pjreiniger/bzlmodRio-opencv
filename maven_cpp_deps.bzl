load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")

filegroup_all = """filegroup(
     name = "all",
     srcs = glob(["**"]),
     visibility = ["//visibility:public"],
 )
 """

cc_library_headers = """cc_library(
    name = "headers",
    hdrs = glob(["**"]),
    includes = ["."],
    visibility = ["//visibility:public"],
)
"""

cc_library_sources = """filegroup(
     name = "sources",
     srcs = glob(["**"]),
     visibility = ["//visibility:public"],
 )
 """

cc_library_static = """

cc_library(
    name = "static_libs",
    srcs = glob(["**/*.lib", "**/*.a"]),
    visibility = ["//visibility:public"],
)
"""

cc_library_shared = """
static_srcs = glob(["**/*.lib", "**/*.a"], exclude=["**/*jni.lib"])
shared_srcs = glob(["**/*.dll", "**/*.so*", "**/*.dylib"], exclude=["**/*jni.dll", "**/*jni.so", "**/*.so.debug", "**/libopencv_java*.dylib"])
shared_jni_srcs = glob(["**/*jni.dll", "**/*jni.so*", "**/*.jni.dylib", "**/libopencv_java*.dylib"], exclude=["**/*.so.debug"])

cc_library(
    name = "static_libs",
    srcs = static_srcs,
    visibility = ["//visibility:public"],
)

cc_library(
    name = "shared_libs",
    srcs = shared_srcs,
    visibility = ["//visibility:public"],
    deps = [
        ":static_libs",
    ]
)

cc_library(
    name = "shared_jni_libs",
    srcs = shared_jni_srcs,
    visibility = ["//visibility:public"],
)
"""

def __setup_wpi_opencv_dependencies(mctx):
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_headers",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-headers.zip",
        sha256 = "f2ecc5a319b2c069a1ae2b41741b429eabb585455da1c9b60c3f1ba94bbc5ade",
        build_file_content = cc_library_headers,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_linuxathena",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-linuxathena.zip",
        sha256 = "e6fc728a01d58af3124483a8740d4f9f332674eea85466d5685885c5be7c09be",
        build_file_content = cc_library_shared,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_linuxathenastatic",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-linuxathenastatic.zip",
        sha256 = "3e3156b80de36deea7866049e49e5c5ad940367016eaace94fa77ef40ee7b376",
        build_file_content = cc_library_static,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_windowsx86-64",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-windowsx86-64.zip",
        sha256 = "d2ae81dbaac8b72e78156cc276fdb1cb481faf84f182847f8acbb2f946332e61",
        build_file_content = cc_library_shared,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_linuxx86-64",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-linuxx86-64.zip",
        sha256 = "63458c2c4c8971390e47f6e114579604fd784fb130ce491dc00915981e535410",
        build_file_content = cc_library_shared,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_osxx86-64",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-osxx86-64.zip",
        sha256 = "caf8c8fb69c8ccdc9fc7f51957cd08e503cbb46f71be859f435d78398c36596f",
        build_file_content = cc_library_shared,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_windowsx86-64static",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-windowsx86-64static.zip",
        sha256 = "7e7668b4a5e2b7747c387376cf63340b71d5542f4189fe56a8668e0e887d9a64",
        build_file_content = cc_library_static,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_linuxx86-64static",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-linuxx86-64static.zip",
        sha256 = "c6c8da3f212147810f17fcb28ad22ded11b47e4b8c0021e48f234142ef0eaa5c",
        build_file_content = cc_library_static,
    )
    maybe(
        http_archive,
        "bazelrio_edu_wpi_first_thirdparty_frc_opencv_opencv-cpp_osxx86-64static",
        url = "https://frcmaven.wpi.edu/release/edu/wpi/first/thirdparty/frc2021/opencv/opencv-cpp/3.4.7-4/opencv-cpp-3.4.7-4-osxx86-64static.zip",
        sha256 = "bc57495846187b238556c416adb508edee974ca90df0b782c5f47d69ed7741dd",
        build_file_content = cc_library_static,
    )

setup_wpi_opencv_dependencies = module_extension(
    __setup_wpi_opencv_dependencies,
)
