#--utf-8--
#-------------------------------------------------------------------------------
# Name:        Arithmetic Practice Buddy
# Purpose:for helping in arithmetic defficiencies
#
# Author:      Hiram
#
# Created:     12/04/2013
# Copyright:   (c) Hiram 2013
# Licence:     <GlPL>
#-------------------------------------------------------------------------------

'''
TODO: !!!start application blank*
TODO: !!!when press Start sess, then show first problem*
TODO: !!!display operator vis a vis expression*
TODO: !!!build expressions maker*
TODO: !show more problems*
TODO: !!!count number of problems*
'''
'''
TODO:____________*
TODO:____________*
TODO:Time_Line
TODO:Start -->Open App*
TODO:   show warn if stop or start pressed
TODO:   before picking option, to pick options *
TODO:Pick Options *
TODO:Press Start --> Starts Problems *
TODO:check what if choose other things while running
TODO:____________*
TODO:____________*
TODO: !!!Connect Op_buttons -->Op_Types *
TODO: !!!Connect Range_buttons --> Range_Types *
TODO: !!!Start blank *
TODO:Start button --> starts problmes/Timer/SPACE_BAR*
TODO:Stop button --> stops problmes /Timer/SPACE_BAR*
TODO:____________*
TODO:____________*
TODO: !!!Operations Runner*
TODO:        when op_button/s pressed*
TODO:        only those ops are made and displayed*
TODO:_____________
TODO:_____________
TODO: !!!Range_runner*
TODO:       when range_button/s pressed*
TODO:        only those ranges used*
TODO:_____________

'''

import sys
import random
import mainGui
import decimal
from PySide import QtGui
from PySide import QtCore

class Ex_Signal(QtCore.QObject):

    #:This is the name of the signal
    runner_sig = QtCore.Signal()
    focus_signal = QtCore.Signal()
    disconnect_signal = QtCore.Signal()
    #art_event_loop = QtCore.QEventLoop()
    
