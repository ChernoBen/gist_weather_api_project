import pytest
from unittest.mock import patch
from src.adapters.pygithub_adapter import PyGitHubAdapter
from src.adapters.exceptions.pygithub_exceptions import PyGitHubException

# Testing if add_comment_to_gist method adds a comment to a gist and it return an url
@patch('src.adapters.pygithub_adapter.Github')
def test_add_comment_success(mock_github):
    mock_gist = mock_github.return_value.get_gist.return_value
    mock_gist.html_url = "https://gist.github.com/fake_gist_url"
    
    adapter = PyGitHubAdapter(access_token="fake_token")
    url = adapter.add_comment_to_gist("This is a test comment")
    
    assert url == "https://gist.github.com/fake_gist_url"
    mock_gist.create_comment.assert_called_once_with("This is a test comment")

# Testing if add_comment_to_gist method raises a PyGitHubException
def test_empty_comment_error():
    adapter = PyGitHubAdapter(access_token="fake_token")
    
    with pytest.raises(PyGitHubException, match="O comentário não pode estar vazio."):
        adapter.add_comment_to_gist("")


