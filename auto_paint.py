#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PointCloudClass.channel_pointcloud import ChannelPointCloud
from PointCloudClass.trans_format import transToPLY

# Param
xyz_pointcloud_file_path = "./masked_pc/office/office_cut.ply"

label_pointcloud_file_path = "./masked_pc/office/office_DownSample_8_masked.pcd"
label_channel_name = "label"

outlier_dist_max = 0.05
estimate_normals_radius = 0.05
estimate_normals_max_nn = 30

d3_40_colors_rgb = [
    [164, 218, 252], [120, 173, 219], [253, 147, 81], [252, 234, 163], [0, 128, 128],
    [132, 220, 198], [255, 104, 107], [255, 166, 158], [148, 103, 189], [189, 147, 189],
    [140, 86, 75], [146, 94, 120], [227, 119, 194], [247, 182, 210], [127, 127, 127],
    [199, 199, 199], [188, 189, 34], [219, 219, 141], [23, 190, 207], [158, 218, 229],
    [57, 59, 121], [82, 84, 163], [107, 110, 207], [156, 158, 222], [99, 121, 57],
    [140, 162, 82], [181, 207, 107], [206, 219, 156], [140, 109, 49], [189, 158, 57],
    [231, 186, 82], [231, 203, 148], [132, 60, 57], [173, 73, 74], [214, 97, 107],
    [231, 150, 156], [123, 65, 115], [165, 81, 148], [206, 109, 189], [222, 158, 214]]

# Process
painted_pointcloud_file_path = xyz_pointcloud_file_path[:-4] + "_painted.pcd"

xyz_pointcloud = ChannelPointCloud()
xyz_pointcloud.loadData(xyz_pointcloud_file_path)

label_pointcloud = ChannelPointCloud()
label_pointcloud.loadData(label_pointcloud_file_path)

merge_pointcloud = ChannelPointCloud()
merge_pointcloud.copyChannelValue(xyz_pointcloud, ["x", "y", "z"])
merge_pointcloud.setChannelValueByKDTree(label_pointcloud, ["label"])
merge_pointcloud.removeOutlierPoints(outlier_dist_max)
merge_pointcloud.paintByLabel(label_channel_name, d3_40_colors_rgb)
merge_pointcloud.savePointCloud(painted_pointcloud_file_path)

transToPLY(painted_pointcloud_file_path, estimate_normals_radius, estimate_normals_max_nn)