class MainWindow(QtGui.QMainWindow, mainGui.Ui_MainWindow):
    """Main Gui class"""

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        
        #:Signal emmission instance.tiation
        self.prob_signal = Ex_Signal()

        self.top_lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.top_lineEdit.setReadOnly(True)

        self.bottom_lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.bottom_lineEdit.setReadOnly(True)

        self.answer_lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.answer_lineEdit.setMaxLength(8)
        
        decimal_validator = QtGui.QDoubleValidator()
        decimal_validator.setDecimals(3)
        self.answer_lineEdit.setValidator(decimal_validator)

        self.prog_start()

    #:when radio button emits a signal, slot adds parameter
    def prog_start(self):
        """ Connects functions to settings and sets some parameters """
        #:Disable buttons I cannot use now
        self.format_converter.setEnabled(False)
        self.consec_op.setEnabled(False)
        self.rand_op.setEnabled(False)

        #:toggled connections for op_types
        self.mult_option.toggled.connect(self.set_op_types)
        self.div_op.toggled.connect(self.set_op_types)
        self.plus_op.toggled.connect(self.set_op_types)
        self.subtr_op.toggled.connect(self.set_op_types)

        #:toggled connections of range types
        self.ones_option.toggled.connect(self.num_ranges)
        self.tens_option.toggled.connect(self.num_ranges)
        self.hundred_op.toggled.connect(self.num_ranges)
        self.ten_ths_option.toggled.connect(self.num_ranges)
        self.hundre_ths_op.toggled.connect(self.num_ranges)

        self.num_range = []
        self.op_types = []
        self.start_button_status = 0
        self.kotoro = 0
        
        #:this starts the ex_initialator from the start button
        self.start_button.clicked.connect(self.ex_initialator)

        #:half - fix for the no focus policy
        self.start_button.clicked.connect(self.focus_policy)
        
        #:Stop problem runner
        self.stop_button.clicked.connect(self.destructonometer)
        
    def ex_initialator(self):
        """ sets up things for the problem runner """
        
        print "ayadara"
        print "self.start_button_status this is...::" ,self.start_button_status
        
        #:Pop up dialogs       
        no_options_selected = QtGui.QMessageBox()
        no_options_selected.setIcon(no_options_selected.Information)
        no_options_selected.setText("Please select from the options provided")
        
        select_range = QtGui.QMessageBox()
        select_range.setIcon(no_options_selected.Information)
        select_range.setText("Please select at least one of the ranges")
        
        select_op_type = QtGui.QMessageBox()
        select_op_type.setIcon(no_options_selected.Information)
        select_op_type.setText("Please select at least one operation type")
        
        
        #:Shows message if no options selected       
        if len(self.op_types) < 1 and len(self.num_range) < 1 and self.start_button_status == 0:
            print "Please pick from the options provided"
            no_options_selected.exec_()
            
        #:Shows message if range is not selected
        if len(self.op_types) >= 1 and len(self.num_range) < 1 and self.start_button_status == 0 :
            print "Please pick at least one of the ranges"
            select_range.exec_()
            
        #:Shows message if op_type/s not selected
        if len(self.op_types) < 1 and len(self.num_range) >= 1 and self.start_button_status == 0:
            print "Please pick at least one of the operation types"        
            select_op_type.exec_()
        
        #:Correct inputs initiates problem maker
        if len(self.op_types) >= 1 and len(self.num_range) >= 1 and (self.start_button_status == 0 or self.start_button_status == 1):
           self.start_button_status = 1
           self.prob_signal.runner_sig.connect(self.problem_runner)
           self.prob_signal.runner_sig.emit()           

        '''
         #self.prob_signal.runner_sig.connect(self.destructonometer)
        
         #:Emit destructonometer signal only when pressing stop
         self.prob_signal.runner_sig.emit()'''

    def problem_runner(self):
        """ Expression Makers """
        while self.start_button_status == 1:

            #:picks range types
            range_type = random.choice(self.num_range)
            
            D = decimal.Decimal
            
            if range_type == 'ones':
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
            elif range_type == 'tens':
                num1 = random.randint(10, 100)
                num2 = random.randint(10, 100)        
            elif range_type == 'hundreds':
                num1 = random.randint(1, 999)
                num2 = random.randint(1, 999)        
            elif range_type == 'tenths':
                num1 = D(random.randrange(10)) /10
                num2 = D(random.randrange(10)) /10
            elif range_type == 'hundreths':
                num1 = D(random.randrange(10)) /100
                num2 = D(random.randrange(10)) /100
            

            #:picks the problem types
            op_type = random.choice(self.op_types)

            #:Sets Top and Bottom Nums
            if num1 >= num2:
                top_num = num1
                btm_num = num2
            elif num2 >= num1:
                top_num = num2
                btm_num = num1
            
            #:Sends Nums to their respective Line Edits
            self.top_lineEdit.setText(str(top_num))
            self.bottom_lineEdit.setText(str(btm_num))

            #addition
            def addition(num1, num2):
                #:Send signal to pixmap for addition
                self.operator_displ.setPixmap(QtGui.QPixmap(":/icons/Plus.png"))
                add_answer = top_num + btm_num
                return add_answer

            #multiplication
            def multiplication(num1, num2):
                #:Send signal to pixmap for mult
                self.operator_displ.setPixmap(QtGui.QPixmap(":/icons/Mult.png"))
                mult_answer = top_num * btm_num
                return mult_answer

            #subtraction
            def subtraction(num1, num2):
                #:Send signal to pixmap for subtraction
                self.operator_displ.setPixmap(QtGui.QPixmap(":/icons/Min.png"))
                sub_answer = top_num - btm_num
                return sub_answer

            #:Division TODO:add division
            def division(num1, num2):
                
                #:when I input 3/12 I got 0 for answer
                #:when I input 12/3 I got 4 for answer
                #         ____
                #:So     3|12 == 12/3 which maks sense
                #:3 ÷ 12 = 0.25 where as, 12 ÷ 3 = 4
                #:and so it seems that the bigger of the two numbers for
                #:this application needs to go on the top so we 
                
                #:Send signal to pixmap for division
                self.operator_displ.setPixmap(QtGui.QPixmap(":/icons/Div.png"))
                div_answer = top_num / btm_num
                return div_answer
                pass

            
            #:Checks for op_type and sends signals accordingly
            if op_type == "mult":
                self.op_answ = multiplication(top_num, btm_num)
                #self.answer_lineEdit.returnPressed.connect(self.ex_evaluator)
            elif op_type == "div":
                self.op_answ = division(top_num, btm_num)
                #self.answer_lineEdit.returnPressed.connect(self.ex_evaluator)
            elif op_type == "add":
                self.op_answ = addition(top_num, btm_num)
                #self.answer_lineEdit.returnPressed.connect(self.ex_evaluator)
            elif op_type == "sub":
                self.op_answ = subtraction(top_num, btm_num)
                #self.answer_lineEdit.returnPressed.connect(self.ex_evaluator)
            self.answer_lineEdit.returnPressed.connect(self.ex_evaluator)
            
            self.answer_lineEdit.clear()
        
            QtGui.QApplication.processEvents()
        
    #:Expression Evaluator
    def ex_evaluator(self):
        """ Evaluates User input """

        self.answer = self.answer_lineEdit.text()
        
        D = decimal.Decimal
        
        print "this is your answer", self.answer
        print "this is correct answer", self.op_answ
        
        if D(self.answer) == self.op_answ:
            print "yahoo we have liftoff"
        else:
            print "wrong answer"
            
        self.kotoro = self.kotoro + 1 
        
        print "inside ex_evaluator this is kotoro...::" ,self.kotoro        
                
        #:So this works because it disconnects all connections 
        self.answer_lineEdit.returnPressed.disconnect()
        #self.answer_lineEdit.returnPressed.connect(self.destructonometer)
  
    #Checks for Spacebar press and sets parameters
    def keyPressEvent(self, s):
    
        if s.key() == QtCore.Qt.Key_Z: 
            print "key press event...::" ,self.start_button_status
            print "space bar pressed"
            
            #:Sends signal that start button was clicked..It connects
            #:to it in a roundabout way
            self.start_button.click()
    
    def destructonometer(self):
    
        print "we be destroying shit"
        '''
        self.start_button_status = 1
        self.top_lineEdit.clear()
        self.bottom_lineEdit.clear()
        self.answer_lineEdit.clear()
        self.answer_lineEdit.returnPressed.disconnect()
        '''    
            
    #:Number choice ranges
    def num_ranges(self):
        """ Contains ranges for range radio buttons """

        self.num_range = []

        if self.ones_option.isChecked():
            self.num_range.append('ones')
        if self.tens_option.isChecked():
            self.num_range.append('tens')
        if self.hundred_op.isChecked():
            self.num_range.append('hundreds')
        if self.ten_ths_option.isChecked():
            self.num_range.append('tenths')
        if self.hundre_ths_op.isChecked():
            self.num_range.append('hundreths')
         
    def set_op_types(self):
        """ Makes the setting of op_types """

        self.op_types = []
        if self.mult_option.isChecked():
           self.op_types.append('mult')
        if  self.div_op.isChecked():
            self.op_types.append('div')
        if self.plus_op.isChecked():
            self.op_types.append('add')
        if self.subtr_op.isChecked():
            self.op_types.append('sub')

    def focus_policy(self):

        self.answer_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        

def student_records(self):
    #Name
    #Log-in/Sign-in
    #New Student
    #Del Student
    #Session Stats
        #Types of sessions Timings
            #Mult
            #Div
            #Plus
            #Sub
            #Cons
            #Rand
    pass

def timings(self):
    #:Divide the numbers by the amount of time it takes to answer the problem
    #:    by time
    #timings for ones .5 - 1.0 seconds
    #timings for decs 2 - 3.5
    #timings for hundreds 3 -8, 8-16, 16-20
    #timings for tenths .5 - 1.0
    #timings for hudreths 2 -3.5
    pass

def wrong_answer(self):
    #:Show that the answer was wrong in red
    #:Write the right answer in green
    pass


def main():
    """Runs the module"""
    app = QtGui.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()






















































