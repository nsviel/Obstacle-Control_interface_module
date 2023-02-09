#---------------------------------------------
from src.scheme import scheme_function
from src.scheme import scheme_com
from src.scheme import scheme_com_lidar

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)
color_title = (200, 200, 200)


def add_sock_server(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("server", color=color_info);
def add_sock_server_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("server", color=color_info);
def add_sock_server_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("server", color=color_info);
def add_sock_server_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("server", color=color_info);
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1

def add_sock_client_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("client", color=color_info);
def add_sock_client_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("client", color=color_info);
def add_sock_client_o_(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Socket");
            dpg.add_text("client", color=color_info);

def add_sock_client_source_i(tag_i, tag_source):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
        with dpg.group(horizontal=True):
            dpg.add_text("Source:");
            dpg.add_text("Lidar 2", tag=tag_source, color=color_info)
def add_sock_client_source_o(tag_i, tag_source):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
        with dpg.group(horizontal=True):
            dpg.add_text("Source:");
            dpg.add_text("Lidar 2", tag=tag_source, color=color_info)
def add_sock_client_source_io(tag_i, tag_o, tag_combo, vis_1, vis_2):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(tag=vis_1):
            scheme_function.line()
            with dpg.group(horizontal=True):
                dpg.add_text("Socket");
                dpg.add_text("client", color=color_info);
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(tag=vis_2, horizontal=True):
            dpg.add_text("Source:");
            choice = ("lidar_1", "lidar_2")
            dpg.add_combo(choice, tag=tag_combo, label="", default_value="Lidar 1", width=80, callback=scheme_com_lidar.command_combo_lidar_main)

def add_http_client_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("client", color=color_info);
def add_http_client_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("client", color=color_info);
def add_http_client_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("client", color=color_info);
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1

def add_http_server_i_text(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        scheme_function.line()
        dpg.add_text(text, color=color_title);
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("server", color=color_info);
def add_http_server_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("server", color=color_info);
def add_http_server_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("server", color=color_info);
def add_http_server_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        with dpg.group(horizontal=True):
            dpg.add_text("HTTPS");
            dpg.add_text("server", color=color_info);
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1