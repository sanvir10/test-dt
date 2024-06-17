import pytest
from download_td import util

def test_validate_empty_url():
    with pytest.raises(ValueError) as excinfo:  
        util.Util().validateUrl("")  
    assert str(excinfo.value) == "Invalid URL(Empty URL)"  

def test_validate_invalid_url():
    with pytest.raises(ValueError) as excinfo:  
        util.Util().validateUrl("https://drive.google.co/file/d/1aNAL2jravbMF3BS6GP4G1C-5ONrKHLWG/view?usp=sharing")  
    assert str(excinfo.value) == "Invalid URL, this must contains: drive.google.com"

def test_validate_url_structure():
    with pytest.raises(ValueError) as excinfo:  
        util.Util().validateUrl("https://drive.google.co/file/1aNAL2jravbMF3BS6GP4G1C-5ONrKHLWG/view?usp=sharing")  
    assert str(excinfo.value) == "Invalid URL(Incorrect structure)"

