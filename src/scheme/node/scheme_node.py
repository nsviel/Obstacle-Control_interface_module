#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection
from src.scheme.command import scheme_callback
from src.scheme.command import scheme_com
from src.scheme.command import scheme_com_mongo

from src.scheme.node.interface import node_module_interface
from src.scheme.node.train import node_module_capture
from src.scheme.node.edge import node_module_edge
from src.scheme.node.train import node_train
from src.scheme.node.edge import node_module_edge_next
from src.scheme.node.edge import node_data_processing
from src.scheme.node.interface import node_network

from src.scheme.node.edge import node_ai
from src.scheme.node.cloud import node_operator
from src.scheme.node.cloud import node_cloud
from src.scheme.node.interface import node_ssd
from src.scheme.node.interface import node_data

import dearpygui.dearpygui as dpg


def create_node():
    node_train.design_block()
    node_module_edge.design_block()
    node_cloud.design_block()

    node_module_interface.design_node()
    node_module_capture.design_node()
    node_module_edge.design_node()
    node_train.design_node()
    node_module_edge_next.design_node()
    node_data_processing.design_node()
    node_ai.design_node()
    node_operator.design_node()
    node_cloud.design_node()
    node_ssd.design_node()
    node_data.design_node()
    node_network.design_node()


def node_legend():
    with dpg.node(label="Legend", tag="node_legend"):
        scheme_function.add_legend_line("legend_train", "Train level components")
        scheme_function.add_legend_line("legend_edge", "Edge level components")
        scheme_function.add_legend_line("legend_cloud", "Cloud level components")
        scheme_function.add_legend_line("legend_control", "Control level components")