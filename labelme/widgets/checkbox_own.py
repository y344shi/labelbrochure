from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QMessageBox, QComboBox, QLabel, QLineEdit, \
    QHBoxLayout, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal

import sys


class CheckBoxSmart(QWidget):
    Signal_OneParameter = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.checkbox_storage = {}
        self.checkbox_storage_with_themes = {}
        self.set_up_boxes()
        self.output_dic_og = self.read_boxes()
        self.set_uncheckable(False)
        self.show()

    def set_up_boxes(self):

        ### 用于循环创造表格的数据 ###
        themes = {'商业': ['具体商品活动', '品牌活动', '场所活动'],
                  '非商业': ['知识宣传', '活动宣传']}
        location = {'线上': ['商场', '超市', '线下屏幕', '交通办公场所', '餐饮娱乐产所和社区'],
                    '线下': ['公司/品牌官网', '购物网站', '社交/娱乐网站', '社交软件']}
        elements = {'偏向构成要素': ['极简-强功能指向', '极简-简约', '超写实', 'MBE插画', '立体主义', '低面建模', '欧普', '极繁', '像素'],
                    '偏向色彩': ['波普', '赛博朋克', '蒸汽波'],
                    '二者都有': ['哥特', '孟菲斯', '蒸汽朋克']}
        culture = {'时间': ['现代', '古风'],
                   '节日': ['春', '夏', '秋', '冬天'],
                   '艺术类型': ['雕塑', '国画写意', '国画工笔', '篆刻', '书法', '其他工艺品']}
        others = {'其他': ['其他']}

        list_names = ['主题', '地点', '构成元素', '文化元素', '其他']
        list_name_data = [themes, location, elements, culture, others]

        divisor = 6

        self.the_window = QVBoxLayout()
        self.setLayout(self.the_window)

        name_index = 0

        for categories in list_name_data:

            line_shape = '-----------------------------------------------------------------------(' \
                         '0.0)/`----------------------------------------------------------------------- '
            line_shape2 = '------------------------------------------------------------------------------------------' \
                          '------------------------------------------------------------ '
            self.label_catagory_line = QLabel(line_shape)
            self.label_catagory = QLabel('[ ' + list_names[name_index] + ' ]')
            self.label_catagory_line2 = QLabel(line_shape2)

            self.the_window.addWidget(self.label_catagory_line)
            self.the_window.addWidget(self.label_catagory)

            self.temp_dic_storage = {}

            for keys in categories:

                self.label_key = QLabel(keys)

                local_list = categories[keys]
                len_ = 0

                # find out the length of a subject manually:
                for items in local_list:
                    len_ += 1
                # print(len_)

                # determining how many loops:
                num_loops = int(len_ / divisor)

                if len_ % divisor != 0:
                    num_loops += 1

                # the giant loop for creating checkboxes
                index_for_atoms = 0
                for i in range(num_loops):

                    j = 0
                    self.partial_layout_math_controlled = QHBoxLayout()
                    if i == 0:
                        self.partial_layout_math_controlled.addWidget(self.label_key)
                    self.partial_layout_math_controlled.addStretch(1)

                    while j < divisor and index_for_atoms < len_:
                        print('looop', index_for_atoms, j, categories[keys][index_for_atoms])
                        self.tep_checkbox = QCheckBox()
                        self.tep_checkbox.setCheckState(False)
                        self.tep_checkbox.setText(categories[keys][index_for_atoms])
                        self.tep_checkbox.clicked.connect(self.clicked)
                        self.partial_layout_math_controlled.addWidget(self.tep_checkbox)
                        self.checkbox_storage[self.tep_checkbox.text()] = self.tep_checkbox
                        self.temp_dic_storage[self.tep_checkbox.text()] = self.tep_checkbox

                        """if categories[keys][index_for_atoms] == '其他': #or  categories[keys][index_for_atoms] == '其他':
                            self.temp_text_edit = QLineEdit()
                            self.temp_text_edit.setObjectName(keys)
                            self.temp_text_edit.setPlaceholderText('input ' + keys + ' descriptions')
                            self.temp_text_edit.textChanged.connect(self.text_changed)
                            self.the_window.addWidget(self.temp_text_edit)
                            self.line_edit_storage[self.temp_text_edit.objectName()] = [self.temp_text_edit, '']
                            self.temp_text_edit.setDisabled(True)"""

                        index_for_atoms += 1
                        j += 1

                    # self.partial_layout.addStretch(1)
                    self.partial_layout_math_controlled.addStretch(1.8)
                    # self.the_window.addLayout(self.partial_layout)
                    self.the_window.addLayout(self.partial_layout_math_controlled)

            self.checkbox_storage_with_themes[list_names[name_index]] = self.temp_dic_storage

            #self.the_window.addWidget(self.label_catagory_line2)

            name_index += 1


        '''self.submit_button = QPushButton()
        self.submit_button.setText('Submit Selections & save')
        self.submit_button.clicked.connect(self.read_boxes)
        self.the_window.addWidget(self.submit_button)'''

    """def text_changed(self):
        print(self.sender().objectName(), ':', self.sender().text())

        self.line_edit_storage[self.sender().objectName()][1] = self.sender().text()
        print(self.line_edit_storage)"""

    def emit_signal(self):
        is_original = (self.output_dic_og == self.read_boxes())
        print('is_original = ', is_original)
        self.Signal_OneParameter.emit(is_original)

    def clicked(self):
        sender = self.sender().text()
        checkstate = self.checkbox_storage[sender].isChecked()
        self.emit_signal()
        print(sender, checkstate)
        #if sender in self.line_edit_storage:
            #self.line_edit_storage[sender][0].setDisabled(not checkstate)

    def update_boxes(self, data_set):
        for catagories in data_set:
            for items in data_set[catagories]:
                self.checkbox_storage_with_themes[catagories][items].setCheckState(Qt.Checked)

    def reSet(self):
        for catagories in self.checkbox_storage_with_themes:
            for keys in self.checkbox_storage_with_themes[catagories]:
                self.checkbox_storage_with_themes[catagories][keys].setCheckState(Qt.Unchecked)

        # cbox = QCheckBox()
        # cbox.setDisabled()

    def set_uncheckable(self, boool):
        for catagories in self.checkbox_storage_with_themes:
            for keys in self.checkbox_storage_with_themes[catagories]:
                self.checkbox_storage_with_themes[catagories][keys].setDisabled(boool)

    #def is_line_edit(self):


    def read_boxes(self):
        print('checked_boxes:')
        output_dic = {}
        str_checked = ''
        for categories in self.checkbox_storage_with_themes:
            str_checked += categories
            str_checked += ': '
            # print(self.checkbox_storage_with_themes[categories])
            temp_keys_under_catagories = []
            for keys in self.checkbox_storage_with_themes[categories]:

                if self.checkbox_storage_with_themes[categories][keys].isChecked():
                    temp_keys_under_catagories.append(keys)
                    str_checked += keys + ', '
                    if

            output_dic[categories] = temp_keys_under_catagories
            str_checked += ' \n'

        # QMessageBox.about(self, '提交:', ' 您成果将这张图片归类为:\n\n' + str(str_checked))
        # print('internal storage:', self.checkbox_storage_with_themes)
        return output_dic

    def set_original(self, dict_og):
        print('og set')
        self.output_dic_og = dict_og

    def __str__(self):
        return_data = self.read_boxes()
        # print('return_data = :', return_data)
        return return_data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckBoxSmart()
    ex.show()
    sys.exit(app.exec_())
