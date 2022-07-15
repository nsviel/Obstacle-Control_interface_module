#! /usr/bin/python
#---------------------------------------------

from param import param_co
from conn import http_client_get
from conn import http_client_post
from src import saving
from src import parser_json

import dearpygui.dearpygui as dpg


def callback_update_conf():
    pass

def callback_lidar_1():
    param_co.state_co["lidar_1"]["speed"] = dpg.get_value("l1_speed")
    param_co.state_co["lidar_1"]["ip"] = dpg.get_value("l1_ip")

def callback_lidar_2():
    param_co.state_co["lidar_2"]["speed"] = dpg.get_value("l2_speed")
    param_co.state_co["lidar_2"]["ip"] = dpg.get_value("l2_ip")

def callback_l1_start():
    http_client_post.post_lidar_start("lidar_1")

def callback_l1_stopt():
    http_client_post.post_lidar_stop("lidar_1")

def callback_l2_start():
    http_client_post.post_lidar_start("lidar_2")

def callback_l2_stopt():
    http_client_post.post_lidar_stop("lidar_2")

def callback_false_alarm():
    http_client_get.get_falsealarm()

def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")
    param_co.state_py["path"]["additional"] = dpg.get_value("ssd_path_add")
    saving.determine_path()

def callback_param_py():
    param_co.state_py["lidar_1"]["device"] = str(dpg.get_value("py_l1_device"))
    param_co.state_py["lidar_2"]["device"] = str(dpg.get_value("py_l2_device"))
    param_co.state_py["self"]["http_server_port"] = dpg.get_value("py_http_server_port")
    parser_json.upload_file(param_co.path_state_py, param_co.state_py)
    http_client_post.post_new_param_py("lidar_1", "device", str(dpg.get_value("py_l1_device")))
    http_client_post.post_new_param_py("lidar_2", "device", str(dpg.get_value("py_l2_device")))

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.ip)
