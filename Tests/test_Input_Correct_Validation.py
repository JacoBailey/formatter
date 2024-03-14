import pytest, re, sys
from pathlib import Path
from unittest.mock import patch
#----------------------------------------------------------------------------
#----- Logic below ensures custom modules can be found by python/pytest -----
#----------------------------------------------------------------------------
testFilename = Path(__file__).name
testDirec_Str = re.sub(testFilename, '', str(__file__), count=1)
mainProgDirec_Str = re.sub(r'(/|\\)Tests(/|\\)', '', testDirec_Str, count=1)
sys.path.append(mainProgDirec_Str)
#----------------------------------------------------------------------------
import Mods_Packs_Libs

@patch('Mods_Packs_Libs.Input_Correct_Validation.pyip.inputYesNo')
@patch('Mods_Packs_Libs.Input_Correct_Validation.input')
class Test_Input_Correct_Validation:   

    @pytest.mark.parametrize('inputYesNoValue', ['yes', 'y', 'YES', 'Y', 'Yes' 'yEs', 'yeS', 'YEs', 'yES', 'YeS'])
    def test_YesInput(self, mock_input, mock_inputYesNo, inputYesNoValue):
        mock_input.return_value = 'test'
        mock_inputYesNo.return_value = inputYesNoValue
        assert Mods_Packs_Libs.input_correct_validation('test', 'testInput') == 'test'

    @pytest.mark.parametrize('inputYesNoValue', ['no', 'n', 'NO', 'N', 'No' 'nO'])
    def test_NoInput(self, mock_input, mock_inputYesNo, inputYesNoValue):
        mock_input.return_value = 'test'
        mock_inputYesNo.return_value = inputYesNoValue
        assert Mods_Packs_Libs.input_correct_validation('test', 'testInput', noTest=True) == False