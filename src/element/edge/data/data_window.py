#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Data_window(window.Window):
    # Build function
    def build_parameter(self):
        pass

    # Command function
    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"]["data"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

    # Update function
    def update(self):
        pass
    def update_data(self):
        dpg.set_value(self.ID.ID_nb_frame, edge.state["data"]["nb_frame"])
        dpg.set_value(self.ID.ID_nb_prediction, edge.state["data"]["nb_prediction"])
