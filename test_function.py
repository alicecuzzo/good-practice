import function 
from mock import patch, Mock

def test_ok_function():
    expected_value = 24
    actual_value = function.ok_function()
    assert expected_value == actual_value, 'bjeogsj'
def test_pass():
    assert 1==1
#def test_wrong():
#    assert 1==0
#def test_sbaglito():
#    assert 1==2, 'niente'

#def test_text_analysis(): #mock_call):

#    wc = function.do_text_analysis()
#    assert wc > 0, 'Text should have more than 0 lenght'

#patch('function.download_text_from_web'
#def test_text_analysis(moke_call):
#   moke_call.return_value = 'Some mock text'

#@patch('requests.get')
#def test_text_analysis(mock_call):
#    mock_call.return_value = Mock()
#    mock_call.return_value.text = 'fake text'
#    wc = function.do_text_analysis()
#    assert wc > 0, 'Text should have more than 0 lenght'


@patch('requests.get')
def test_text_analysis(mock_call):
    mock_call.return_value = Mock()
    mock_call.return_value.text = 'fake text'
    wc = function.do_text_analysis()
    kal =  mock_call.call_args_list[0]
    args, kwar = kal
    print args
    assert wc > 0, 'Text should have more than 0 lenght'

    
